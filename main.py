import pandas as pd
import sqlite3
import os, time

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

# print statement will execute if you are able to connect to DB and is used for testing the connectivity
print("Connected to the database")

# Write your SQL queries
'''
#Outputs the full table
full_table_query = """
Select * From Listings
"""
'''
def get_full_table(sqliteConnection):
    full_table_query = """
    SELECT * FROM Listings;
    """
    try:
        full_table = pd.read_sql_query(full_table_query, sqliteConnection)
        return full_table
    except sqlite3.Error as e:
        print(f"Error executing full table query: {e}")
        return []
def get_most_reviews(sqliteConnection):
    most_reviews_query = """
SELECT name,  neighbourhood, number_of_reviews, price
FROM listings
WHERE number_of_reviews IS NOT NULL
ORDER BY number_of_reviews DESC
LIMIT 10;
"""
    try:
        most_reviews = pd.read_sql_query(most_reviews_query, sqliteConnection)
        return most_reviews
    except sqlite3.Error as e:
        print(f"Error executing full table query: {e}")
        return []
def get_most_expensive(sqliteConnection):
    most_expensive_query = """
    SELECT name, host_name, number_of_reviews, price
FROM listings
WHERE price IS NOT NULL
ORDER BY CAST(price AS REAL) DESC
LIMIT 10;
"""
    try:
        most_expensive = pd.read_sql_query(most_expensive_query, sqliteConnection)
        return most_expensive
    except sqlite3.Error as e:
        print(f"Error executing full table query: {e}")
        return []

def get_cheapest(sqliteConnection):
    cheapest_query = """
    SELECT name, host_name, number_of_reviews, price
    FROM listings
    WHERE price IS NOT NULL and TRIM(price) != ''
    ORDER BY CAST(price AS REAL) ASC
    LIMIT 10;
    """
    try:
        cheapest = pd.read_sql_query(cheapest_query, sqliteConnection)
        return cheapest
    except sqlite3.Error as e:
        print(f"Error executing cheapest query: {e}")
        return []


def get_total_listings(sqliteConnection):
    total_query = """
    SELECT COUNT(*) FROM listings;
    """
    try:
        total = pd.read_sql_query(total_query, sqliteConnection)
        return total
    except sqlite3.Error as e:
        print(f"Error executing total listings query: {e}")
        return []


def get_listing_count_per_neighborhood(sqliteConnection):
    listing_count_per_neighborhood_query = """
    SELECT neighbourhood, COUNT(*) AS count
    FROM listings
    GROUP BY neighbourhood
    ORDER BY count DESC; 
    """
    try:
        result = pd.read_sql_query(listing_count_per_neighborhood_query, sqliteConnection)
        return result
    except sqlite3.Error as e:
        print(f"Error executing listing count query: {e}")
        return []


def get_top_room_types(sqliteConnection):
    top_room_types_query = """
    SELECT room_type, COUNT(*) AS count
    From listings
    GROUP BY room_type
    ORDER BY count DESC
    """
    try:
        result = pd.read_sql_query(top_room_types_query, sqliteConnection)
        return result
    except sqlite3.Error as e:
        print(f"Error executing top room types query: {e}")
        return []


def get_avg_price(sqliteConnection):
    avg_price_query = """
    SELECT AVG(price) AS average_price
    FROM listings
    WHERE price IS NOT NULL AND TRIM(price) != ''
    """
    try:
        result = pd.read_sql_query(avg_price_query, sqliteConnection)
        return result
    except sqlite3.Error as e:
        print(f"Error executing average price query: {e}")
        return []


def get_avg_reviews(sqliteConnection):
    avg_reviews_query = """
    SELECT AVG(number_of_reviews) AS average_reviews
    FROM listings
    """
    try:
        result = pd.read_sql_query(avg_reviews_query, sqliteConnection)
        return result
    except sqlite3.Error as e:
        print(f"Error executing average reviews query: {e}")
        return []


def get_most_listings(sqliteConnection):
    most_listings_query = """
    SELECT host_id, host_name, COUNT(*) AS total_listings
    FROM listings
    GROUP BY host_id, host_name
    ORDER BY total_listings DESC
    LIMIT 10;
    """
    try:
        result = pd.read_sql_query(most_listings_query, sqliteConnection)
        return result
    except sqlite3.Error as e:
        print(f"Error executing most listings query: {e}")
        return []


