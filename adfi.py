#1.0 -- Adding a new variable to the data called fistresn, which is the fiorres / total revenue This is my form of standardize the data 
#2.0 -- additionally the objective is to regisger the increase of fistresn accross years

# -------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------ creating the variable fistresn -----------------------------------------
#1.0 -- Adding a new variable to the data called fistresn, which is the fiorres / total revenue This is my form of standardize the data 
# -------------------------------------------------------------------------------------------------------------------------------------

# connecting to postgreSQL
exec(open('connect2sql.py').read())

# Query the database and load directly into a DataFrame
a = pd.read_sql_query("SELECT subjid, ficat, fitest, fiorres, fidtc from ru.fi order by subjid, ficat, fidtc", conn)
print(a)
conn.close()
df=a.copy()


# Step 1: Find the 'totalRevenue' for each combination of ticker and date
revenue_dict = df[df['fitest'] == 'totalRevenue'].groupby(['subjid', 'fidtc'])['fiorres'].first().to_dict()

# Step 2: Define the function to apply
def divide_by_revenue(row):
    # Retrieve the totalRevenue for the current ticker and date
    total_revenue = revenue_dict.get((row['subjid'], row['fidtc']), None)

    # Check if totalRevenue is valid (not None and not zero)
    if total_revenue is None or total_revenue == 0:
        return float('nan')  # Return NaN for missing or zero totalRevenue
    else:
        return row['fiorres'] / total_revenue  # Perform the division safely

# Step 3: Apply the function to each row and create the 'value_new' column
df['fistresn'] = df.apply(divide_by_revenue, axis=1)
z =  df[['subjid', 'ficat', 'fitest', 'fidtc', 'fistresn']]
# Show the result
print(df)
#------------------------------------------------------------------- creating a variable chg and pchg ---------------------------------
#2.0 -- additionally the objective is to regisger the increase of fistresn accross years ----------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------

df =  z[['subjid', 'ficat', 'fitest', 'fidtc', 'fistresn']]

# Ensure 'date' is a datetime object
df['fidtc'] = pd.to_datetime(df['fidtc'])

# Pivot to restructure data
pivot_df = df.pivot(index=['subjid', 'ficat', 'fitest'], columns='fidtc', values='fistresn')

# Extract year-end dates and handle the most recent column
# using list comprehension
# [expression for item in iterable if condition]

year_end_dates = [col for col in pivot_df.columns if col.month == 12 and col.day == 31]
latest_date = pivot_df.columns[-1]

# If the latest date is not in year-end dates, add it to the list
if latest_date not in year_end_dates:
    year_end_dates.append(latest_date)

# Sort the dates to ensure chronological order
year_end_dates = sorted(year_end_dates)

# Calculate changes for selected dates
change_columns = []
for i in range(len(year_end_dates) - 1):
    col_1 = year_end_dates[i]
    col_2 = year_end_dates[i + 1]
    change_col = f"{col_2}_chg"
    pivot_df[change_col] = pivot_df[col_2] - pivot_df[col_1]
    change_columns.append(change_col)

# Reset index to flatten the DataFrame
result_df = pivot_df.reset_index()


# Select only the 'change' columns along with identifiers
change_columns = [col for col in result_df.columns if "_chg" in str(col)]
subset_df = result_df[['subjid', 'ficat', 'fitest'] + change_columns]

# Rename the change columns to remove "change_"
rename_mapping = {col: col.replace(" 00:00:00_chg", "") for col in change_columns}
subset_df = subset_df.rename(columns=rename_mapping)

# Melting

y= subset_df.melt(id_vars=['subjid', 'ficat','fitest'], var_name='fidtc', value_name='chg')
x=y.dropna()
w=z.dropna()
v = pd.merge(w,x,on=['subjid', 'ficat', 'fitest','fidtc'], how='left')

# -------------------------------------- creating the adfi dataset: Analysis DAtaset for FInancials
from sqlalchemy import create_engine
from urllib.parse import quote_plus

username = ''
password = ''
host = 'localhost'
database = ''

# Escape the password
escaped_password = quote_plus(password)

# Connection string
connection_string = f'postgresql+psycopg2://{username}:{escaped_password}@{host}/{database}'
engine = create_engine(connection_string)


# Insert the DataFrame into the SQL table
v.to_sql('adfi', con=engine, if_exists='replace', index=False, schema='ru')

################################################################################################
# ----------------------------------- EXAMPLES START ____________________________________
# ----------------------------------- EXAMPLES START ____________________________________
# ----------------------------------- EXAMPLES START ____________________________________
################################################################################################
import pandas as pd

# Example DataFrame
df = pd.DataFrame({
    'ticker': ['ABC', 'ABC', 'ABC', 'XYZ', 'XYZ', 'XYZ'],
    'statements': ['Income Statement', 'Cash Flow Statement', 'Balance Sheet', 
                   'Income Statement', 'Cash Flow Statement', 'Balance Sheet'],
    'parameter': ['totalRevenue', 'netIncomeFromContinuingOperations', 'totalDebt',
                  'totalRevenue', 'netIncomeFromContinuingOperations', 'totalDebt'],
    'value': [100, 20, 200, 110, 15, 250]
})

