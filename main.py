import pandas as pd
import sqlite3

#print("test")
# https://www.geeksforgeeks.org/python/sql-using-python/
# https://www.sqlitetutorial.net/sqlite-import-csv/

# To Open IMPORT CSV in console to the database: sqlite3 NashvilleAirBNB.db #Example would be sqlite3 AnyDBNameToCreate
# then .mode csv #If the file is a csv
# then import listings.csv listings       #import filename tablename

sqliteConnection = sqlite3.connect('NashvilleAirBNB.db')

# cursor
crsr = sqliteConnection.cursor()

# print statement will execute if you are able to connect to DB
print("Connected to the database")

# Write your SQL queries
most_reviews_query = """
SELECT name,  neighbourhood, number_of_reviews, price
FROM listings
WHERE number_of_reviews IS NOT NULL
ORDER BY number_of_reviews DESC
LIMIT 10;
"""

###Write a lot more queries below this line for SQL practice


# Run the query and load the result into a DataFrame
#df = pd.read_sql_query(most_reviews_query, sqliteConnection) 


# close the connection
sqliteConnection.close()

print(df) #Prints the query
