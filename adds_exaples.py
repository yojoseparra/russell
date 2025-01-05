


# ---------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------ START of EXAPLES ---------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------------
# This was done before finishing the code hereup
# -----------------------------------------------------------------------------------------------------------
#---------------------------------------------- ------------- Euclidean -------------------------------------
# -----------------------------------------------------------------------------------------------------------
import pandas as pd

# Example DataFrame
df = pd.DataFrame({
    'ticker': ['ABC', 'ABC', 'ABC', 'XYZ', 'XYZ', 'XYZ', 'ABC', 'ABC', 'ABC', 'ABC', 'ABC', 'ABC'],
    'statements': ['Income Statement', 'Cash Flow Statement', 'Balance Sheet', 
                   'Income Statement', 'Cash Flow Statement', 'Balance Sheet', 
                   'Income Statement', 'Cash Flow Statement', 'Balance Sheet',
                   'Income Statement', 'Cash Flow Statement', 'Balance Sheet'],
    'parameter': ['totalRevenue', 'netIncomeFromContinuingOperations', 'totalDebt',
                  'totalRevenue', 'netIncomeFromContinuingOperations', 'totalDebt',
                  'totalRevenue', 'netIncomeFromContinuingOperations', 'totalDebt',
                  'totalRevenue', 'netIncomeFromContinuingOperations', 'totalDebt'],
    'value': [100, 20, 200, 110, 15, 250, 110, 30, 180, 120, 40, 160],
    'date': ['2021-01-01', '2021-01-01', '2021-01-01',
             '2021-01-01', '2021-01-01', '2021-01-01',
             '2022-01-01', '2022-01-01', '2022-01-01',
             '2023-01-01', '2023-01-01', '2023-01-01']
})

import pandas as pd
from scipy.spatial.distance import euclidean

# Filter data for each company
df_abc = df[df['ticker'] == 'ABC'].pivot(index='date', columns='parameter', values='value', fill_value=0)
df_xyz = df[df['ticker'] == 'XYZ'].pivot(index='date', columns='parameter', values='value', fill_value=0)

# Align both dataframes
df_combined = df_abc.join(df_xyz, lsuffix='_ABC', rsuffix='_XYZ', on='date', how='left')
df_combined=df_combined.dropna()
# Calculate Euclidean distance
distance = euclidean(df_combined.filter(like='_ABC').values.flatten(),
                     df_combined.filter(like='_XYZ').values.flatten())
print(f"Euclidean Distance: {distance}")


# -----------------------------------------------------------------------------------------------------------
#---------------------------------------------- ------------- Cosine similarity -----------------------------
# -----------------------------------------------------------------------------------------------------------
from sklearn.metrics.pairwise import cosine_similarity
# Example DataFrame
df = pd.DataFrame({
    'ticker': ['ABC', 'ABC', 'ABC', 'XYZ', 'XYZ', 'XYZ', 'ABC', 'ABC', 'ABC', 'ABC', 'ABC', 'ABC', 'XYZ', 'XYZ', 'XYZ'],
    'statements': ['Income Statement', 'Cash Flow Statement', 'Balance Sheet', 
                   'Income Statement', 'Cash Flow Statement', 'Balance Sheet', 
                   'Income Statement', 'Cash Flow Statement', 'Balance Sheet',
                   'Income Statement', 'Cash Flow Statement', 'Balance Sheet',
                   'Income Statement', 'Cash Flow Statement', 'Balance Sheet'],
    'parameter': ['totalRevenue', 'netIncomeFromContinuingOperations', 'totalDebt',
                  'totalRevenue', 'netIncomeFromContinuingOperations', 'totalDebt',
                  'totalRevenue', 'netIncomeFromContinuingOperations', 'totalDebt',
                  'totalRevenue', 'netIncomeFromContinuingOperations', 'totalDebt',
                  'totalRevenue', 'netIncomeFromContinuingOperations', 'totalDebt'],
    'value': [100, 20, 200, 110, 15, 250, 110, 30, 180, 120, 40, 160,180,10,360],
    'date': ['2021-01-01', '2021-01-01', '2021-01-01',
             '2021-01-01', '2021-01-01', '2021-01-01',
             '2022-01-01', '2022-01-01', '2022-01-01',
             '2023-01-01', '2023-01-01', '2023-01-01',
             '2022-01-01', '2022-01-01', '2022-01-01']
})

