# Subject Profile PR
import pandas as pd
import psycopg2
import os
wd = os.getcwd()


d = pd.read_csv(wd+"/data/pr.csv")


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






