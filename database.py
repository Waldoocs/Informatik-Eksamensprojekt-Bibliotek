import mysql.connector

# Function to establish connection to MySQL database
def connect_to_database():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="bibliotek"
    )

# Function to create the "Books" table if it doesn't exist
def create_books_table():
    connection = None
    try:
        connection = connect_to_database()
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Books (
                id INT AUTO_INCREMENT PRIMARY KEY,
                title VARCHAR(255),
                author VARCHAR(255),
                genre VARCHAR(255)
            )
        """)
        connection.commit()
        print("Books table created successfully")
    except mysql.connector.Error as e:
        print("Error creating Books table:", e)
    finally:
        if connection is not None and connection.is_connected():
            cursor.close()
            connection.close()

# Function to insert sample data into the "Books" table
def insert_sample_data():
    connection = None
    try:
        connection = connect_to_database()
        cursor = connection.cursor()
        # Example books data
        books_data = [
            ("The Great Gatsby", "F. Scott Fitzgerald", "Fiction"),
            ("To Kill a Mockingbird", "Harper Lee", "Fiction"),
            ("1984", "George Orwell", "Dystopian"),
            ("Pride and Prejudice", "Jane Austen", "Romance"),
            ("The Catcher in the Rye", "J.D. Salinger", "Coming-of-age"),
            ("Harry Potter and the Philosopher's Stone", "J.K. Rowling", "Fantasy")
        ]
        # Insert each book into the table
        for book in books_data:
            cursor.execute("INSERT INTO Books (title, author, genre) VALUES (%s, %s, %s)", book)
        connection.commit()
        print("Sample data inserted successfully")
    except mysql.connector.Error as e:
        print("Error inserting sample data:", e)
    finally:
        if connection is not None and connection.is_connected():
            cursor.close()
            connection.close()

# Call the function to insert sample data
insert_sample_data()


# Function to fetch data from the "Books" table
def fetch_data():
    connection = None
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

# Call the function to create the Books table if it doesn't exist
create_books_table()