df = pd.DataFrame({
    'ticker': ['ABC', 'ABC', 'ABC','XYZ', 'XYZ', 'XYZ'],
    'statements': ['Income Statement', 'Cash Flow Statement', 'Balance Sheet', 
                   'Income Statement', 'Cash Flow Statement', 'Balance Sheet'],
    'parameter': ['totalRevenue', 'netIncomeFromContinuingOperations', 'totalDebt',
                  'totalRevenue', 'netIncomeFromContinuingOperations', 'totalDebt'],
    'value': [100, 20, 200, 110, 15, 250],
    'date': ['2021-01-01', '2021-01-01', '2021-01-01',
             '2021-01-01', '2021-01-01', '2021-01-01']
})
# Filter data for each company
df_abc = df[df['ticker'] == 'ABC'].pivot(index='date', columns='parameter', values='value')
df_xyz = df[df['ticker'] == 'XYZ'].pivot(index='date', columns='parameter', values='value')

# Align both dataframes
df_combined = df_abc.join(df_xyz, lsuffix='_ABC', rsuffix='_XYZ', on='date', how='left')
df_combined=df_combined.dropna()
# Reshape data to vectors the last reshape NOT NEEDED
vector_abc = df_combined.filter(like='_ABC').values.flatten().reshape(1, -1)
vector_xyz = df_combined.filter(like='_XYZ').values.flatten().reshape(1, -1)

# Compute cosine similarity
similarity = cosine_similarity(vector_abc, vector_xyz)[0, 0]
print(f"Cosine Similarity: {similarity}")
# Cosine Similarity: 0.9704187371506882
# Cosine Similarity: 0.9982098327983145


# -------------------------------------------------- another try more generalized 
# Example DataFrame
a = pd.DataFrame({
    'subjid': ['ABC', 'ABC', 'ABC', 'XYZ', 'XYZ', 'XYZ', 'ABC', 'ABC', 'ABC', 'ABC', 'ABC', 'ABC', 'XYZ', 'XYZ', 'XYZ'],
    'statements': ['Income Statement', 'Cash Flow Statement', 'Balance Sheet', 
                   'Income Statement', 'Cash Flow Statement', 'Balance Sheet', 
                   'Income Statement', 'Cash Flow Statement', 'Balance Sheet',
                   'Income Statement', 'Cash Flow Statement', 'Balance Sheet',
                   'Income Statement', 'Cash Flow Statement', 'Balance Sheet'],
    'text': ['totalRevenue', 'netIncomeFromContinuingOperations', 'totalDebt',
                  'totalRevenue', 'netIncomeFromContinuingOperations', 'totalDebt',
                  'totalRevenue', 'netIncomeFromContinuingOperations', 'totalDebt',
                  'totalRevenue', 'netIncomeFromContinuingOperations', 'totalDebt',
                  'totalRevenue', 'netIncomeFromContinuingOperations', 'totalDebt'],
    'fistresn': [100, 20, 200, 110, 15, 250, 110, 30, 180, 120, 40, 160,180,10,360],
    'fidtc': ['2021-01-01', '2021-01-01', '2021-01-01',
             '2021-01-01', '2021-01-01', '2021-01-01',
             '2022-01-01', '2022-01-01', '2022-01-01',
             '2023-01-01', '2023-01-01', '2023-01-01',
             '2022-01-01', '2022-01-01', '2022-01-01']
})


import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
tickerA='ABC'
tickerB='XYZ'
dt = '2022-01-01'
param = 'fistresn'

# Deleting rows with -1, 0, 1 or with missing values
bA = a[a['subjid'].isin([tickerA]) & (a['fidtc']== dt )][['fidtc','text', param]]
bA = bA[ (bA[param].isin([-1,0,1, np.nan]) == False) ]

