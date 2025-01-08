#1.0 -- Adding a new variable to the data called fistresn, which is the fiorres / total revenue This is my form of standardize the data 
#2.0 -- additionally the objective is to regisger the increase of fistresn accross years 'chg'
#3.0 -- A new dataset is created in the SQL posgtres called 'cd' or Cosine Distance

# -------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------ creating the variable fistresn -----------------------------------------
#1.0 -- Adding a new variable to the data called fistresn, which is the fiorres / total revenue This is my form of standardize the data 
# -------------------------------------------------------------------------------------------------------------------------------------

# connecting to postgreSQL
exec(open('connect2sql.py').read())

# Query the database and load directly into a DataFrame
a = pd.read_sql_query("SELECT * from ru.mo ", conn)
print(a)
conn.close()
df=a.copy()


# Step 1: Find the 'totalRevenue' for each combination of ticker and date
revenue_dict = df[df['fitest'] == 'TotalRevenue'].groupby(['subjid', 'fidtc'])['fiorres'].first().to_dict()

# Step 2: Define the function to apply
def divide_by_revenue(row):
    # Retrieve the totalRevenue for the current ticker and date
    total_revenue = revenue_dict.get((row['subjid'], row['fidtc']), None)

    # Check if totalRevenue is valid (not None and not zero)
    if total_revenue is None or total_revenue == 0:
        return float('nan')  # Return NaN for missing or zero totalRevenue
    else:
        return row['fiorres'] / total_revenue  # Perform the division safely

# Step 3: Apply the function to each row and create the 'value_new' column
df['fistresn'] = df.apply(divide_by_revenue, axis=1)

z1 = df.copy()


z =  df[['subjid', 'ficat', 'fitest', 'fidtc', 'fiperiod', 'fiorres']]


#------------------------------------------------------------------- creating a variable chg and pchg ---------------------------------
#2.0 -- additionally the objective is to regisger the increase of fistresn accross years ----------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------

df =  z[['subjid', 'ficat', 'fitest', 'fidtc', 'fiperiod', 'fiorres']]

# Ensure 'date' is a datetime object
df['fidtc'] = pd.to_datetime(df['fidtc'], format="%Y-%m-%d").dt.date


# Pivot to restructure data
pivot_df = df.pivot(index=['subjid', 'ficat', 'fitest', 'fiperiod'], columns='fidtc', values='fiorres')
#pivot_df.to_csv('data/pivot_df.csv')
# Extract year-end dates and handle the most recent column
# using list comprehension
# [expression for item in iterable if condition]

b = [col for col in pivot_df.columns if col.month == 3]
c = [col for col in pivot_df.columns if col.month == 6]
d = [col for col in pivot_df.columns if col.month == 9]
e = [col for col in pivot_df.columns if col.month == 12]




# Sort the dates to ensure chronological order
#year_end_dates = sorted(year_end_dates)

# Calculate changes for selected dates
change_columns = []

for i in range(len(b) - 1 ):
    col_1 = b[i]
    col_2 = b[i + 1]
    change_col = f"{col_2}_{col_1}_chg"
    pivot_df[change_col] = (pivot_df[col_2] - pivot_df[col_1]) / pivot_df[col_1]
    change_columns.append(change_col)

for i in range(len(c) - 1 ):
    col_1 = c[i]
    col_2 = c[i + 1]
    change_col = f"{col_2}_{col_1}_chg"
    pivot_df[change_col] =  (pivot_df[col_2] - pivot_df[col_1]) / pivot_df[col_1]
    change_columns.append(change_col)

for i in range(len(d) - 1 ):
    col_1 = d[i]
    col_2 = d[i + 1]
    change_col = f"{col_2}_{col_1}_chg"
    pivot_df[change_col] =  (pivot_df[col_2] - pivot_df[col_1]) / pivot_df[col_1]
    change_columns.append(change_col)

for i in range(len(e) - 1 ):
    col_1 = e[i]
    col_2 = e[i + 1]
    change_col = f"{col_2}_{col_1}_chg"
    pivot_df[change_col] =  (pivot_df[col_2] - pivot_df[col_1]) / pivot_df[col_1]
    change_columns.append(change_col)


