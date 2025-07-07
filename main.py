import pandas as pd
import sqlite3

#print("test")
# https://www.geeksforgeeks.org/python/sql-using-python/
# https://www.sqlitetutorial.net/sqlite-import-csv/

# To Open IMPORT CSV in console to the database: sqlite3 NashvilleAirBNB.db #Example would be sqlite3 AnyDBNameToCreate
# then .mode csv #If the file is a csv
# then import listings.csv listings       #import filename tablename

#Can eventually make this a parameter so you can just select Nashville for city and it will pull that db if we have a list of dbs

sqliteConnection = sqlite3.connect('NashvilleAirBNB.db')

# cursor
crsr = sqliteConnection.cursor()

# print statement will execute if you are able to connect to DB
print("Connected to the database")

# Write your SQL queries

full_table_query = """
Select * From Listings
"""

most_reviews_query = """
SELECT name,  neighbourhood, number_of_reviews, price
FROM listings
WHERE number_of_reviews IS NOT NULL
ORDER BY number_of_reviews DESC
LIMIT 10;
"""

most_expensive_query = """
SELECT name, host_name, number_of_reviews, price
FROM listings
WHERE price IS NOT NULL
ORDER BY CAST(price AS REAL) DESC
LIMIT 10;
"""

cheapest_query = """
SELECT name, host_name, number_of_reviews, price
FROM listings
WHERE price IS NOT NULL and TRIM(price) != ''
ORDER BY CAST(price AS REAL) ASC
LIMIT 10;
"""

###Write a lot more queries below this line for SQL practice


# Run the query and load the result into a DataFrame
most_reviews = pd.read_sql_query(most_reviews_query, sqliteConnection) 
most_expensive = pd.read_sql_query(most_expensive_query, sqliteConnection) 
full_table = pd.read_sql_query(full_table_query, sqliteConnection)
cheapest = pd.read_sql_query(cheapest_query,sqliteConnection)
# close the connection
sqliteConnection.close()

#print(full_table)
#print(most_reviews) #Prints the query for most expensive
#print(most_expensive) #Prints the query for most expensive
#print(cheapest)
