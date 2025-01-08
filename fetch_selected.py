
import yfinance as yf
import pandas as pd


from yahoofinancials import YahooFinancials as YF
ticker=['BABA', 'GOOGL', 'AMZN', 'AAPL', 'BRK-B', 'EXPD', 'MA', 'MSFT', 'NVDA', 'PP.AT', 'QLYS', 'VEEV', 'NVO', 
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
f = YF(ticker)
a=f.get_financial_stmts(frequency ='annual', statement_type=[ 'income', 'balance', 'cash' ]) 


#---------------------------------------------- Flattening data

b=a['incomeStatementHistory']


# Flatten the JSON data
flattened_data = []

data=b
for company, records in data.items():
    for record in records:
        for date, metrics in record.items():
            row = {"Company": company, "Date": date}
            row.update(metrics)  # Add financial metrics
            flattened_data.append(row)

# Create a DataFrame
df = pd.DataFrame(flattened_data)

df.to_csv("data/fetch_selected_is.csv", index=False)


b=a['balanceSheetHistory']



# Flatten the JSON data
flattened_data = []

data=b
for company, records in data.items():
    for record in records:
        for date, metrics in record.items():
            row = {"Company": company, "Date": date}
            row.update(metrics)  # Add financial metrics
            flattened_data.append(row)

# Create a DataFrame
df = pd.DataFrame(flattened_data)

df.to_csv("data/fetch_selected_bs.csv", index=False)


d=a['cashflowStatementHistory']

# Flatten the JSON data
flattened_data = []

data=b
for company, records in data.items():
    for record in records:
        for date, metrics in record.items():
            row = {"Company": company, "Date": date}
            row.update(metrics)  # Add financial metrics
            flattened_data.append(row)

# Create a DataFrame
df = pd.DataFrame(flattened_data)

df.to_csv("data/fetch_selected_cf.csv", index=False)