# Initialize an empty list to hold the results
result_list = []

# Step 1: Loop through each group of 'ticker'
for ticker, group in df.groupby('ticker'):
    # Check if 'totalRevenue' exists in the group
    total_revenue_row = group[group['parameter'] == 'totalRevenue']
    
    if not total_revenue_row.empty:
        # Get the 'totalRevenue' value for the group
        total_revenue = total_revenue_row['value'].values[0]
        
        # Create the 'value_new' column by dividing the 'value' by totalRevenue
        group['value_new'] = group['value'] / total_revenue
    else:
        # If no 'totalRevenue', set 'value_new' to NaN for all rows in the group
        group['value_new'] = float('nan')
    
    # Append the processed group back into the result list
    result_list.append(group)

# Step 2: Concatenate the processed groups back into a single DataFrame
final_df = pd.concat(result_list)

# Show the result
print(final_df)


# ------------------ second approach using a small example just to fix the final code to run all data
import pandas as pd

# Example DataFrame
df = pd.DataFrame({
    'ticker': ['ABC', 'ABC', 'ABC', 'XYZ', 'XYZ', 'XYZ'],
    'statements': ['Income Statement', 'Cash Flow Statement', 'Balance Sheet', 
                   'Income Statement', 'Cash Flow Statement', 'Balance Sheet'],
    'parameter': ['totalRevenue', 'netIncomeFromContinuingOperations', 'totalDebt',
                  'totalRevenue', 'netIncomeFromContinuingOperations', 'totalDebt'],
    'value': [100, 20, 200, 110, 15, 250]
})

# Step 1: Find the 'totalRevenue' for each ticker
revenue_dict = df[df['parameter'] == 'totalRevenue'].groupby('ticker')['value'].first().to_dict()

# Step 2: Define the function to apply
def divide_by_revenue(row):
    # Retrieve the totalRevenue for the current ticker
    total_revenue = revenue_dict.get(row['ticker'], None)
    
    if total_revenue is not None:
        # Divide the value by totalRevenue
        return row['value'] / total_revenue
    else:
        # If no totalRevenue is found, return NaN
        return float('nan')

# Step 3: Apply the function to each row and create the 'value_new' column
df['value_new'] = df.apply(divide_by_revenue, axis=1)

# Show the result
print(df)

#    ticker           statements                          parameter  value  value_new
# 0    ABC     Income Statement                       totalRevenue    100   1.000000
# 1    ABC  Cash Flow Statement  netIncomeFromContinuingOperations     20   0.200000
# 2    ABC        Balance Sheet                          totalDebt    200   2.000000
# 3    XYZ     Income Statement                       totalRevenue    110   1.000000
# 4    XYZ  Cash Flow Statement  netIncomeFromContinuingOperations     15   0.136364
# 5    XYZ        Balance Sheet                          totalDebt    250   2.272727
 
# ------------------------------ using the second approach with dates ---------------------------------


import pandas as pd

# Example DataFrame with a 'date' column
df = pd.DataFrame({
    'ticker': ['ABC', 'ABC', 'ABC', 'XYZ', 'XYZ', 'XYZ','ABC', 'ABC', 'ABC'],
    'statements': ['Income Statement', 'Cash Flow Statement', 'Balance Sheet', 
                    'Income Statement', 'Cash Flow Statement', 'Balance Sheet', 
                   'Income Statement', 'Cash Flow Statement', 'Balance Sheet'],
    'parameter': ['totalRevenue', 'netIncomeFromContinuingOperations', 'totalDebt',
                 'totalRevenue', 'netIncomeFromContinuingOperations', 'totalDebt',
                  'totalRevenue', 'netIncomeFromContinuingOperations', 'totalDebt'],
    'value': [100, 20, 200, 110, 15, 250, 110,30,180],
    'date': ['2021-01-01', '2021-01-01', '2021-01-01',
             '2021-01-01', '2021-01-01', '2021-01-01',
             '2022-01-01', '2022-01-01', '2022-01-01']})

# Step 1: Find the 'totalRevenue' for each combination of ticker and date
revenue_dict = df[df['parameter'] == 'totalRevenue'].groupby(['ticker', 'date'])['value'].first().to_dict()

# Step 2: Define the function to apply
def divide_by_revenue(row):
    # Retrieve the totalRevenue for the current ticker and date
    total_revenue = revenue_dict.get((row['ticker'], row['date']), None)
    
    if total_revenue is not None:
        # Divide the value by totalRevenue
        return row['value'] / total_revenue
    else:
        # If no totalRevenue is found, return NaN
        return float('nan')

# Step 3: Apply the function to each row and create the 'value_new' column
df['value_new'] = df.apply(divide_by_revenue, axis=1)

# Show the result
print(df)


