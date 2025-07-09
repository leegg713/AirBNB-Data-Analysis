import pandas as pd
import sqlite3

#Putting all the original SQL Queries I made without them being functions here#
#Will use this to test when creating new queries as well

sqliteConnection = sqlite3.connect('NashvilleAirBNB.db')

# cursor
crsr = sqliteConnection.cursor()

# print statement will execute if you are able to connect to DB and is used for testing the connectivity
print("Connected to the database")

# Write your SQL queries

full_table_query = """
Select * From Listings
"""

#Gets 10 most amount of reviews AirBNBs
most_reviews_query = """
SELECT name,  neighbourhood, number_of_reviews, price
FROM listings
WHERE number_of_reviews IS NOT NULL
ORDER BY number_of_reviews DESC
LIMIT 10;
"""
#Gets 10 most expensive AirBNBs
most_expensive_query = """
SELECT name, host_name, number_of_reviews, price
FROM listings
WHERE price IS NOT NULL
ORDER BY CAST(price AS REAL) DESC
LIMIT 10;
"""
#Gets cheapest 10 AirBNBs
cheapest_query = """
SELECT name, host_name, number_of_reviews, price
FROM listings
WHERE price IS NOT NULL and TRIM(price) != ''
ORDER BY CAST(price AS REAL) ASC
LIMIT 10;
"""
#Gets total amount of listings
total_query = """
SELECT COUNT(*) FROM listings;


"""
#Gets count of listings per neighborhood
listing_count_per_neighborhood_query = """
SELECT neighbourhood, COUNT(*) AS count
FROM listings
GROUP BY neighbourhood
ORDER BY count DESC; 
"""

#Gets the top room types 
top_room_types_query = """
SELECT room_type, COUNT(*) AS count
From listings
GROUP BY room_type
ORDER BY count DESC

"""

#Gets the overall average price and excludes 0's and blanks

avg_price_query = """
SELECT AVG(price) AS average_price
FROM listings
WHERE price IS NOT NULL AND TRIM(price) != ''
"""


#Gets the overall average reviews and includes 0's and blanks in the calculation

avg_reviews_query = """
SELECT AVG(number_of_reviews) AS average_reviews
FROM listings
"""

#Gets the top 10 hosts with the most listings
#host_listings_count is already a column but made this for practice

most_listings_query = """
SELECT host_id, host_name, COUNT(*) AS total_listings
FROM listings
GROUP BY host_id, host_name
ORDER BY total_listings DESC
LIMIT 10;


"""

#Gets the top 10 cheapest average price per host exlcuding hosts that are 0 or null and rounds to 2 decimal places

price_per_host_query = """
SELECT host_id, host_name, ROUND(AVG(price), 2) as average_price
FROM listings
WHERE price IS NOT NULL AND TRIM(price) != ''
GROUP BY host_id, host_name
ORDER BY average_price ASC
LIMIT 10
"""


###Write a lot more queries above this line for SQL practice####



# Run the query and load the result into a DataFrame
most_reviews = pd.read_sql_query(most_reviews_query, sqliteConnection) 
most_expensive = pd.read_sql_query(most_expensive_query, sqliteConnection) 
full_table = pd.read_sql_query(full_table_query, sqliteConnection)
cheapest = pd.read_sql_query(cheapest_query,sqliteConnection)
total = pd.read_sql_query(total_query,sqliteConnection)
listing_count_per_neighborhood = pd.read_sql_query(listing_count_per_neighborhood_query,sqliteConnection)
top_room_types = pd.read_sql_query(top_room_types_query,sqliteConnection)
avg_price = pd.read_sql_query(avg_price_query, sqliteConnection)
avg_reviews = pd.read_sql_query(avg_reviews_query,sqliteConnection)
most_listings= pd.read_sql_query(most_listings_query, sqliteConnection)
price_per_host= pd.read_sql_query(price_per_host_query, sqliteConnection)




#print(full_table)
#print(most_reviews) #Prints the query for most expensive
#print(most_expensive) #Prints the query for most expensive
#print(cheapest) #Prints cheapest
#print(total) #Prints total count of listings
#print(listing_count_per_neighborhood) #Prints total count of listings per neighborhood
#print(top_room_types) #Prints all rooms types
#print(avg_price) #Prints average price of a listing
#print(avg_reviews) #Prints the average reviews for a listing
#print(avg_reviews['average_reviews'][0]) #Prints just the average as the average is the first row in the pandas dataframe
#print(most_listings) #Prints the top 10 hosts with the most listings
#print(price_per_host) #Prints top 10 cheapest average prices for hosts


#QUERIES TO MAKE##

'''

📊 Descriptive / Summary Queries
Count total number of listings - Completed

Find distinct neighborhoods and how many listings are in each - Completed

Identify most common room types - Completed

Average price overall and per room type - Completed

Average number of reviews per listing - Completed

🧑‍💼 Host-Based Queries
Hosts with the most listings - Completed 

Average price per host

Hosts with the highest-rated or most-reviewed listings

🗺️ Location-Based Queries
Most expensive neighborhoods on average

Cheapest neighborhoods on average

Neighborhoods with the most listings

Neighborhoods with highest average availability

🕒 Availability & Activity
Listings with year-round availability

Listings with 0 availability but high reviews (possible inactive hosts)

Listings with high availability but few or no reviews (possibly unpopular or new)

Listings with the highest reviews per month

⚠️ Data Quality / Anomalies
Listings with missing or zero price

Listings with extremely high or low prices (outliers)

Listings with reviews but no availability

Listings with missing host names or neighborhoods

🔍 Filtering by Criteria
Listings under a certain price with high reviews

Private rooms under a price threshold

Entire homes available all year

Listings with at least N reviews

🧮 Aggregates / Comparisons
Min, max, avg price per room type

Compare availability across room types

Top 5 neighborhoods by number of reviews

Compare average reviews between neighborhoods

'''