import os
import csv
import pandas
import xlrd 




# prepering file for upload
d = pandas.read_csv("C:/Users/USUARIO/projects/python/portfolio/microcap/data/b.csv", index_col=0)
d = d.dropna()
d.to_csv('data/bb.csv', index=False)

# Uploading file
import psycopg2
try:
    conn = psycopg2.connect("dbname=  user= password= host=localhost port=5432" )
    cursor= conn.cursor()

    # Open the CSV file
    with open('data/bb.csv', 'r', encoding='utf-8') as f:
        csv_reader = csv.reader(f)
        next(csv_reader)  # Skip the header row
        

        # Insert each row into the PostgreSQL table
        for row in csv_reader:
            cursor.execute(
                "INSERT INTO portfolio.financials ( domain, ficat, figrpid, subjid, fitest, fiorres, fiorresu, fidtc) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                row
            )

    conn.commit()
    print("Data successfully inserted into the PostgreSQL table.")

except Exception as e:
    print(f"An error occurred: {e}")
finally:
    # Close the database connection
    if cursor:
        cursor.close()
    if conn:
        conn.close()

########## 2 file

# Preparing file for upload 
a = pandas.read_csv("data/a.csv", index_col=0)
#d = a.dropna()
#d.to_csv('data/a.csv')

# Uploading the file
try:
    conn = psycopg2.connect("dbname= user= password= host=localhost port=5432" )
    cursor= conn.cursor()

    # Open the CSV file
    with open('data/a.csv', 'r') as f:
        # Use the copy_expert method to execute COPY command
        cursor.copy_expert("""
            COPY portfolio.financials (domain, ficat, figrpid, subjid, fitest, fiorres, fiorresu, fidtc)
            FROM STDIN
            WITH CSV HEADER
        """, f)
    conn.commit()
    print("Data successfully inserted into the PostgreSQL table.")

except Exception as e:
    print(f"An error occurred: {e}")
finally:
    # Close the database connection
    if cursor:
        cursor.close()
    if conn:
        conn.close()



########## 3 file

# Preparing file for upload 
c = pandas.read_csv("data/c_not_na.csv", index_col=0)
c.to_csv('data/cc.csv', index=False)

# Uploading the file
try:
    conn = psycopg2.connect("dbname=  user= password= host=localhost port=5432" )
    cursor= conn.cursor()

    # Open the CSV file
    with open('data/cc.csv', 'r') as f:
        # Use the copy_expert method to execute COPY command
        cursor.copy_expert("""
            COPY portfolio.financials (domain, ficat, figrpid, subjid, fitest, fiorres, fiorresu, fidtc)
            FROM STDIN
            WITH CSV HEADER
        """, f)
    conn.commit()
    print("Data successfully inserted into the PostgreSQL table.")

except Exception as e:
    print(f"An error occurred: {e}")
finally:
    # Close the database connection
    if cursor:
        cursor.close()
    if conn:
        conn.close()
