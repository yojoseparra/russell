# Warren Buffet to select companies based on book 'The Guru Investor' By John P. Reese

# --------------------------------------------------------------------------------------------------------
# --------------------------------------------- MOAT Pair Compare ----------------------------------------
# --------------------------------------------------------------------------------------------------------
# Query the database and load directly into a DataFrame

# connecting to postgreSQL
exec(open('connect2sql.py').read())

# Query the database and load directly into a DataFrame
a = pd.read_sql_query("SELECT a.* , scgrpid, sctestcd  from ru.admo as a left join ru.sc as b on a.fitest = b.sctest0 and a.ficat = b.scgrp", conn)
print(a)
b=a.copy()
# Ensure 'date' is a datetime object
import pandas as pd
a['period'] = pd.to_datetime(a['fidtc'], format="%Y-%m-%d").dt.date

def long2wide(tickers=[ 'AMZN', 'BABA'], dataframe=a):
    pd.options.mode.chained_assignment = None  # Turn off the warning
    # the following displays the ticker data wide accross years
    # This code works with 2 tickers
    b=dataframe[dataframe.subjid.isin(tickers)].copy()
    c = b[['subjid', 'scgrpid','ficat', 'sctestcd', 'fidtc', 'chg', 'fistresn', 'fiperiod']].sort_values(by=['subjid', 'ficat','scgrpid', 'fidtc'])
    c = c.melt(id_vars=['subjid', 'scgrpid','ficat', 'sctestcd', 'fiperiod', 'fidtc'], value_vars= ['chg', 'fistresn' ] , var_name='param', value_name='aval')
    c['param'] = c['param'].str.upper()
    # Theere are duplicates
    #duplicates = c[c.duplicated(subset=['subjid', 'ficat', 'scgrpid', 'sctestcd', 'fiperiod', 'fidtc', 'param'], keep=False)]
    #print(duplicates)
    c=c.sort_values(by=  ['subjid', 'ficat','scgrpid', 'param', 'fidtc'] )

    c = c.pivot(index=['subjid','ficat','scgrpid', 'sctestcd', 'fiperiod','fidtc'], columns=[ 'param'], values='aval') 
    c.reset_index(inplace=True)
    d = c.pivot(index=['subjid','ficat','scgrpid', 'sctestcd', 'fiperiod'], columns=[ 'fidtc']) 

    # There are many columns with scarce data, these columns must leave
    # Define a threshold for minimum non-null values (e.g., 50%)
    threshold = 0.1 * len(d)
    # Drop columns with scarce data
    d = d.dropna(axis=1, thresh=threshold)


    # Simplify column names
    # Flatten MultiIndex columns
    d.columns = ['_'.join(map(str, col)).strip() for col in d.columns]
    # we go from ' FISTRESN_2021-12-31 00:00:00' to 'FIS_2021-03-31'
    d.columns = [f"{col.split('_')[0][:3]}_{col.split('_')[1].split(' ')[0]}"
                    if "_" in col else col  # Handles columns that are not in the expected format
                    for col in d.columns]

    d.reset_index(inplace=True)



    da = d[d['subjid'] == tickers[0]]
    threshold = 0.1 * len(da)
    da = da.dropna(axis=1, thresh=threshold)
    # There are duplicated for the last quarter, the 'TTM'. We are adding this one as an additional column
    da_latest = da[da['fiperiod'] == 'TTM']
    da_latest = da_latest.dropna(axis=1, thresh=threshold)
    da = da[da['fiperiod'] != 'TTM']
    numeric_columns_a = da_latest.select_dtypes(include='number') # sometimes Da_latest do not have data one numeric column is scgrpid


    if (  len(numeric_columns_a.columns) > 1 ):
        da = da.merge(da_latest, on= ['subjid','ficat','scgrpid', 'sctestcd'], how='left' )
    #e.to_csv('data/e.csv')
    db = d[d['subjid'] == tickers[1]]

    db = db.dropna(axis=1, thresh=threshold)

    db_latest = db[db['fiperiod'] == 'TTM']
    db_latest = db_latest.dropna(axis=1, thresh=threshold)
    db = db[db['fiperiod'] != 'TTM']
    numeric_columns_b = db_latest.select_dtypes(include='number') # sometimes Db_latest do not have data, meaning TTM does not have financial data


    if ( len(numeric_columns_b.columns) > 1 ):
        db = db.merge(db_latest, on= ['subjid','ficat','scgrpid', 'sctestcd'], how='left' )

    e = da.merge(db, on= ['ficat','scgrpid', 'sctestcd'], how='outer' )
    #e.columns = e.columns.set_levels([level.str.replace('-12-31', '', regex=False) if level.dtype == 'object' else level for level in e.columns.levels])
    return e
    
# creating a list to iterate the tickers
from itertools import combinations
subjid = a['subjid'].unique()
pairs = list(combinations(subjid, 2))
# Convert tuples to lists
pairs = [list(tup) for tup in pairs]

# Convert to strings with a percentage sign
processing = [ round((i + 1) / len(pairs) * 100) for i in range(len(pairs))]
percentages = [f"{p}%" for p in processing]
pairs = list(combinations(subjid, 2))
processing = dict(zip(pairs, percentages))

# --------------------------------------------------------------------------------------------------------------------------
# ---------------------------This creates an excel with the financials of two companies ------------------------------------
import numpy as np
for tickers in pairs:
    pd.options.mode.chained_assignment = None  # Turn off the warning
    print(tickers)
    print(processing[tickers])
    e = long2wide(tickers=tickers)
    #tickers = pairs[2]
    # ------------------------------------------------- Presenting data in console as percentages ---------------------------
    # -----------------------------------------------------------------------------------------------------------------------
    # Transform all numeric columns to percentages
    numeric_cols = e.select_dtypes(include='number').columns
    e[numeric_cols] = e[numeric_cols] * 100
    # Optional: Format as strings with '%' sign
    #e[numeric_cols] = e[numeric_cols].applymap(lambda x: f"{x:.0f}%")
    e[numeric_cols] = e[numeric_cols].applymap(lambda x: f"{x:.0f}%" if not pd.isna(x) else np.nan)
    e.to_csv( 'data/archive/ADMO_'+tickers[0] + '_' + tickers[1] +'_V.2.csv', index=False )



# --------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------- COSINE DISTANCE FOR A SINGLE COMPANY -----------------------------------
# connecting to postgreSQL
exec(open('connect2sql.py').read())
import pandas as pd
# Query the database and load directly into a DataFrame
a = pd.read_sql_query("select subjid, fidtc, SPLIT_PART(afidtc, '_', 1) as subjid1, aval as cosine from ru.cd where subjid = 'MSFT' and (aval < -0.9 or aval > 0.9)", conn)

b = pd.pivot_table(a, values= 'subjid', aggfunc='count', index= ['subjid1'], columns='fidtc')
b.reset_index(inplace=True)
b.to_csv('data/b.csv', index=False)