#pivot_df.to_csv('data/pivot_df.csv')
# Reset index to flatten the DataFrame
result_df = pivot_df.reset_index()


# Select only the 'change' columns along with identifiers
change_columns = [col for col in result_df.columns if "_chg" in str(col)]
subset_df = result_df[['subjid', 'ficat', 'fitest', 'fiperiod'] + change_columns]
#subset_df.to_csv('data/subset_df.csv')

# Rename the change columns to remove "change_"
rename_mapping = {col: col.replace("_chg", "") for col in change_columns}
subset_df = subset_df.rename(columns=rename_mapping)

# Melting

y= subset_df.melt(id_vars=['subjid', 'ficat','fitest', 'fiperiod'], var_name='afidtc', value_name='chg')
x=y.dropna()

# separate one column into 2columns
# Split the column into two new columns
x[['fidtc', 'fidtc0']] = x['afidtc'].str.split('_', expand=True)
x['fidtc'] = pd.to_datetime(x['fidtc'], format="%Y-%m-%d")
import pandas as pd
w=z.dropna()
v = pd.merge(w,x,on=['subjid', 'ficat', 'fitest','fidtc', 'fiperiod'], how='left')
v = v.drop("fidtc0", axis='columns')
# Ensure 'date' is a datetime object


v.sort_values(by=['subjid', 'ficat','fitest'])
#v.to_csv('data/v.csv')
# adding all the info toguether

t = pd.merge(z1,v,on=['subjid', 'ficat', 'fitest','fidtc', 'fiperiod', 'fiorres'], how='left')


#3.0 -- A new dataset is created in the SQL posgtres called 'cd' or Cosine Distance
# -------------------------------------- creating the adfi dataset: Analysis DAtaset for FInancials
from sqlalchemy import create_engine
from urllib.parse import quote_plus

# connecting to postgreSQL
exec(open('connect2sql.py').read())
# Escape the password
escaped_password = quote_plus(password)

# Connection string
connection_string = f'postgresql+psycopg2://{username}:{escaped_password}@{host}/{database}'
engine = create_engine(connection_string)

# Insert the DataFrame into the SQL table
t.to_sql('admo', con=engine, if_exists='replace', index=False, schema='ru')

#        domain             ficat     subjid                                    fitest       fiorres fiorresu      fidtc fiperiod  fistresn                 afidtc       chg
# 0          MO  INCOME STATEMENT  035420.KS                              Amortization  1.317349e+10      KRW 2020-12-31      12M  0.002484                    NaN       NaN
# 1          MO  INCOME STATEMENT  035420.KS                              Amortization  2.118140e+10      KRW 2021-12-31      12M  0.003107  2021-12-31_2020-12-31  0.607880
# 2          MO  INCOME STATEMENT  035420.KS                              Amortization  4.227506e+10      KRW 2022-12-31      12M  0.005143  2022-12-31_2021-12-31  0.995858
# 3          MO  INCOME STATEMENT  035420.KS                              Amortization  5.432705e+10      KRW 2023-12-31      12M  0.005618  2023-12-31_2022-12-31  0.285085
# 4          MO  INCOME STATEMENT    0NWV.IL                              Amortization  2.070000e+08      EUR 2020-12-31      12M  0.008228                    NaN       NaN
# ...       ...               ...        ...                                       ...           ...      ...        ...      ...       ...                    ...       ...
# 136033     MO        CASH FLOWS        WAT  UnrealizedGainLossOnInvestmentSecurities  0.000000e+00      USD 2022-12-31      12M  0.000000  2022-12-31_2021-12-31 -1.000000
# 136034     MO        CASH FLOWS        WAT  UnrealizedGainLossOnInvestmentSecurities  0.000000e+00      USD 2023-12-31      12M  0.000000                    NaN       NaN
# 136035     MO        CASH FLOWS        WEX  UnrealizedGainLossOnInvestmentSecurities  4.804200e+07      USD 2020-12-31      12M  0.030799                    NaN       NaN
# 136036     MO        CASH FLOWS        WMT  UnrealizedGainLossOnInvestmentSecurities -1.886000e+09      USD 2020-01-31      12M       NaN                    NaN       NaN
# 136037     MO        CASH FLOWS        WMT  UnrealizedGainLossOnInvestmentSecurities -8.589000e+09      USD 2021-01-31      12M -0.015361                    NaN       NaN




