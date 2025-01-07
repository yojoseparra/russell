#1.0 -- Adding a new variable to the data called fistresn, which is the fiorres / total revenue This is my form of standardize the data 
#2.0 -- additionally the objective is to regisger the increase of fistresn accross years

# -------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------ creating the variable fistresn -----------------------------------------
#1.0 -- Adding a new variable to the data called fistresn, which is the fiorres / total revenue This is my form of standardize the data 
# -------------------------------------------------------------------------------------------------------------------------------------

# connecting to postgreSQL
exec(open('connect2sql.py').read())

# Query the database and load directly into a DataFrame
a = pd.read_sql_query("SELECT * from ru.qfi ", conn)
print(a)
conn.close()
df=a.copy()


# Step 1: Find the 'totalRevenue' for each combination of ticker and date
revenue_dict = df[df['fitest'] == 'TotalRevenue'].groupby(['subjid', 'fidtc', 'fiperiod'])['fiorres'].first().to_dict()

# Step 2: Define the function to apply
def divide_by_revenue(row):
    # Retrieve the totalRevenue for the current ticker and date
    total_revenue = revenue_dict.get((row['subjid'], row['fidtc'], row['fiperiod']), None)

    # Check if totalRevenue is valid (not None and not zero)
    if total_revenue is None or total_revenue == 0:
        return float('nan')  # Return NaN for missing or zero totalRevenue
    else:
        return row['fiorres'] / total_revenue  # Perform the division safely

# Step 3: Apply the function to each row and create the 'value_new' column
df['fistresn'] = df.apply(divide_by_revenue, axis=1)

z1 = df.copy()


z =  df[['subjid', 'ficat', 'fitest', 'fidtc', 'fiperiod', 'fiorres']]


#------------------------------------------------------------------- creating a variable chg and pchg ---------------------------------
#2.0 -- additionally the objective is to regisger the increase of fistresn accross years ----------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------

df =  z[['subjid', 'ficat', 'fitest', 'fidtc', 'fiperiod', 'fiorres']]

# Ensure 'date' is a datetime object
df['fidtc'] = pd.to_datetime(df['fidtc'], format="%Y-%m-%d").dt.date


# Pivot to restructure data
pivot_df = df.pivot(index=['subjid', 'ficat', 'fitest', 'fiperiod'], columns='fidtc', values='fiorres')

# Extract year-end dates and handle the most recent column
# using list comprehension
# [expression for item in iterable if condition]

b = [col for col in pivot_df.columns if col.month == 3]
c = [col for col in pivot_df.columns if col.month == 6]
d = [col for col in pivot_df.columns if col.month == 9]
e = [col for col in pivot_df.columns if col.month == 12]




# Sort the dates to ensure chronological order
#year_end_dates = sorted(year_end_dates)

# Calculate changes for selected dates
change_columns = []

for i in range(len(b) - 1 ):
    col_1 = b[i]
    col_2 = b[i + 1]
    change_col = f"{col_2}_{col_1}_chg"
    pivot_df[change_col] = (pivot_df[col_2] - pivot_df[col_1]) / pivot_df[col_1]
    change_columns.append(change_col)

for i in range(len(c) - 1 ):
    col_1 = c[i]
    col_2 = c[i + 1]
    change_col = f"{col_2}_{col_1}_chg"
    pivot_df[change_col] =  (pivot_df[col_2] - pivot_df[col_1]) / pivot_df[col_1]
    change_columns.append(change_col)

for i in range(len(d) - 1 ):
    col_1 = d[i]
    col_2 = d[i + 1]
    change_col = f"{col_2}_{col_1}_chg"
    pivot_df[change_col] =  (pivot_df[col_2] - pivot_df[col_1]) / pivot_df[col_1]
    change_columns.append(change_col)

for i in range(len(e) - 1 ):
    col_1 = e[i]
    col_2 = e[i + 1]
    change_col = f"{col_2}_{col_1}_chg"
    pivot_df[change_col] =  (pivot_df[col_2] - pivot_df[col_1]) / pivot_df[col_1]
    change_columns.append(change_col)


#pivot_df.to_csv('data/pivot_df.csv')
# Reset index to flatten the DataFrame
result_df = pivot_df.reset_index()


# Select only the 'change' columns along with identifiers
change_columns = [col for col in result_df.columns if "_chg" in str(col)]
subset_df = result_df[['subjid', 'ficat', 'fitest', 'fiperiod'] + change_columns]
#subset_df.to_csv('data/subset_df.csv')

# Rename the change columns to remove "change_"
rename_mapping = {col: col.replace("_chg", "") for col in change_columns}
subset_df = subset_df.rename(columns=rename_mapping)

# Melting

y= subset_df.melt(id_vars=['subjid', 'ficat','fitest', 'fiperiod'], var_name='afidtc', value_name='chg')
x=y.dropna()

# separate one column into 2columns
# Split the column into two new columns
x[['fidtc', 'fidtc0']] = x['afidtc'].str.split('_', expand=True)


w=z.dropna()
v = pd.merge(w,x,on=['subjid', 'ficat', 'fitest','fidtc', 'fiperiod'], how='left')
v = v.drop("fidtc0", axis='columns')

v.sort_values(by=['subjid', 'ficat','fitest'])
#v.to_csv('data/v.csv')
# adding all the info toguether

t = pd.merge(z1,v,on=['subjid', 'ficat', 'fitest','fidtc', 'fiperiod', 'fiorres'], how='left')



# -------------------------------------- creating the adfi dataset: Analysis DAtaset for FInancials
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
t.to_sql('qadfi', con=engine, if_exists='replace', index=False, schema='ru')
