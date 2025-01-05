# Warren Buffet to select companies based on book 'The Guru Investor' By John P. Reese

# --------------------------------------------------------------------------------------------------------
# --------------------------------------------- CHG FISTRESN ---------------------------------------------
# --------------------------------------------------------------------------------------------------------
# Query the database and load directly into a DataFrame

# connecting to postgreSQL
exec(open('connect2sql.py').read())
# Query the database and load directly into a DataFrame
a = pd.read_sql_query("SELECT *  from ru.console_display", conn)
print(a)
conn.close()
b=a.copy()
# Third Try ------------------------------------ 
# the following displays the ticker data wide accross years
def long2wide_fistresn(tickers=[ 'DIOD', 'XPEL'], dataframe=a):
    # the following displays the ticker data wide accross years
    # This code works with 2 tickers
    b=dataframe[dataframe.subjid.isin(tickers)].copy()
    c = b[['subjid', 'scgrpid','ficat', 'sctestcd', 'fidtc', 'fistres']].sort_values(by=['subjid', 'ficat','scgrpid', 'fidtc'])
    c = c.melt(id_vars=['subjid', 'scgrpid','ficat', 'sctestcd', 'fidtc'], value_vars= 'fistres' , var_name='param', value_name='aval')
    c = c.pivot(index=['subjid','ficat','scgrpid', 'sctestcd'], columns=[ 'fidtc', 'param'], values='aval') 

    ca = b[['subjid', 'scgrpid','ficat', 'sctestcd', 'fidtc', 'chgn']].sort_values(by=['subjid',  'ficat','scgrpid', 'fidtc'])
    ca = ca.melt(id_vars=['subjid', 'scgrpid','ficat', 'sctestcd', 'fidtc'], value_vars= 'chgn' , var_name='param', value_name='aval')
    ca = ca.pivot(index=['subjid','ficat','scgrpid', 'sctestcd'], columns=[ 'fidtc', 'param'], values='aval') 
    d = c.merge(ca, on=['subjid','ficat','scgrpid', 'sctestcd'], how='left')


    return d
    


import os
os.system('cls')
d = long2wide_fistresn([ 'DIOD', 'XPEL'])

print(d.to_string( ) )

d.to_csv('data/d.csv')


# fidtc                                                                            2020-12-31 2021-12-31 2022-12-31 2023-12-31 2024-09-30 2020-12-31 2021-12-31 2022-12-31 2023-12-31 2024-09-30
# param                                                                               fistres    fistres    fistres    fistres    fistres       chgn       chgn       chgn       chgn       chgn
# subjid ficat            scgrpid sctestcd
# DIOD   BALANCE SHEET    1.0     cash And Cash Equivalents                              22.0       20.0       17.0       19.0        NaN        NaN      -1.67      -3.31       2.15        NaN
#                         2.0     cash Cash Equivalents And Short Term Investments       22.0       21.0       17.0       20.0        NaN        NaN      -1.80      -3.32       2.41        NaN
#                         4.0     restricted Cash                                         4.0        0.0        0.0        0.0        NaN        NaN      -4.09       0.04      -0.04        NaN
#                         6.0     accounts Receivable                                    26.0       20.0       18.0       22.0        NaN        NaN      -6.18      -1.40       3.93        NaN
#                         7.0     gross Accounts Receivable                              26.0       20.0       19.0       23.0        NaN        NaN      -6.25      -1.35       3.97        NaN
# ...                                                                                     ...        ...        ...        ...        ...        ...        ...        ...        ...        ...
# XPEL   INCOME STATEMENT 68.0    diluted Average Shares                                 17.0       11.0        9.0        7.0        7.0        NaN      -6.72      -2.13      -1.55        NaN
#                         71.0    minority Interests                                      0.0        0.0        NaN        NaN        NaN        NaN       0.00        NaN        NaN        NaN
#                         74.0    total Unusual Items                                    -0.0       -0.0       -0.0        0.0        0.0        NaN       0.05      -0.03       0.25        NaN
#                         75.0    total Unusual Items Excluding Goodwill                 -0.0       -0.0       -0.0        0.0        0.0        NaN       0.05      -0.03       0.25        NaN
#                         76.0    reconciled Depreciation                                 1.0        2.0        2.0        2.0        3.0        NaN       0.29       0.73       0.00        NaN

# connecting to postgreSQL
exec(open('connect2sql.py').read())
# Query the database and load directly into a DataFrame
pr = pd.read_sql_query("SELECT *  from ru.pr where subjid in ('DIOD', 'XPEL')", conn)
print(pr.to_string())
conn.close()
