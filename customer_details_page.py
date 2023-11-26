import mysql.connector

# Function to connect to MySQL database
def connect_to_database():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Shreya@2003",
        database="InteriorDB"
    )

# Function to get customer details by ID using a stored procedure
def get_customer_details_by_id(customer_id):
    connection = connect_to_database()
    cursor = connection.cursor()

    try:
        # Call the stored procedure
        cursor.callproc('GetCustomerDetailsByID', [customer_id])

        # Fetch the result
        result = []
        for result in cursor.stored_results():
            result = result.fetchall()
        return result

    finally:
        cursor.close()
        connection.close()
