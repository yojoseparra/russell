
# connecting to postgreSQL
exec(open('connect2sql.py').read())
import pandas as pd
# Query the database and load directly into a DataFrame
b = pd.read_sql_query( "SELECT * from ru.sc", conn)
conn.close()

# -------------------------------------------------------
# prepering file for upload
c = pd.read_csv("data/fitest_merged2.csv")

c['sctest0'] = c['sctest'].apply(lambda x: x[0].upper() + x[1:] if x else x)



import string
import re
def split_on_caps(s):
    # Use regex to split on the transition between lowercase to uppercase
    return re.sub(r'([a-z])([A-Z])', r'\1 \2', s)

c.loc[:,'sctestcd'] = c['sctest0'].apply(split_on_caps)



c['text'] = c['scgrp'] + " - " + c['sccat'] + " - " + c['sctestcd'] 

#---------------------------------------------creating sc dataset
from sqlalchemy import create_engine
from urllib.parse import quote_plus


# Connection string
connection_string = f'postgresql+psycopg2://{username}:{escaped_password}@{host}/{database}'
engine = create_engine(connection_string)

c.to_sql('sc', con=engine, if_exists='replace', index=False, schema='ru')

