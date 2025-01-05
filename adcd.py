# This code calculate the cosine distance within different periods of a subjid (ticker) and between 2 different subjid tickers.
# only a subset was taken the ones in DS.

# -----------------------------------------------------------------------------------------------------------------------
# --------------------------------------------- COSINE DISTANCE CALCULATION ON DS    ----------------------------------
# -----------------------------------------------------------------------------------------------------------------------

import pandas as pd
import psycopg2
import sqlalchemy
import sys
print(sys.path)
sys.path.append('/microcap/src')
import pandas as pd
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

# Database connection
conn = psycopg2.connect( dbname="russell",user="jose",password="letme2G@tin",host="localhost",port="5432")
# Query the database and load directly into a DataFrame
a = pd.read_sql_query("SELECT a.*, text from (select * from ru.adfi where subjid in  (select distinct subjid from ru.ds) )  as a "
                      + "left join (select distinct scgrp,sctest, text from ru.sc) as b on a.fitest = b.sctest  and a.ficat=b.scgrp", conn)
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

parameters = ['chg',  'fistresn']
total = []
total = pd.DataFrame(results)

for param in parameters:
    results = []
    results = pd.DataFrame(results)
    i=0
    for tickers in pairs:
        print('-- FROM LOOP --')
        print(processing[tickers] + '-- Copletion -- ( ' + tickers[0] + ', ' + tickers[1] + ' )  PARAMETER:  ' + param.upper() )
        i = i+ 1
        print(i)
        # There are tickers without a single value for the chg variable. in this case we skip to the next iteration
        testinga= a[a['subjid']== tickers[0] ]
        testingb= a[a['subjid']== tickers[1] ]
        if (param=='chg'):
            testinga= a[a['subjid']== tickers[0] ]
            testingb= a[a['subjid']== tickers[1] ]
            chga = testinga.isna().all()
            chgb = testingb.isna().all()
            if ( (chga['chg'] == True) | (chgb['chg'] == True) ):
                continue
        # invoking the cosindis to calculate the cosine_distance
        z = cosindis(tickers,param= param)
        y = pd.melt(z, id_vars=[ 'dtype','param','subjid','fidtc'], var_name='afidtc',value_name='aval')
        results=pd.concat([results,y], ignore_index=True, names=None)
        # results= results.drop_duplicates(results)
    total =pd.concat([total,results], ignore_index=True, names=None) 

total= total.drop_duplicates(results)
total=total.sort_values(['subjid','fidtc', 'param' ])
#total.to_csv('data/total.csv')

# -------------------------------------- creating the adfi dataset: Analysis DAtaset for FInancials
from sqlalchemy import create_engine
from urllib.parse import quote_plus

username = ''
password = ''
host = ''
database = ''

# Escape the password
escaped_password = quote_plus(password)

# Connection string
connection_string = f'postgresql+psycopg2://{username}:{escaped_password}@{host}/{database}'
engine = create_engine(connection_string)


# Insert the DataFrame into the SQL table this is the cd or cosine distance
# adcd_1 represents cosine distances within subjids or tickers for different periods.
total.to_sql('adcd', con=engine, if_exists='replace', index=False, schema='ru')