u = t[ [ 'ficat','fitest']]
u = u.drop_duplicates()
u.to_csv('data/ordering_fitest.csv', index=False)


# This code calculate the cosine distance within different periods of a subjid (ticker) and between 2 different subjid tickers.
# only a subset was taken the ones in DS.

# -----------------------------------------------------------------------------------------------------------------------
# --------------------------------------------- COSINE DISTANCE CALCULATION ON ADMO    ----------------------------------
# -----------------------------------------------------------------------------------------------------------------------
# -------------------------------------- creating the cd dataset: Analysis DAtaset for FInancials
import pandas as pd
import psycopg2
import sqlalchemy
import sys
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
# ------------------------ defining a function that will calculate cosine_similarity

def cosindis(tickers=('XPEL', 'SHLS'), param= 'chg', dataframe=a):
    # Usage: cosindis(['DIOD','XPEL'], param = 'fistresn') # By default takes a dataframe called 'a'
    # Pending improvements: check columns in the pivot with scarse data and delete them

    baa = a[a['subjid'].isin(tickers) ][['subjid','fidtc','text', param]]

    # There are tickers without a single value for the chg variable. in this case we skip to the next iteration
    baa = baa[ (baa[param].isin([-1,0,1, np.nan]) == False) ]
    # Step 1: Pivot data to create feature vectors for each (ticker, date)
    b = baa.pivot_table(index=['subjid','fidtc'], columns=['text'], values=param)
    # Step 2: Normalize the rows (optional but recommended for cosine similarity)

    #filterng on each ticker. the idea is to normalize them individually.
    tickera= b.index.get_level_values(0).unique()[0]
    tickerb= b.index.get_level_values(0).unique()[1]


    ba = a[a['subjid'].isin(tickers) ][['subjid','fidtc','text', param]]

    # There are tickers without a single value for the chg variable. in this case we skip to the next iteration
    ba = b.loc[tickera]
    bb = b.loc[tickerb]

    da = ba.div((ba ** 2).sum(axis=1) ** 0.5, axis=0)
    da.fillna(0, inplace=True) 
    db = bb.div((bb ** 2).sum(axis=1) ** 0.5, axis=0)
    db.fillna(0, inplace=True)

    d = pd.concat([da,db])
    #d=pd.concat([da,db], ignore_index=True, names=None)

    # Calculate cosine similarities between columns
    s = cosine_similarity(d)
    d.reset_index(inplace=True)


    # Generate column names using numbers from 0 to size of dates var
    
    col = [f"{tickera}_{i}" for i in ba.index]
    colb = [f"{tickerb}_{i}" for i in bb.index]
    col.extend(colb)

    s = pd.DataFrame(s , columns=col)
    s['subjid'] =  b.index.get_level_values(0)
    s['param'] = param.upper()
    s['fidtc'] = d['fidtc']
    s['dtype'] = 'DERIVED: NORMALIZED COSINE DISTANCE BETWEEN SUBJECTS'
    s.sort_values(['subjid','fidtc'])       
    return s

# ------------------------------------------------------------------------------------------------------------------------
# importing data
# ------------------------------------------------------------------------------------------------------------------------

# connecting to postgreSQL
exec(open('connect2sql.py').read())

# Query the database and load directly into a DataFrame
a = pd.read_sql_query("SELECT a.*, sctest, sctestcd,text from ru.admo as a "
                      + "left join (select distinct scgrp,sctest, sctest0, sctestcd, text from ru.sc) as b "
                      + "on a.ficat=b.scgrp  and a.fitest = b.sctest0", conn)
conn.close()

# ------------------------------------------------------------------------------------------------------------------------
# creting pairs of tickers
# ------------------------------------------------------------------------------------------------------------------------

# The objective is to create a list with all possible parwise combinations of subjis to calculate the cosine distances
from itertools import combinations
# List of items
subjid = a['subjid'].unique()

# Generate all combinations of the items (length 2)
pairs = list(combinations(subjid, 2))
processing = [ round((i + 1) / len(pairs) * 100) for i in range(len(pairs))]
# Convert to strings with a percentage sign
percentages = [f"{p}%" for p in processing]
processing = dict(zip(pairs, percentages))