bB = a[a['subjid'].isin([tickerB]) & (a['fidtc']== dt )][['fidtc', 'text', param]]
bB = bB[ (bB[param].isin([-1,0,1, np.nan]) == False) ]

# Step 1: Pivot data to create feature vectors for each (ticker, date)
b = bA.pivot_table(index=['fidtc'], columns=['text'], values=param)

# Repeating for C
c = bB.pivot_table(index=['fidtc'], columns=['text'], values=param)



# Step 2: Normalize the rows (optional but recommended for cosine similarity)
d = b.div((b ** 2).sum(axis=1) ** 0.5, axis=0)
d.reset_index()
e = c.div((c ** 2).sum(axis=1) ** 0.5, axis=0)
e.reset_index()

f = d.join(e, how='inner', on=['fidtc'], lsuffix='_A', rsuffix='_B')


# Reshape data to vectors the last reshape NOT NEEDED
va = f.filter(like='_A').values.flatten().reshape(1, -1)
vb = f.filter(like='_B').values.flatten().reshape(1, -1)

# Compute cosine similarity
# Step 3: Calculate cosine similarity for all rows
g = cosine_similarity(va, vb)[0, 0]


# ------------------------------------------------------- Trying to generalyze even more, for diferent subjid and for different dates
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Data
a = pd.DataFrame({
    'subjid': ['ABC', 'ABC', 'ABC', 'XYZ', 'XYZ', 'XYZ', 'ABC', 'ABC', 'ABC', 'ABC', 'ABC', 'ABC', 'XYZ', 'XYZ', 'XYZ'],
    'statements': ['Income Statement', 'Cash Flow Statement', 'Balance Sheet', 
                   'Income Statement', 'Cash Flow Statement', 'Balance Sheet', 
                   'Income Statement', 'Cash Flow Statement', 'Balance Sheet',
                   'Income Statement', 'Cash Flow Statement', 'Balance Sheet',
                   'Income Statement', 'Cash Flow Statement', 'Balance Sheet'],
    'text': ['totalRevenue', 'netIncomeFromContinuingOperations', 'totalDebt',
                  'totalRevenue', 'netIncomeFromContinuingOperations', 'totalDebt',
                  'totalRevenue', 'netIncomeFromContinuingOperations', 'totalDebt',
                  'totalRevenue', 'netIncomeFromContinuingOperations', 'totalDebt',
                  'totalRevenue', 'netIncomeFromContinuingOperations', 'totalDebt'],
    'fistresn': [100, 20, 200, 110, 15, 250, 110, 30, 180, 120, 40, 160, 180, 10, 360],
    'fidtc': ['2021-01-01', '2021-01-01', '2021-01-01',
             '2021-01-01', '2021-01-01', '2021-01-01',
             '2022-01-01', '2022-01-01', '2022-01-01',
             '2023-01-01', '2023-01-01', '2023-01-01',
             '2022-01-01', '2022-01-01', '2022-01-01']
})

# Parameters
tickers = a['subjid'].unique()  # Automatically handles multiple tickers
dates = a['fidtc'].unique()    # Automatically handles multiple dates
param = 'fistresn'

# Step 1: Prepare the data for cosine similarity computation
results = []
for dt in dates:
    for i, tickerA in enumerate(tickers):
        for tickerB in tickers[i+1:]:  # Compare each pair only once
            # Filter data for each ticker and date
            bA = a[(a['subjid'] == tickerA) & (a['fidtc'] == dt)][['fidtc', 'text', param]]
            bA = bA[~bA[param].isin([-1, 0, 1, np.nan])]
            bB = a[(a['subjid'] == tickerB) & (a['fidtc'] == dt)][['fidtc', 'text', param]]
            bB = bB[~bB[param].isin([-1, 0, 1, np.nan])]

            # Pivot data to create feature vectors
            if not bA.empty and not bB.empty:  # Ensure data exists for both tickers
                bA_pivot = bA.pivot_table(index=['fidtc'], columns='text', values=param)
                bB_pivot = bB.pivot_table(index=['fidtc'], columns='text', values=param)

                # Normalize rows for cosine similarity
                bA_normalized = bA_pivot.div((bA_pivot ** 2).sum(axis=1) ** 0.5, axis=0)
                bB_normalized = bB_pivot.div((bB_pivot ** 2).sum(axis=1) ** 0.5, axis=0)

                # Align columns and calculate cosine similarity
                common_columns = bA_normalized.columns.intersection(bB_normalized.columns)
                if not common_columns.empty:  # Ensure there's overlap in features
                    va = bA_normalized[common_columns].values.flatten().reshape(1, -1)
                    vb = bB_normalized[common_columns].values.flatten().reshape(1, -1)
                    similarity = cosine_similarity(va, vb)[0, 0]

                    # Append results
                    results.append({
                        'date': dt,
                        'tickerA': tickerA,
                        'tickerB': tickerB,
                        'cosine_similarity': similarity
                    })

