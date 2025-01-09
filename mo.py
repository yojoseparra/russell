# MOAT
import yfinance as yf
import pandas as pd


from yahoofinancials import YahooFinancials as YF

ticker=['BABA', 'GOOGL', 'AMZN', 'AAPL', 'BRK-B', 'EXPD', 'MA', 'MSFT', 'NVDA', 'PP.AT', 'QLYS', 'VEEV', 'NVO', 
'IVU.DE', 'OLTH.AT', 'AVGO', 'GMWKF', 'MASI', 'MNST', 'WYNN', 'CHH', 'ANSS', 'IDXX', 'DEO', 'CLCGY', 'LRLCF', 'DANOY',
'0NWV.IL', 'PLWL.ME', 'GMKN.ME', 'CSCO', 'LVS', 'ETKAY', 'EXPGY', 'BKNG', 'VRSN', 'NJDCY', 'GVDBF',
'EBAY', 'NVDA', 'CBCFF', 'INFY', 'AMGN', 'KAO.F', 'CWW.F', 'FUC.F', 'AAPL', 'KHC', 'SHW', 'ULTA', 'APH', 'AME', 'AMT',
'ALFVY', 'ABBV', 'ZTS', 'TGR.BE', 'WNS', 'WES', 'WST','AVGO', 'FWRD' ,'HDSN' ,'IDCC' ,'KAI' ,'MATX' ,'MCRI' ,'MTH' ,
'SHLS' ,'TH' ,'DIOD' ,'XPEL',
'GMWKF',
'INXN',
'MASI',
'MNST',
'WYNN',
'CHH',
'ANSS',
'IDXX',
'DEO',
'CLCGY',
'LRLCF',
'DANOY',
'0NWV.IL',
'PLZL.ME',
'GMKN.ME',
'CSCO',
'LVS',
'EKTAY',
'600276.SS',
'EXPGY',
'BKNG',
'VRSN',
'NJDCY',
'GVDBF',
'EBAY',
'NVDA',
'CBCFF',
'600519.SS',
'603288.SS',
'INFY',
'AMGN',
'KAO.F',
'CWW.F',
'FUC.F',
'AAPL',
'KHC',
'SHW',
'ULTA',
'APH',
'AME',
'AMT',
'ALFVY',
'ABBV',
'ZTS',
'TGR.BE',
'WNS',
'WEX',
'WES',
'WST',
'WFAFF',
'WEGE3.SA',
'WDFC',
'WAT',
'WCN',
'WMMVY',
'WMT',
'V',
'VRSK',
'VEEV',
'VACNY',
'USB',
'UPS',
'UNP',
'UL',
'UNICY',
'TRAUF',
'TRU',
'TDG',
'WU',
'TTC',
'HD',
'HSY',
'TXN',
'TCEHY',
'TMSNY',
'TGYM.MI',
'TROW',
'TRBCX',
'SNPS',
'SYIEY',
'SYK',
'SAUHF',
'SBUX',
'F000003W8R.L',
'SPXSF',
'SCCO',
'SONVY',
'SIRI',
'SPXCY',
'SKFOF',
'SMMNY',
'SSDOY',
'SGIOY',
'SHZHY',
'SGSOY',
'NOW',
'SEIC',
'SBGSY',
'SDMHF',
'SAP',
'SCHYF',
'SAFRY',
'SPGI',
'RY',
'RTOXF',
'ROL',
'ROK',
'RTMVY',
'RMD',
'RSG',
'RELX',
'RELIANCE.NS',
'RCRRF',
'REC.MI',
'REA.AX',
'UNLRF',
'PUODY',
'PG',
'PTAUY',
'POOL',
'PII',
'PAA',
'PEP',
'PAYX',
'PGPHF',
'OLCLY',
'ORCL',
'NVZMY',
'NVO',
'NVS',
'NOC',
'NTRS',
'NSC',
'NDSN',
'NKE',
'035420.KS',
'NPSNY',
'6268.T',
'MSCI',
'MCO',
'MPWR',
'MSFT',
'MRK',
'MELI',
'MCD',
'MKC',
'MA',
'MKTX',
'MANH',
'MCQEF',
'0HAU.IL',
'LOW',
'LNSTY',
'LMT',
'LGRVF',
'LANC',
'LTOUF',
'LSTR']

import pandas as pd
from yahooquery import Ticker
f = Ticker(ticker)
# Retrieve financial statements
i = f.income_statement()
i.to_csv('data/is.csv')
b = f.balance_sheet()
b.to_csv('data/bs.csv')
c = f.cash_flow()
c.to_csv('data/cf.csv')

i.reset_index(inplace=True)
b.reset_index(inplace=True)
c.reset_index(inplace=True)

e = pd.melt(i, id_vars = ['symbol','asOfDate', 'periodType', 'currencyCode'], value_name ='fiorres', var_name='fitest')
e = e.dropna()
e.columns = ['subjid', 'fidtc', 'fiperiod','fiorresu','fitest', 'fiorres']
e['domain'] = 'MO'
e['ficat'] = 'INCOME STATEMENT'
f = e[ [ 'domain', 'ficat', 'subjid', 'fitest','fiorres', 'fiorresu', 'fidtc', 'fiperiod']]



#### 


e = pd.melt(b, id_vars = ['symbol','asOfDate', 'periodType', 'currencyCode'], value_name ='fiorres', var_name='fitest')
e.columns = ['subjid', 'fidtc', 'fiperiod','fiorresu','fitest', 'fiorres']
e = e.dropna()

e['domain'] = 'MO'
e['ficat'] = 'BALANCE SHEET'

g = e[ [ 'domain', 'ficat', 'subjid', 'fitest','fiorres', 'fiorresu', 'fidtc', 'fiperiod']]


###


e = pd.melt(c, id_vars = ['symbol','asOfDate', 'periodType', 'currencyCode'], value_name ='fiorres', var_name='fitest')
e.columns = ['subjid', 'fidtc', 'fiperiod','fiorresu','fitest', 'fiorres']
e = e.dropna()
e['domain'] = 'MO' 

e['ficat'] = 'CASH FLOWS'

h = e[ [ 'domain', 'ficat', 'subjid', 'fitest','fiorres', 'fiorresu', 'fidtc', 'fiperiod']]




z = pd.concat([f,g,h])

z.to_csv('data/z.csv', index=False)

f.to_csv('data/f.csv')
g.to_csv('data/g.csv')
h.to_csv('data/h.csv')


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
z.to_sql('mo', con=engine, if_exists='replace', index=False, schema='ru')




