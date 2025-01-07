import os
import csv
import pandas
import xlrd 



# Uploading file
import psycopg2
try:
    # connecting to postgreSQL
    exec(open('connect2sql.py').read())
    cursor= conn.cursor()

    # Open the CSV file
    with open('data/z.csv', 'r', encoding='utf-8') as f:
        csv_reader = csv.reader(f)
        next(csv_reader)  # Skip the header row
        

        # Insert each row into the PostgreSQL table
        for row in csv_reader:
            cursor.execute(
                "INSERT INTO ru.qfi ( domain,	ficat,	subjid,	fitest,	fiorres,	fiorresu,	fidtc, fiperiod ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
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







