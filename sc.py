

conn = psycopg2.connect( dbname="",user="",password="",host="localhost",port="5432")
# Query the database and load directly into a DataFrame
b = pd.read_sql_query(
    "SELECT * from ru.sc"
    , conn)
conn.close()

import string
import re
def split_on_caps(s):
    # Use regex to split on the transition between lowercase to uppercase
    return re.sub(r'([a-z])([A-Z])', r'\1 \2', s)

b.loc[:,'sctestcd'] = b['sctest'].apply(split_on_caps)
b['text'] = b['sccat'] + " - " + b['scscat'] + " - " + b['sctestcd'] 

#---------------------------------------------creating sc dataset
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

b.to_sql('sc', con=engine, if_exists='replace', index=False, schema='ru')