# Step 2: Convert results to DataFrame for better visualization
results_df = pd.DataFrame(results)
print(results_df)

# --------------------------------------------------------------using only 2 tickers ----------------------------------------------


# connecting to postgreSQL
exec(open('connect2sql.py').read())
# Query the database and load directly into a DataFrame
a = pd.read_sql_query("SELECT * from ru.adfi", conn)
conn.close()

import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
tickerA='AAT'
tickerB='ZYXI'
dt = '2022-12-31'
param = 'fistresn'

# Deleting rows with -1, 0, 1 or with missing values
bA = a[a['subjid'].isin([tickerA]) & (a['fidtc']== dt )][['fidtc','text', param]]
bA = bA[ (bA[param].isin([-1,0,1, np.nan]) == False) ]

bB = a[a['subjid'].isin([tickerB]) & (a['fidtc']== dt )][['fidtc', 'text', param]]
bB = bB[ (bB[param].isin([-1,0,1, np.nan]) == False) ]

# Step 1: Pivot data to create feature vectors for each (ticker, date)
b = bA.pivot_table(index=['fidtc'], columns=['text'], values=param)

# Repeating for C
c = bB.pivot_table(index=['fidtc'], columns=['text'], values=param)



# Step 2: Normalize the rows (optional but recommended for cosine similarity)
d = b.div((b ** 2).sum(axis=1) ** 0.5, axis=0)
d.reset_index()
e = c.div((c ** 2).sum(axis=1) ** 0.5, axis=0)
e.reset_index()

f = d.join(e, how='inner', on=['fidtc'], lsuffix='_A', rsuffix='_B')


# Reshape data to vectors the last reshape NOT NEEDED
va = f.filter(like='_A').values.flatten().reshape(1, -1)
vb = f.filter(like='_B').values.flatten().reshape(1, -1)

# Compute cosine similarity
# Step 3: Calculate cosine similarity for all rows
g = cosine_similarity(va, vb)[0, 0]




# ---------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------ Normalizing and Calculating the Cosine Similarity ------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------------


import pandas as pd
import psycopg2
import sqlalchemy

import sys
print(sys.path)
sys.path.append('/microcap/src')

# connecting to postgreSQL
exec(open('connect2sql.py').read())

# Query the database and load directly into a DataFrame
a = pd.read_sql_query("SELECT a.*, text from (select * from ru.adfi where subjid in (select distinct subjid from ru.ds)) as a "
                      + "left join (select distinct sctest, text from ru.sc) as b on a.fitest = b.sctest ", conn)
conn.close()
# ----------------------------------------------------------- first attempt for pairs of tickers in different dates
# Parameters
tickers = a['subjid'].unique()  # Automatically handles multiple tickers
dates = a['fidtc'].unique()    # Automatically handles multiple dates
param = 'fistresn'

