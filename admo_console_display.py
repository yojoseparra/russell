# Warren Buffet to select companies based on book 'The Guru Investor' By John P. Reese

# --------------------------------------------------------------------------------------------------------
# --------------------------------------------- CHG FISTRESN ---------------------------------------------
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

def long2wide_fistresn_wide(tickers=[ 'AMZN', 'BABA'], dataframe=a):
    pd.options.mode.chained_assignment = None  # Turn off the warning
    # the following displays the ticker data wide accross years
    # This code works with 2 tickers
    b=dataframe[dataframe.subjid.isin(tickers)].copy()
    c = b[['subjid', 'scgrpid','ficat', 'sctestcd', 'fidtc', 'fistresn', 'fiperiod']].sort_values(by=['subjid', 'ficat','scgrpid', 'fidtc'])
    c = c.melt(id_vars=['subjid', 'scgrpid','ficat', 'sctestcd', 'fiperiod', 'fidtc'], value_vars= 'fistresn' , var_name='param', value_name='aval')
    # Theere are duplicates
    #duplicates = c[c.duplicated(subset=['subjid', 'ficat', 'scgrpid', 'sctestcd', 'fiperiod', 'fidtc', 'param'], keep=False)]
    #print(duplicates)

    c = c.pivot(index=['subjid','ficat','scgrpid', 'sctestcd', 'fiperiod'], columns=[ 'fidtc', 'param'], values='aval') 
    ca = b[['subjid', 'scgrpid','ficat', 'sctestcd', 'fidtc', 'fiperiod', 'chg']].sort_values(by=['subjid',  'ficat','scgrpid', 'fidtc'])
    ca = ca.melt(id_vars=['subjid', 'scgrpid','ficat', 'sctestcd', 'fiperiod', 'fidtc'], value_vars= 'chg' , var_name='param', value_name='aval')
    ca = ca.pivot(index=['subjid','ficat','scgrpid', 'sctestcd', 'fiperiod'], columns=[ 'fidtc', 'param'], values='aval') 
    d = c.merge(ca, on=['subjid','ficat','scgrpid', 'sctestcd', 'fiperiod'], how='left')
    d.reset_index(inplace=True)

    # There are many columns with scarce data, these columns must leave
    # Define a threshold for minimum non-null values (e.g., 50%)
    threshold = 0.1 * len(d)
    # Drop columns with scarce data
    d = d.dropna(axis=1, thresh=threshold)

    # Modify the MultiIndex to remove the time part from the 'fidtc' level like 2022-12-31
    d.columns = pd.MultiIndex.from_tuples(
        [(str(item[0]).split(' ')[0] if isinstance(item[0], pd.Timestamp) else item[0], item[1]) 
        for item in d.columns],
        names=d.columns.names
    )
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

import numpy as np
for tickers in pairs:
    pd.options.mode.chained_assignment = None  # Turn off the warning
    print(tickers)
    print(processing[tickers])
    e = long2wide_fistresn_wide(tickers=tickers)
    #tickers = pairs[2]
    # ------------------------------------------------- Presenting data in console as percentages ----------------------------
    # ------------------------------------------------------------------------------------------------------------------------
    # Transform all numeric columns to percentages
    numeric_cols = e.select_dtypes(include='number').columns
    e[numeric_cols] = e[numeric_cols] * 100
    # Optional: Format as strings with '%' sign
    #e[numeric_cols] = e[numeric_cols].applymap(lambda x: f"{x:.0f}%")
    e[numeric_cols] = e[numeric_cols].applymap(lambda x: f"{x:.0f}%" if not pd.isna(x) else np.nan)
    e.to_csv( 'data/'+tickers[0] + '_' + tickers[1] +'.csv', index=False )


# ------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------- Presenting the profile of the company --------------------------------
dir = 'data/' + '_'.join(tickers) + '.csv'
#e.to_csv(dir)
querying = f"SELECT *  from ru.pr where subjid in ('{tickers[1]}')"
pr = pd.read_sql_query( querying, conn)
print(pr.to_string())

