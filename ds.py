# Subject Disposition DS
import pandas as pd
import psycopg2
import sqlalchemy


d = pd.read_csv("data/profile1.csv")


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
d.to_sql('ds', con=engine, if_exists='replace', index=False, schema='ru')