def get_price_per_host(sqliteConnection):
    price_per_host_query = """
    SELECT host_id, host_name, ROUND(AVG(price), 2) as average_price
    FROM listings
    WHERE price IS NOT NULL AND TRIM(price) != ''
    GROUP BY host_id, host_name
    ORDER BY average_price ASC
    LIMIT 10
    """
    try:
        result = pd.read_sql_query(price_per_host_query, sqliteConnection)
        return result
    except sqlite3.Error as e:
        print(f"Error executing price per host query: {e}")
        return []



# Run the query and load the result into a DataFrame
'''
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
'''
#print(get_full_table(sqliteConnection))

####PRINT STATEMENTS FOR TESTING WHEN CREATING NEW SQL QUERIES ######

def display_menu():
    print("Welcome to Lee's AirBNB Data Analysis Application!")

    while True:
        print("\n--- Let's Get Some Nashville Data! Yeehaw!! ---")
        print("1. Print Full Table")
        print("2. Show Top 10 Listings by Most Reviews")
        print("3. Show Top 10 Most Expensive Listings")
        print("4. Show Top 10 Cheapest Listings")
        print("5. Show Total Number of Listings")
        print("6. Show Listing Count per Neighborhood")
        print("7. Show Top Room Types")
        print("8. Show Average Price")
        print("9. Show Average Reviews")
        print("10. Show Top 10 Hosts with Most Listings")
        print("11. Show Top 10 Cheapest Hosts by Avg Price")
        print("0. Exit")

        choice = input("Select an option (0–11): ").strip()
        os.system('clear')
        choice_lower = choice.lower()

        if choice == '1':
            print("Full Table Below")
            print()
            print(get_full_table(sqliteConnection))
            time.sleep(5) #Uncomment after testing
        elif choice == '2' or choice_lower in ['most_reviews', 'most reviews']:
            print(get_most_reviews(sqliteConnection))
            time.sleep(5) #Uncomment after testing

        elif choice == '3' or choice_lower in ['most_expensive', 'expensive']:
            print(get_most_expensive(sqliteConnection))
            time.sleep(5)

        elif choice == '4' or choice_lower in ['cheapest']:
            print(get_cheapest(sqliteConnection))
            time.sleep(5)

        elif choice == '5' or choice_lower in ['total', 'count']:
            print(get_total_listings(sqliteConnection).iloc[0, 0]) #Prints 1st thing in Dataframe which in this case is the count 
            time.sleep(5)

        elif choice == '6' or choice_lower in ['listing_count', 'neighborhoods']:
            print(get_listing_count_per_neighborhood(sqliteConnection))
            time.sleep(5)

        elif choice == '7' or choice_lower in ['room_types']:
            print(get_top_room_types(sqliteConnection))
            time.sleep(5)

        elif choice == '8' or choice_lower in ['avg_price', 'average price']:
            avg_price = get_avg_price(sqliteConnection)
            print("Average Price:", round(avg_price['average_price'][0], 2)) #Gets only the average price and does not output the 0 for it being the first dataframe
            time.sleep(5)

        elif choice == '9' or choice_lower in ['avg_reviews', 'average reviews']:
            avg_reviews = get_avg_reviews(sqliteConnection)
            print("Average Reviews:", round(avg_reviews['average_reviews'][0], 2)) #Gets only the average reviews number and does not output the 0 for it being the first dataframe
            time.sleep(5)

        elif choice == '10' or choice_lower in ['most_listings']:
            print(get_most_listings(sqliteConnection).to_string(index=False)) #Removes the count on the side for each dataframe
            time.sleep(5)

        elif choice == '11' or choice_lower in ['cheapest_hosts']:
            print(get_price_per_host(sqliteConnection))
            time.sleep(5)

        elif choice == '0' or choice_lower == 'exit':
            print("Exiting the program.")
            break

        else:
            print("❌ Invalid selection. Please try again.")

# Main function to execute the program
def main():
    display_menu()

#Executes the program
if __name__ == "__main__":
    main()

# close the connection to the database
sqliteConnection.close()

