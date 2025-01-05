# Warren Buffet to select companies based on book 'The Guru Investor' By John P. Reese

# --------------------------------------------------------------------------------------------------------
# --------------------------------------------- COSINE ---------------------------------------------------
# --------------------------------------------------------------------------------------------------------

# connecting to postgreSQL
exec(open('connect2sql.py').read())

# Query the database and load directly into a DataFrame
a = pd.read_sql_query("SELECT *  from ru.adcd", conn)
print(a)


# -------------------------------------------------------------------------------------------------------------------------------
# --------------------------------------------CREATING NEW VARS -----------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------
b= a.copy()
b[['asubjid', 'afidtc1']] = b['afidtc'].str.split('_', expand=True)
b.drop([ 'afidtc' ], axis= 1, inplace=True)
b.rename(columns={'afidtc1': 'afidtc' }, inplace=True)

tickers =['MATX', 'TH', 'HDSN', 'MCRI', 'IDCC', 'SHLS', 'MTH', 'KAI', 'FWRD']


c = b[(b['subjid'].isin(tickers) ) & (b['asubjid']== tickers[0] )].sort_values(by=['param','subjid', 'asubjid','fidtc', 'afidtc'])
c=c.reset_index(drop=True)
c=c[['dtype','param', 'subjid','fidtc', 'aval', 'asubjid', 'afidtc']]

# Remove duplicates for AVAL. I suppose that internally these values are longer than expected and that what we see as duplicate, they are not
# Therefore, I change the format

c['aval1'] = round(c[['aval']],2)*100
c.drop(['aval'] , axis= 1, inplace=True)
c.rename(columns={'aval1': 'aval' }, inplace=True)
d=c.drop_duplicates()
d.reset_index(drop=True)


# d.to_csv('data/d.csv', index=False)

d.sort_values(by=['afidtc','subjid', 'asubjid', 'param','fidtc'])
e = d.pivot(index=['dtype','subjid', 'asubjid', 'fidtc'], columns=['param','afidtc'], values='aval')
print(e)

# --------------------------------------------------------------- All tickers of interest -------------------------------
tickersql =", ".join(f"'{item}'" for item in tickers)
querying = f"SELECT *  from ru.pr where subjid in ({tickersql})"
pr = pd.read_sql_query( querying, conn)
print(pr.to_string())

conn.close()
# param                                                                               CHG                         FISTRESN
# afidtc                                                                       2021-12-31 2022-12-31 2023-12-31 2020-12-31 2021-12-31 2022-12-31 2023-12-31 2024-09-30
# dtype                                              subjid asubjid fidtc
# DERIVED: NORMALIZED COSINE DISTANCE BETWEEN SUB... DIOD   DIOD    2020-12-31        NaN        NaN        NaN      100.0       97.0       94.0       90.0       35.0
#                                                                   2021-12-31      100.0       36.0      -21.0       97.0      100.0       99.0       96.0       43.0
#                                                                   2022-12-31       36.0      100.0       33.0       94.0       99.0      100.0       98.0       42.0
#                                                                   2023-12-31      -21.0       33.0      100.0       90.0       96.0       98.0      100.0       35.0
#                                                                   2024-09-30        NaN        NaN        NaN       35.0       43.0       42.0       35.0      100.0
#                                                           XPEL    2020-12-31        NaN        NaN        NaN       75.0       77.0       78.0       78.0       32.0
#                                                                   2021-12-31      -25.0       22.0       -8.0       84.0       83.0       86.0       87.0       42.0
#                                                                   2022-12-31       -1.0       21.0       31.0       83.0       83.0       86.0       88.0       43.0
#                                                                   2023-12-31      -16.0       42.0       57.0       80.0       77.0       83.0       86.0       35.0
#                                                                   2024-09-30        NaN        NaN        NaN       70.0       68.0       66.0       62.0       92.0

e.to_csv('data/e.csv')