querying1 = f"SELECT *  from ru.pr where subjid in ('{tickers[0]}')"
pr1 = pd.read_sql_query( querying1, conn)
print(pr1.to_string())


#conn.close()

# fidtc subjid_x             ficat scgrpid                                          sctestcd fiperiod_x_x 2021-09-30 2022-09-30 2023-09-30 2024-09-30_x_x 2022-09-30 2023-09-30  ... fiperiod_x_y 2024-09-30_x_y 2024-06-30 2021-06-30 2022-06-30 2023-06-30 2024-06-30 2022-06-30 2023-06-30 fiperiod_y_y 2024-09-30_y_y
# 0         AAPL     BALANCE SHEET       1                         Cash And Cash Equivalents          12M   0.095512   0.059965   0.078179       0.076574  -0.323240   0.267233  ...          12M            NaN   0.074718   0.084622   0.070263   0.163764  -0.472251  -0.020599   1.491135          NaN            NaN
# 1         AAPL     BALANCE SHEET       2                                  Cash Equivalents          12M   0.048207   0.012933   0.004190       0.007017  -0.710802  -0.685098  ...          12M            NaN   0.027513   0.041359   0.028612   0.123757  -0.742851  -0.183976   3.622951          NaN            NaN
# 2         AAPL     BALANCE SHEET       3                                    Cash Financial          12M   0.047305   0.047032   0.073989       0.069556   0.071713   0.529117  ...          12M            NaN   0.047205   0.043263   0.041650   0.040007   0.364827   0.135589   0.026641          NaN            NaN
# 3         AAPL     BALANCE SHEET       4  Cash Cash Equivalents And Short Term Investments          12M   0.171230   0.122497   0.160599       0.166663  -0.228851   0.274325  ...          12M            NaN   0.308136   0.774927   0.528315   0.525003  -0.321106  -0.195822   0.062120          NaN            NaN
# 4         AAPL     BALANCE SHEET       5                                  Commercial Paper          12M   0.016402   0.025314   0.015615       0.025489   0.663667  -0.400421  ...          NaN            NaN        NaN        NaN        NaN        NaN        NaN        NaN        NaN          NaN            NaN
# ..         ...               ...     ...                                               ...          ...        ...        ...        ...            ...        ...        ...  ...          ...            ...        ...        ...        ...        ...        ...        ...        ...          ...            ...
# 188        NaN  INCOME STATEMENT      70                            Special Income Charges          NaN        NaN        NaN        NaN            NaN        NaN        NaN  ...          12M            NaN  -0.000840  -0.000077  -0.000509  -0.000142   5.866667   6.769231  -0.702970          TTM      -0.000814
# 189        NaN  INCOME STATEMENT      72                                         Write Off          NaN        NaN        NaN        NaN            NaN        NaN        NaN  ...          12M            NaN   0.000840   0.000077   0.000509   0.000142   5.866667   6.769231  -0.702970          TTM       0.000814
# 190        NaN  INCOME STATEMENT      75                               Total Unusual Items          NaN        NaN        NaN        NaN            NaN        NaN        NaN  ...          12M            NaN  -0.002240   0.007752   0.001685  -0.000071  35.600000  -0.743668  -1.044910          TTM      -0.000523
# 191        NaN  INCOME STATEMENT      76            Total Unusual Items Excluding Goodwill          NaN        NaN        NaN        NaN            NaN        NaN        NaN  ...          12M            NaN  -0.002240   0.007752   0.001685  -0.000071  35.600000  -0.743668  -1.044910          TTM      -0.000523
# 192        NaN  INCOME STATEMENT      78                                      Other Gand A          NaN        NaN        NaN        NaN            NaN        NaN        NaN  ...          12M            NaN   0.031042   0.030383   0.029757   0.035745   0.004488   0.155277   0.283898          TTM       0.030717


