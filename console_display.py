# Warren Buffet to select companies based on book 'The Guru Investor' By John P. Reese

# --------------------------------------------------------------------------------------------------------
# --------------------------------------------- CHG FISTRESN ---------------------------------------------
# --------------------------------------------------------------------------------------------------------

# connecting to postgreSQL

exec(open('connect2sql.py').read())
# Query the database and load directly into a DataFrame
a = pd.read_sql_query("SELECT *  from ru.console_display", conn)
print(a)
conn.close()

b=a.copy()
# Third Try ------------------------------------ 
# the following displays the ticker data wide accross years
def long2wide(tickers=[ 'DIOD', 'XPEL'], dataframe=a):
    # the following displays the ticker data wide accross years
    # This code works with 2 tickers
    b=dataframe.copy()
    c = b[['subjid', 'scgrpid','ficat', 'sctestcd', 'fidtc', 'fistres']].sort_values(by=['subjid', 'ficat','scgrpid', 'fidtc'])
    c = c.melt(id_vars=['subjid', 'scgrpid','ficat', 'sctestcd', 'fidtc'], value_vars= 'fistres' , var_name='param', value_name='aval')


    ca = b[['subjid', 'scgrpid','ficat', 'sctestcd', 'fidtc', 'chgn']].sort_values(by=['subjid',  'ficat','scgrpid', 'fidtc'])
    ca = ca.melt(id_vars=['subjid', 'scgrpid','ficat', 'sctestcd', 'fidtc'], value_vars= 'chgn' , var_name='param', value_name='aval')
    
    d = pd.concat([c, ca], ignore_index=True, axis=0)
    d=d.drop_duplicates()

    d = d[d.subjid.isin(tickers) ].sort_values(by=[ 'fidtc' ,'ficat','scgrpid'])
 
    e = d.pivot(index=['ficat','scgrpid', 'sctestcd'], columns=['fidtc', 'param', 'subjid'], values='aval')
    return e


import os
os.system('cls')
i=long2wide([ 'DIOD', 'XPEL'])

print(i.to_string( ) )

#i.to_csv('data/i.csv')

# fidtc                                                                     2020-12-31                 2021-12-31                   2022-12-31                  2023-12-31                  2024-09-30
# param                                                                        fistres       chgn         fistres       chgn           fistres       chgn          fistres       chgn          fistres      chgn
# subjid                                                                          DIOD  XPEL DIOD XPEL       DIOD XPEL  DIOD   XPEL       DIOD XPEL  DIOD  XPEL       DIOD XPEL  DIOD  XPEL       DIOD XPEL DIOD XPEL
# ficat            scgrpid sctestcd
# BALANCE SHEET    1.0     cash And Cash Equivalents                              22.0  18.0  NaN  NaN       20.0  4.0 -1.67 -14.55       17.0  2.0 -3.31 -1.23       19.0  3.0  2.15  0.44        NaN  NaN  NaN  NaN
#                  2.0     cash Cash Equivalents And Short Term Investments       22.0  18.0  NaN  NaN       21.0  4.0 -1.80 -14.55       17.0  2.0 -3.32 -1.23       20.0  3.0  2.41  0.44        NaN  NaN  NaN  NaN
#                  4.0     restricted Cash                                         4.0   NaN  NaN  NaN        0.0  NaN -4.09    NaN        0.0  NaN  0.04   NaN        0.0  NaN -0.04   NaN        NaN  NaN  NaN  NaN
#                  6.0     accounts Receivable                                    26.0   6.0  NaN  NaN       20.0  5.0 -6.18  -1.18       18.0  5.0 -1.40 -0.53       22.0  6.0  3.93  1.54        NaN  NaN  NaN  NaN
#                  7.0     gross Accounts Receivable                              26.0   6.0  NaN  NaN       20.0  5.0 -6.25  -1.12       19.0  5.0 -1.35 -0.58       23.0  6.0  3.97  1.53        NaN  NaN  NaN  NaN
# ...                                                                              ...   ...  ...  ...        ...  ...   ...    ...        ...  ...   ...   ...        ...  ...   ...   ...        ...  ...  ...  ...
# INCOME STATEMENT 71.0    minority Interests                                     -0.0   0.0  NaN  NaN       -0.0  0.0 -0.32   0.00       -0.0  NaN  0.02   NaN       -0.0  NaN  0.19   NaN       -0.0  NaN  NaN  NaN
#                  73.0    special Income Charges                                 -0.0   NaN  NaN  NaN       -0.0  NaN -0.01    NaN        0.0  NaN  0.20   NaN        0.0  NaN -0.15   NaN        0.0  NaN  NaN  NaN
#                  74.0    total Unusual Items                                    -1.0  -0.0  NaN  NaN        1.0 -0.0  2.06   0.05       -1.0 -0.0 -1.96 -0.03        1.0  0.0  1.35  0.25       -0.0  0.0  NaN  NaN
#                  75.0    total Unusual Items Excluding Goodwill                 -1.0  -0.0  NaN  NaN        1.0 -0.0  2.06   0.05       -1.0 -0.0 -1.96 -0.03        1.0  0.0  1.35  0.25       -0.0  0.0  NaN  NaN
#                  76.0    reconciled Depreciation                                 9.0   1.0  NaN  NaN        7.0  2.0 -2.00   0.29        6.0  2.0 -0.40  0.73        8.0  2.0  1.88  0.00       11.0  3.0  NaN  NaN

# # Database connection
# conn = psycopg2.connect(dbname="russell",user="jose",password="letme2G@tin",host="localhost",port="5432")
# # Query the database and load directly into a DataFrame
# sctestcd = pd.read_sql_query("SELECT *  from ru.sc", conn)
# print(sctestcd)
# conn.close()

# sctestcd=sctestcd[['scgrp','scgrpid','sctest','sctestcd']]
# sctestcd = sctestcd.drop_duplicates()
# sctestcd.to_csv('data/sctestcd.csv')