# Step 1: Prepare the data for cosine similarity computation
results = []
for dt in dates:
    for i, tickerA in enumerate(tickers):
        for tickerB in tickers[i+1:]:  # Compare each pair only once
            # Filter data for each ticker and date
            bA = a[(a['subjid'] == tickerA) & (a['fidtc'] == dt)][['fidtc', 'text', param]]
            bA = bA[~bA[param].isin([-1, 0, 1, np.nan])]
            bB = a[(a['subjid'] == tickerB) & (a['fidtc'] == dt)][['fidtc', 'text', param]]
            bB = bB[~bB[param].isin([-1, 0, 1, np.nan])]

            # Pivot data to create feature vectors
            if not bA.empty and not bB.empty:  # Ensure data exists for both tickers
                bA_pivot = bA.pivot_table(index=['fidtc'], columns='text', values=param)
                bB_pivot = bB.pivot_table(index=['fidtc'], columns='text', values=param)

                # Normalize rows for cosine similarity
                bA_normalized = bA_pivot.div((bA_pivot ** 2).sum(axis=1) ** 0.5, axis=0)
                bB_normalized = bB_pivot.div((bB_pivot ** 2).sum(axis=1) ** 0.5, axis=0)

                # Align columns and calculate cosine similarity
                common_columns = bA_normalized.columns.intersection(bB_normalized.columns)
                if not common_columns.empty:  # Ensure there's overlap in features
                    va = bA_normalized[common_columns].values.flatten().reshape(1, -1)
                    vb = bB_normalized[common_columns].values.flatten().reshape(1, -1)
                    similarity = cosine_similarity(va, vb)[0, 0]

                    # Append results
                    results.append({
                        'date': dt,
                        'tickerA': tickerA,
                        'tickerB': tickerB,
                        'cosine_similarity': similarity
                    })

# Step 2: Convert results to DataFrame for better visualization
results_df = pd.DataFrame(results)
results_df=results_df.sort_values(by=['tickerB', 'tickerA','date'])
print(results_df)

results_df.to_csv('data/selected.csv')

# >>> print(results_df)
#            date tickerA tickerB  cosine_similarity
# 854  2020-12-31    EVRI    DIOD           0.550589
# 683  2021-12-31    EVRI    DIOD           0.636344
# 512  2022-12-31    EVRI    DIOD           0.584272
# 341  2023-12-31    EVRI    DIOD           0.539144
# 170  2024-09-30    EVRI    DIOD           0.600473
# ..          ...     ...     ...                ...
# 684  2020-12-31    XPEL     UHG           0.832531
# 513  2021-12-31    XPEL     UHG           0.795026
# 342  2022-12-31    XPEL     UHG           0.835232
# 171  2023-12-31    XPEL     UHG           0.669476
# 0    2024-09-30    XPEL     UHG           0.835294

# ------------------------------------------------------------------ second attempt ------------------------------------
# ---------------------------- including cosing similarity for the same ticker but different years ----------------------

# Parameters
tickers = a['subjid'].unique()
dates = a['fidtc'].unique()
param = 'fistresn'

# Step 1: Prepare data for cosine similarity computation
results = []
for ticker in tickers:
    ticker_data = a[a['subjid'] == ticker]
    years = ticker_data['fidtc'].unique()
    
    # Compare different years for the same ticker
    for i, yearA in enumerate(years):
        for yearB in years[i+1:]:
            bA = ticker_data[ticker_data['fidtc'] == yearA][['fidtc', 'text', param]]
            bA = bA[~bA[param].isin([-1, 0, 1, np.nan])]
            bB = ticker_data[ticker_data['fidtc'] == yearB][['fidtc', 'text', param]]
            bB = bB[~bB[param].isin([-1, 0, 1, np.nan])]
            
            if not bA.empty and not bB.empty:
                bA_pivot = bA.pivot_table(index=['fidtc'], columns='text', values=param)
                bB_pivot = bB.pivot_table(index=['fidtc'], columns='text', values=param)
                
                # Normalize rows
                bA_normalized = bA_pivot.div((bA_pivot ** 2).sum(axis=1) ** 0.5, axis=0)
                bB_normalized = bB_pivot.div((bB_pivot ** 2).sum(axis=1) ** 0.5, axis=0)
                
                # Align columns and calculate cosine similarity
                common_columns = bA_normalized.columns.intersection(bB_normalized.columns)
                if not common_columns.empty:
                    va = bA_normalized[common_columns].values.flatten().reshape(1, -1)
                    vb = bB_normalized[common_columns].values.flatten().reshape(1, -1)
                    similarity = cosine_similarity(va, vb)[0, 0]
                    
                    # Append results
                    results.append({
                        'ticker': ticker,
                        'yearA': yearA,
                        'yearB': yearB,
                        'cosine_similarity': similarity
                    })

