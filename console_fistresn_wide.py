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
b=a.copy()
# Third Try ------------------------------------ 
# the following displays the ticker data wide accross years
def long2wide_fistresn_wide(tickers=[ 'DIOD', 'FWRD'], dataframe=a):
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
    d.reset_index(inplace=True)

    e = d[d['subjid'] == tickers[0]].merge(d[d[ 'subjid' ]== tickers[1]], on= ['ficat','scgrpid', 'sctestcd'], how='left' )
    e.columns = e.columns.set_levels([level.str.replace('-12-31', '', regex=False) if level.dtype == 'object' else level for level in e.columns.levels])
    return e
    

tickers = [ 'MTH', 'UHG']
import os
os.system('cls')
e = long2wide_fistresn_wide(tickers=tickers)

#print(e.to_string( ) )
dir = 'data/' + '_'.join(tickers) + '.csv'
e.to_csv(dir)
querying = f"SELECT *  from ru.pr where subjid in ('{tickers[1]}')"
pr = pd.read_sql_query( querying, conn)
print(pr.to_string())

querying1 = f"SELECT *  from ru.pr where subjid in ('{tickers[0]}')"
pr1 = pd.read_sql_query( querying1, conn)
print(pr1.to_string())
#conn.close()
# >>> print(e.to_string( ) )
# fidtc subjid_x             ficat scgrpid                                                    sctestcd  2020_x  2021_x  2022_x  2023_x 2024-09-30_x 2020_x 2021_x 2022_x 2023_x 2024-09-30_x subjid_y  2020_y  2021_y  2022_y  2023_y 2024-09-30_y 2020_y 2021_y 2022_y 2023_y 2024-09-30_y
# param                                                                                                fistres fistres fistres fistres      fistres   chgn   chgn   chgn   chgn         chgn          fistres fistres fistres fistres      fistres   chgn   chgn   chgn   chgn         chgn
# 0         DIOD     BALANCE SHEET     1.0                                   cash And Cash Equivalents    22.0    20.0    17.0    19.0          NaN    NaN  -1.67  -3.31   2.15          NaN     XPEL    18.0     4.0     2.0     3.0          NaN    NaN -14.55  -1.23   0.44          NaN
# 1         DIOD     BALANCE SHEET     2.0            cash Cash Equivalents And Short Term Investments    22.0    21.0    17.0    20.0          NaN    NaN  -1.80  -3.32   2.41          NaN     XPEL    18.0     4.0     2.0     3.0          NaN    NaN -14.55  -1.23   0.44          NaN
# 2         DIOD     BALANCE SHEET     4.0                                             restricted Cash     4.0     0.0     0.0     0.0          NaN    NaN  -4.09   0.04  -0.04          NaN      NaN     NaN     NaN     NaN     NaN          NaN    NaN    NaN    NaN    NaN          NaN
# 3         DIOD     BALANCE SHEET     6.0                                         accounts Receivable    26.0    20.0    18.0    22.0          NaN    NaN  -6.18  -1.40   3.93          NaN     XPEL     6.0     5.0     5.0     6.0          NaN    NaN  -1.18  -0.53   1.54          NaN
# 4         DIOD     BALANCE SHEET     7.0                                   gross Accounts Receivable    26.0    20.0    19.0    23.0          NaN    NaN  -6.25  -1.35   3.97          NaN     XPEL     6.0     5.0     5.0     6.0          NaN    NaN  -1.12  -0.58   1.53          NaN
# 5         DIOD     BALANCE SHEET     8.0                  allowance For Doubtful Accounts Receivable    -0.0    -0.0    -0.0    -0.0          NaN    NaN   0.07  -0.05  -0.05          NaN     XPEL    -0.0    -0.0    -0.0    -0.0          NaN    NaN  -0.06   0.05   0.01          NaN
# 6         DIOD     BALANCE SHEET    11.0                                              prepaid Assets     6.0     6.0     4.0     NaN          NaN    NaN   0.23  -1.74    NaN          NaN     XPEL     1.0     1.0     NaN     NaN          NaN    NaN   0.51    NaN    NaN          NaN
# 7         DIOD     BALANCE SHEET    13.0                                              current Assets    83.0    66.0    58.0    71.0          NaN    NaN -17.51  -7.73  13.39          NaN     XPEL    40.0    30.0    33.0    37.0          NaN    NaN  -9.02   2.49   3.99          NaN
# 8         DIOD     BALANCE SHEET    14.0                                                 receivables    26.0    20.0    18.0    22.0          NaN    NaN  -6.18  -1.40   3.93          NaN     XPEL     6.0     5.0     5.0     6.0          NaN    NaN  -0.94  -0.77   1.71          NaN
# 9         DIOD     BALANCE SHEET    18.0                                                   inventory    25.0    19.0    18.0    23.0          NaN    NaN  -5.67  -1.30   5.45          NaN     XPEL    14.0    20.0    25.0    27.0          NaN    NaN   5.96   4.84   2.01          NaN
# 10        DIOD     BALANCE SHEET    19.0                                              finished Goods     7.0     6.0     5.0     8.0          NaN    NaN  -0.94  -1.18   2.98          NaN     XPEL    14.0    19.0    20.0    20.0          NaN    NaN   4.85   0.65   0.11          NaN



