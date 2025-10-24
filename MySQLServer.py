import mysql.connector
from mysql.connector import Error

# Define MySQL server connection parameters
host = "localhost"
user = "your_mysql_username"       
password = "your_mysql_password"   

try:
    # Connect to MySQL server (no database specified yet)
    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password
    )

    # Check if connection was successful
    if connection.is_connected():
        cursor = connection.cursor()
        
        # Create database if it doesn't already exist
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("DB database `alx_book_store` created successfully!")

except mysql.connector.Error as e:
    # Handle any errors during connection or execution
    print(f"Error while connecting to MySQL: {e}")

finally:
    # Ensure resources are cleaned up properly
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed.")