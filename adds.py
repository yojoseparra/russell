
# This code calculate the cosine distance within different periods of a subjid (ticker) .
# This code calculate the cosine distance for subjects in the ds dataset. these are the most interesting tickers in the russell 2000 index for me on 2024

# -----------------------------------------------------------------------------------------------------------------------
# --------------------------------------------- COSINE DISTANCE CALCULATION ON DS ----------------------------------
# -----------------------------------------------------------------------------------------------------------------------



import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# connecting to postgreSQL
exec(open('connect2sql.py').read())
# Query the database and load directly into a DataFrame
a = pd.read_sql_query("SELECT a.*, text from (select * from ru.adfi where subjid in (select distinct subjid from ru.ds)) as a "
                      + "left join (select distinct sctest, text from ru.sc) as b on a.fitest = b.sctest ", conn)
conn.close()


# ------------------------ defining a function that will calculate cosine_similarity



def selfcos(ticker='', param='fistresn', dataframe=a):
    # By default takes a dataframe called 'a'
    # selfcos(ticker='TH')
    # subset
    # Deleting rows with -1, 0, 1 or with missing values
    bA = a[a['subjid']== ticker ][['fidtc','text', param]]
    bA = bA[ (bA[param].isin([-1,0,1, np.nan]) == False) ]

    # Step 1: Pivot data to create feature vectors for each (ticker, date)
    b = bA.pivot_table(index=['fidtc'], columns=['text'], values=param)

    # Step 2: Normalize the rows (optional but recommended for cosine similarity)
    d = b.div((b ** 2).sum(axis=1) ** 0.5, axis=0)
    d.fillna(0, inplace=True)

    # Calculate cosine similarities between columns
    similarity_matrix = cosine_similarity(d)

    # Convert similarity matrix to a DataFrame
    s = pd.DataFrame(similarity_matrix, index=d.index,  columns=d.index)
    s.reset_index(inplace=True)
    return s

# Parameters
tickers = a['subjid'].unique()
parameters = ['fistresn', 'chg' ]

# Generate column names using numbers from 0 to size of dates var
#totalCols = len(a['fidtc'].unique())
#column_names = [f"Column_{i}" for i in range(totalCols)]
# Results
#results = pd.DataFrame(columns=column_names) # Cosine similarities within each ticker

# List to hold DataFrames
results = []
results = pd.DataFrame(results)



# An additional for is avoided as it makes the code obscure, so WE RUN THIS FOLLOWING CODE TWICE as we have two parameters
param= parameters[1]
# Step 1: Within-Ticker Similarities
for ticker in tickers:
    ticker_data = a[a['subjid'] == ticker]
    result = selfcos(ticker=ticker, param=param, dataframe=ticker_data)
    result['subjid']=ticker
    result['param'] = param.upper()
    result['dtype'] = 'DERIVED NORMALIZED COSINE DISTANCE WITHIN SUBJECT'
    z = pd.melt(result, id_vars=[ 'dtype','param','subjid','fidtc'], var_name='afidtc',value_name='aval')
    z= z.drop_duplicates(z)
    z = z[z.fidtc != z.afidtc ]
    # this if is not needed, but i wont take it out
    if ticker == tickers[0]: 
        results=pd.concat([results,z], ignore_index=True, names=None)

        colNames = z.columns
        print(z.head())
        print(type(results))
    elif ticker != tickers[0]:
        y = z.loc[:, colNames]

    # Append the row using pd.concat()
    # Drop columns not in the first DataFrame
        results=pd.concat([results, y], ignore_index=True, names=None) 


results.to_csv('data/results1.csv')