# Step 2: Convert results to DataFrame
results_df = pd.DataFrame(results)
print(results_df)


results_df.to_csv('data/selected.csv')

    # ticker       yearA       yearB  cosine_similarity
# 0     XPEL  2024-09-30  2023-12-31           0.996051
# 1     XPEL  2024-09-30  2022-12-31           0.990533
# 2     XPEL  2024-09-30  2021-12-31           0.961149
# 3     XPEL  2024-09-30  2020-12-31           0.975185
# 4     XPEL  2023-12-31  2022-12-31           0.993556
# ..     ...         ...         ...                ...
# 190   DIOD  2023-12-31  2021-12-31           0.962991
# 191   DIOD  2023-12-31  2020-12-31           0.909607
# 192   DIOD  2022-12-31  2021-12-31           0.989258
# 193   DIOD  2022-12-31  2020-12-31           0.944572
# 194   DIOD  2021-12-31  2020-12-31           0.969793



# ------------------------------------------------------------------ second attempt ------------------------------------
# ---------------------------- including cosing similarity for the same ticker but different years ----------------------



# Parameters
tickers = a['subjid'].unique()
dates = a['fidtc'].unique()
param = 'fistresn'

# Results
results_within = []  # Cosine similarities within each ticker
results_between = []  # Cosine similarities between tickers

# Step 1: Within-Ticker Similarities
for ticker in tickers:
    ticker_data = a[a['subjid'] == ticker]
    years = ticker_data['fidtc'].unique()
    
    # Compare different years for the same ticker
    for i, yearA in enumerate(years):
        for yearB in years[i+1:]:
            bA = ticker_data[ticker_data['fidtc'] == yearA][['fidtc', 'text', param]]
            bA = bA[~bA[param].isin([-1, 0, 1, np.nan])]
            bB = ticker_data[ticker_data['fidtc'] == yearB][['fidtc', 'text', param]]
            bB = bB[~bB[param].isin([-1, 0, 1, np.nan])]
            
            if not bA.empty and not bB.empty:
                bA_pivot = bA.pivot_table(index=['fidtc'], columns='text', values=param)
                bB_pivot = bB.pivot_table(index=['fidtc'], columns='text', values=param)
                
                # Normalize rows
                bA_normalized = bA_pivot.div((bA_pivot ** 2).sum(axis=1) ** 0.5, axis=0)
                bB_normalized = bB_pivot.div((bB_pivot ** 2).sum(axis=1) ** 0.5, axis=0)
                
                # Align columns and calculate cosine similarity
                common_columns = bA_normalized.columns.intersection(bB_normalized.columns)
                if not common_columns.empty:
                    va = bA_normalized[common_columns].values.flatten().reshape(1, -1)
                    vb = bB_normalized[common_columns].values.flatten().reshape(1, -1)
                    similarity = cosine_similarity(va, vb)[0, 0]
                    
                    # Append results
                    results_within.append({
                        'ticker': ticker,
                        'yearA': yearA,
                        'yearB': yearB,
                        'cosine_similarity': similarity
                    })

# Step 2: Between-Ticker Similarities
for date in dates:
    for i, tickerA in enumerate(tickers):
        for tickerB in tickers[i+1:]:
            bA = a[(a['subjid'] == tickerA) & (a['fidtc'] == date)][['fidtc', 'text', param]]
            bA = bA[~bA[param].isin([-1, 0, 1, np.nan])]
            bB = a[(a['subjid'] == tickerB) & (a['fidtc'] == date)][['fidtc', 'text', param]]
            bB = bB[~bB[param].isin([-1, 0, 1, np.nan])]
            
            if not bA.empty and not bB.empty:
                bA_pivot = bA.pivot_table(index=['fidtc'], columns='text', values=param)
                bB_pivot = bB.pivot_table(index=['fidtc'], columns='text', values=param)
                
                # Normalize rows
                bA_normalized = bA_pivot.div((bA_pivot ** 2).sum(axis=1) ** 0.5, axis=0)
                bB_normalized = bB_pivot.div((bB_pivot ** 2).sum(axis=1) ** 0.5, axis=0)
                
                # Align columns and calculate cosine similarity
                common_columns = bA_normalized.columns.intersection(bB_normalized.columns)
                if not common_columns.empty:
                    va = bA_normalized[common_columns].values.flatten().reshape(1, -1)
                    vb = bB_normalized[common_columns].values.flatten().reshape(1, -1)
                    similarity = cosine_similarity(va, vb)[0, 0]
                    
                    # Append results
                    results_between.append({
                        'tickerA': tickerA,
                        'tickerB': tickerB,
                        'date': date,
                        'cosine_similarity': similarity
                    })

