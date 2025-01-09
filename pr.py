# Subject Profile PR
import pandas as pd
import psycopg2
import os
wd = os.getcwd()
d = pd.read_csv(wd+"/data/pr.csv")

# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
from yahooquery import Ticker

# List of company tickers
companies = ['BABA', 'GOOGL', 'AMZN', 'AAPL', 'BRK-B', 'EXPD', 'MA', 'MSFT', 'NVDA', 'PP.AT', 'QLYS', 'VEEV', 'NVO', 
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

def get_profile(ticker):
    retries = 3  # Set the number of retries
    for attempt in range(retries):
        try:
            t = Ticker(ticker)
            profile = t.asset_profile
            return profile
        except RetryError:
            print(f"Rate limit hit for {ticker}, retrying...")
            time.sleep(30)  # Wait before retrying
        except Exception as e:
            print(f"Error fetching data for {ticker}: {e}")
            break
    return None

# Example usage
tickers = ['AAPL', 'MSFT', 'GOOG']

# Create an empty list to store profile data
profiles_list = []

# Fetch and store profiles
for ticker in tickers:
    profile = get_profile(ticker)
    if profile:
        # Assuming the profile is a dictionary, you can convert it into a row
        profile_data = profile.get('assetProfile', {})
        profile_data['ticker'] = ticker  # Add the ticker as a new column
        profiles_list.append(profile_data)
    else:
        print(f"Could not fetch profile for {ticker}")

# Convert the list of profiles into a DataFrame
df_profiles = pd.DataFrame(profiles_list)

# Display the DataFrame
print(df_profiles)













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


# Insert the DataFrame into the SQL table
d.to_sql('pr', con=engine, if_exists='replace', index=False, schema='ru')