#   ticker           statements                          parameter  value        date  value_new
# 0    ABC     Income Statement                       totalRevenue    100  2021-01-01   1.000000
# 1    ABC  Cash Flow Statement  netIncomeFromContinuingOperations     20  2021-01-01   0.200000
# 2    ABC        Balance Sheet                          totalDebt    200  2021-01-01   2.000000
# 3    XYZ     Income Statement                       totalRevenue    110  2021-01-01   1.000000
# 4    XYZ  Cash Flow Statement  netIncomeFromContinuingOperations     15  2021-01-01   0.136364
# 5    XYZ        Balance Sheet                          totalDebt    250  2021-01-01   2.272727
# 6    ABC     Income Statement                       totalRevenue    110  2022-01-01   1.000000
# 7    ABC  Cash Flow Statement  netIncomeFromContinuingOperations     30  2022-01-01   0.272727
# 8    ABC        Balance Sheet                          totalDebt    180  2022-01-01   1.636364


# ------------------------------ creating a change variable --------------------------------------------------

import pandas as pd

# Example DataFrame with a 'date' column
df = pd.DataFrame({
    'ticker': ['ABC', 'ABC', 'ABC', 'XYZ', 'XYZ', 'XYZ','ABC', 'ABC', 'ABC'],
    'statements': ['Income Statement', 'Cash Flow Statement', 'Balance Sheet', 
                    'Income Statement', 'Cash Flow Statement', 'Balance Sheet', 
                   'Income Statement', 'Cash Flow Statement', 'Balance Sheet'],
    'parameter': ['totalRevenue', 'netIncomeFromContinuingOperations', 'totalDebt',
                 'totalRevenue', 'netIncomeFromContinuingOperations', 'totalDebt',
                  'totalRevenue', 'netIncomeFromContinuingOperations', 'totalDebt'],
    'value': [100, 20, 200, 110, 15, 250, 110,30,180],
    'date': ['2021-01-01', '2021-01-01', '2021-01-01',
             '2021-01-01', '2021-01-01', '2021-01-01',
             '2022-01-01', '2022-01-01', '2022-01-01']})

import pandas as pd

# Example DataFrame
df = pd.DataFrame({
    'ticker': ['ABC', 'ABC', 'ABC', 'XYZ', 'XYZ', 'XYZ', 'ABC', 'ABC', 'ABC', 'ABC', 'ABC', 'ABC'],
    'statements': ['Income Statement', 'Cash Flow Statement', 'Balance Sheet', 
                   'Income Statement', 'Cash Flow Statement', 'Balance Sheet', 
                   'Income Statement', 'Cash Flow Statement', 'Balance Sheet',
                   'Income Statement', 'Cash Flow Statement', 'Balance Sheet'],
    'parameter': ['totalRevenue', 'netIncomeFromContinuingOperations', 'totalDebt',
                  'totalRevenue', 'netIncomeFromContinuingOperations', 'totalDebt',
                  'totalRevenue', 'netIncomeFromContinuingOperations', 'totalDebt',
                  'totalRevenue', 'netIncomeFromContinuingOperations', 'totalDebt'],
    'value': [100, 20, 200, 110, 15, 250, 110, 30, 180, 120, 40, 160],
    'date': ['2021-01-01', '2021-01-01', '2021-01-01',
             '2021-01-01', '2021-01-01', '2021-01-01',
             '2022-01-01', '2022-01-01', '2022-01-01',
             '2023-01-01', '2023-01-01', '2023-01-01']
})

# Ensure 'date' is a datetime object
df['date'] = pd.to_datetime(df['date'])

# Pivot to restructure data for comparison
pivot_df = df.pivot(index=['ticker', 'statements', 'parameter'], columns='date', values='value')

# Sort columns to ensure chronological order
pivot_df = pivot_df.sort_index(axis=1)

# Calculate changes for all consecutive years
change_columns = []
for i in range(len(pivot_df.columns) - 1):
    col_1 = pivot_df.columns[i]
    col_2 = pivot_df.columns[i + 1]
    change_col = f"change_{col_1.year}_{col_2.year}"
    pivot_df[change_col] = pivot_df[col_2] - pivot_df[col_1]
    change_columns.append(change_col)

# Reset index to flatten the DataFrame
result_df = pivot_df.reset_index()

# Show the result
print(result_df)
# date ticker           statements                          parameter  2021-01-01 00:00:00  2022-01-01 00:00:00  2023-01-01 00:00:00  change_2021_2022  change_2022_2023
# 0       ABC        Balance Sheet                          totalDebt                200.0                180.0                160.0             -20.0             -20.0
# 1       ABC  Cash Flow Statement  netIncomeFromContinuingOperations                 20.0                 30.0                 40.0              10.0              10.0
# 2       ABC     Income Statement                       totalRevenue                100.0                110.0                120.0              10.0              10.0
# 3       XYZ        Balance Sheet                          totalDebt                250.0                  NaN                  NaN               NaN               NaN
# 4       XYZ  Cash Flow Statement  netIncomeFromContinuingOperations                 15.0                  NaN                  NaN               NaN               NaN
# 5       XYZ     Income Statement                       totalRevenue                110.0                  NaN                  NaN               NaN               NaN
# ----------------------------------- EXAMPLES END ------------------------------------------------------------------------------------

