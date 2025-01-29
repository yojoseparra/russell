# --------------------------------------------- Share Price Fetch -------------------------------------------------------
tickers=['BABA', 'GOOGL', 'AMZN', 'AAPL', 'BRK-B', 'EXPD', 'MA', 'MSFT', 'NVDA', 'PP.AT', 'QLYS', 'VEEV', 'NVO', 
'IVU.DE', 'OLTH.AT', 'AVGO', 'GMWKF', 'MASI', 'MNST', 'WYNN', 'CHH', 'ANSS', 'IDXX', 'DEO', 'CLCGY', 'LRLCF', 'DANOY',
'0NWV.IL', 'PLWL.ME', 'GMKN.ME', 'CSCO', 'LVS', 'ETKAY', 'EXPGY', 'BKNG', 'VRSN', 'NJDCY', 'GVDBF',
 'EBAY', 'NVDA', 'CBCFF', 'INFY', 'AMGN', 'KAO.F', 'CWW.F', 'FUC.F', 'AAPL', 'KHC', 'SHW', 'ULTA', 'APH', 'AME', 'AMT',
 'ALFVY', 'ABBV', 'ZTS', 'TGR.BE', 'WNS', 'WES', 'WST','AVGO',
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

from yahooquery import Ticker
import pandas as pd


# Create a Ticker object
ticker_obj = Ticker(tickers)

# Fetch summary details (includes market cap)
summary_details = ticker_obj.summary_detail

# Ensure summary_details is a dictionary
if isinstance(summary_details, dict):
    # Initialize a list to store data
    data = []

    for ticker, details in summary_details.items():
        if isinstance(details, dict):  # Ensure we have valid data for the ticker
            row = details
            row['Ticker'] = ticker  # Add the ticker as a column
            data.append(row)
        else:
            print(f"Skipping {ticker}: Invalid data format")

    # Convert to DataFrame
    summary_df = pd.DataFrame(data)

    # Display the resulting DataFrame
    print(summary_df)
else:
    print("Unexpected data format:", summary_details)

summary_df.to_csv('data/summary_df.csv', index=False)
from datetime import datetime


e = pd.melt(summary_df, id_vars = ['Ticker','currency'], value_name ='fiorres', var_name='fitest')

e['timeStamp'] = datetime.now().date()

e.columns = ['subjid', 'fiorresu','fitest', 'fiorres', 'timeStamp']
e = e.dropna()

e['domain'] = 'MA' 

e['ficat'] = 'MARKET INDICATORS'


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
e.to_sql('ma', con=engine, if_exists='replace', index=False, schema='ru')



