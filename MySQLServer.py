import mysql.connector

def create_database(connection):
    cursor = connection.cursor()
    try:
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()

def main():
    # Connection configuration
    config = {
        'user': 'root',
        'password': 'your_password',  # Replace 'your_password' with your MySQL password
        'host': 'localhost'
    }

    try:
        # Establishing a connection to the MySQL server
        connection = mysql.connector.connect(**config)
        if connection.is_connected():
            create_database(connection)
    except mysql.connector.Error as err:
        print("Error while connecting to MySQL:", err)
    finally:
        # Closing the connection
        if connection and connection.is_connected():
            connection.close()
            print("MySQL connection is closed")

if __name__ == "__main__":
    main()
