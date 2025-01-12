# Subject Profile PR
import pandas as pd
import psycopg2
import os

# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
from yahooquery import Ticker

# List of company tickers
tickers = ['BABA', 'GOOGL', 'AMZN', 'AAPL', 'BRK-B', 'EXPD', 'MA', 'MSFT', 'NVDA', 'PP.AT', 'QLYS', 'VEEV', 'NVO', 
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
import time
from yahooquery import Ticker
from requests.exceptions import RetryError


# Create a Ticker object for multiple symbols
companies = Ticker(tickers)
# Fetch profiles for all companies
profiles = companies.asset_profile

# Convert to a DataFrame
profiles_df = pd.DataFrame(profiles).T  # Transpose for easier reading
profiles_df.reset_index(inplace=True)
#profiles_df.drop('level_0', axis=1)

from sqlalchemy import create_engine
from urllib.parse import quote_plus

# connecting to postgreSQL
exec(open('connect2sql.py').read())

# profiles_df.to_csv('data/profiles.csv', index=True)


d = pd.read_csv('data/profiles.csv',  encoding='utf-8')


# connecting to postgreSQL
exec(open('connect2sql.py').read())
# Connection string
connection_string = f'postgresql+psycopg2://{username}:{escaped_password}@{host}/{database}'
engine = create_engine(connection_string)


# Insert the DataFrame into the SQL table this is the cd or cosine distance
# adcd_1 represents cosine distances within subjids or tickers for different periods.
d.to_sql('pr', con=engine, if_exists='replace', index=False, schema='ru')






