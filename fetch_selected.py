
import yfinance as yf
import pandas as pd


from yahoofinancials import YahooFinancials as YF
ticker=[
'ATMU', 'BBSI', 'BCC', 'BDC', 'BTU', 'BXC', 'CCOI', 'CEIX', 'COCO',
       'CVLG', 'DENN', 'DIOD', 'ELA', 'EVRI', 'EVTC', 'FTDR', 'FWRD',
       'GOLF', 'GRBK', 'HCC', 'HCKT', 'HDSN', 'HLF', 'IBP', 'IDCC',
       'IMXI', 'INVA', 'IPAR', 'JBI', 'KAI', 'KRT', 'KTB', 'LEGH', 'LEU',
       'LGIH', 'MATX', 'MCRI', 'METCB', 'MHO', 'MTH', 'MYE', 'NRC',
       'PMTS', 'PRKS', 'RYI', 'SHLS', 'STC', 'STRL', 'TEX', 'TH', 'TWI',
       'UHG', 'VC', 'WNC', 'XPEL', 'ZYXI']
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