# ------------------------------------------------------------------------------------------------------------------------
# Start Looping
# ------------------------------------------------------------------------------------------------------------------------

parameters = ['fistresn']
param = parameters[0]

results = []
results = pd.DataFrame(results)

for tickers in pairs:
    print('-- FROM LOOP --')
    print(processing[tickers] + '-- Copletion -- ( ' + tickers[0] + ', ' + tickers[1] + ' )  PARAMETER:  ' + param.upper() )
    i = i+ 1
    print(i)
    # There are tickers without a single value for the chg variable. in this case we skip to the next iteration
    testinga= a[a['subjid']== tickers[0] ]
    testingb= a[a['subjid']== tickers[1] ]

    # invoking the cosindis to calculate the cosine_distance
    z = cosindis(tickers,param= parameters[0])
    y = pd.melt(z, id_vars=[ 'dtype','param','subjid','fidtc'], var_name='afidtc',value_name='aval')
    results=pd.concat([results,y], ignore_index=True, names=None)
    # results= results.drop_duplicates(results)

copy_results = results.copy()

results= results.drop_duplicates()
results = results.sort_values(['subjid','fidtc', 'param' ])
results.to_csv('data/results.csv')

# -------------------------------------- creating the... dataset: Analysis DAtaset for FInancials
#	dtype	param	subjid	fidtc	afidtc	aval

from sqlalchemy import create_engine
from urllib.parse import quote_plus


# connecting to postgreSQL
exec(open('connect2sql.py').read())
# Connection string
connection_string = f'postgresql+psycopg2://{username}:{escaped_password}@{host}/{database}'
engine = create_engine(connection_string)


# Insert the DataFrame into the SQL table this is the cd or cosine distance
# adcd_1 represents cosine distances within subjids or tickers for different periods.
results.to_sql('cd', con=engine, if_exists='replace', index=False, schema='ru')


#                                                    dtype     param     subjid      fidtc                         afidtc      aval
# 16373  DERIVED: NORMALIZED COSINE DISTANCE BETWEEN SU...  FISTRESN  035420.KS 2020-12-31  035420.KS_2020-12-31 00:00:00  1.000000
# 16383  DERIVED: NORMALIZED COSINE DISTANCE BETWEEN SU...  FISTRESN  035420.KS 2020-12-31  035420.KS_2021-12-31 00:00:00  0.761687
# 16393  DERIVED: NORMALIZED COSINE DISTANCE BETWEEN SU...  FISTRESN  035420.KS 2020-12-31  035420.KS_2022-12-31 00:00:00  0.842005
# 16403  DERIVED: NORMALIZED COSINE DISTANCE BETWEEN SU...  FISTRESN  035420.KS 2020-12-31  035420.KS_2023-12-31 00:00:00  0.848167
# 16413  DERIVED: NORMALIZED COSINE DISTANCE BETWEEN SU...  FISTRESN  035420.KS 2020-12-31  035420.KS_2024-09-30 00:00:00  0.136894
# ...                                                  ...       ...        ...        ...                            ...       ...
# 16382  DERIVED: NORMALIZED COSINE DISTANCE BETWEEN SU...  FISTRESN        ZTS 2024-09-30  035420.KS_2020-12-31 00:00:00  0.181772
# 16392  DERIVED: NORMALIZED COSINE DISTANCE BETWEEN SU...  FISTRESN        ZTS 2024-09-30  035420.KS_2021-12-31 00:00:00  0.197766
# 16402  DERIVED: NORMALIZED COSINE DISTANCE BETWEEN SU...  FISTRESN        ZTS 2024-09-30  035420.KS_2022-12-31 00:00:00  0.091012
# 16412  DERIVED: NORMALIZED COSINE DISTANCE BETWEEN SU...  FISTRESN        ZTS 2024-09-30  035420.KS_2023-12-31 00:00:00  0.110438
# 16422  DERIVED: NORMALIZED COSINE DISTANCE BETWEEN SU...  FISTRESN        ZTS 2024-09-30  035420.KS_2024-09-30 00:00:00  0.562255