# Convert results to DataFrames
results_within_df = pd.DataFrame(results_within)
results_between_df = pd.DataFrame(results_between)

# Output
print("Within-Ticker Cosine Similarities:")
print(results_within_df)
print("\nBetween-Ticker Cosine Similarities:")
print(results_between_df)

# ---------------------------------------------------------------------------


# Second Try ------------------------------------ 

def long2wide(tickers=[ 'DIOD', 'XPEL'], dataframe=a):
    # the following displays the ticker data wide accross years
    # This code works regardless the number of tickers
    b=dataframe.copy()
    c = b[['subjid', 'scgrpid','ficat', 'sctestcd', 'fidtc', 'fistres']].sort_values(by=['subjid', 'ficat','scgrpid', 'fidtc'])
    c = c.melt(id_vars=['subjid', 'scgrpid','ficat', 'sctestcd', 'fidtc'], value_vars= 'fistres' , var_name='param', value_name='aval')
    ca = b[['subjid', 'scgrpid','ficat', 'sctestcd', 'fidtc', 'chgn']].sort_values(by=['subjid',  'ficat','scgrpid', 'fidtc'])
    ca = ca.melt(id_vars=['subjid', 'scgrpid','ficat', 'sctestcd', 'fidtc'], value_vars= 'chgn' , var_name='param', value_name='aval')
    
    d = pd.concat([c, ca], ignore_index=True, axis=0)
    d=d.drop_duplicates()

    e = d.pivot(index=['subjid','ficat','scgrpid', 'sctestcd','param'], columns=['fidtc'], values='aval')
    e=e.reset_index()

    f = e.pivot(index=['subjid','ficat','scgrpid', 'sctestcd'], columns=['param'] )
    g=f.reset_index()


    h = g[g.subjid.isin(tickers)]
    return h
    #h.to_csv('data/h.csv')    
long2wide([ 'DIOD', 'XPEL'])

# First Try------------------------------------ Vertical assesment at a particular period

def long2wide(ticker='DIOD', dataframe=a):
    b=dataframe.copy()
    c = b[['subjid', 'scgrpid','ficat', 'sctestcd', 'fidtc', 'fistres']].sort_values(by=['subjid', 'ficat','scgrpid', 'fidtc'])
    c = c[c.subjid.isin([ticker])]
    c.reset_index(drop=True)

    c=c.drop_duplicates()
    d = c.pivot(index=['subjid','ficat','scgrpid', 'sctestcd'], columns=['fidtc'], values='fistres')
    d.reset_index(inplace=True)
    left = d

    # --------------- right
    c = b[['subjid', 'scgrpid','ficat', 'sctestcd', 'fidtc', 'chgn']].sort_values(by=['subjid',  'ficat','scgrpid', 'fidtc'])
    c = c[c.subjid.isin([ticker])]
    c.reset_index(drop=True)

    c=c.drop_duplicates()
    d = c.pivot(index=['subjid','ficat','scgrpid', 'sctestcd'], columns=['fidtc'], values='chgn')
    d.reset_index(inplace=True)

    #e.to_csv('data/rows.csv')

    right = d

    # The objective is to have a wide format data
    f = left.merge(right, how= 'left', on= ['subjid', 'ficat', 'scgrpid', 'sctestcd'], suffixes=['_VAL','_CHG'])

    import os
    os.system('cls')
    print(f.to_string())
long2wide()