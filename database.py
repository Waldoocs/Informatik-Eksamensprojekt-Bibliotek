import mysql.connector

# Function to establish connection to MySQL database
def connect_to_database():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="bibliotek"
    )

# Function to fetch data from the "Books" table
def fetch_data():
    connection = None  # Initialize connection variable
    try:
        connection = connect_to_database()
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM Books")
            rows = cursor.fetchall()
            return rows
    except mysql.connector.Error as e:
        print("Error while fetching data from Books table:", e)
    finally:
        if connection is not None and connection.is_connected():
            cursor.close()
            connection.close()
