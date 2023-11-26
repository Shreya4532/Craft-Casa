import streamlit as st
import mysql.connector

def query_product_info(product_name):
    # Connect to the MySQL database
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Shreya@2003",
        database="interiordb"
    )

    # Create a cursor object to execute SQL queries
    cursor = connection.cursor()

    # Construct the SQL query
    query = """
        SELECT
            c.Name AS CustomerName,
            s.Name AS SellerName,
            p.Name AS ProductName,
            t.TransactionDate
        FROM
            customer c
            JOIN transaction t ON c.Customer_id = t.Customer_id
            JOIN product p ON t.Product_id = p.ProductID
            JOIN seller s ON p.Seller_id = s.Seller_id
        WHERE
            p.Name = %s
    """

    # Execute the query with the provided product name
    cursor.execute(query, (product_name,))

    # Fetch all the rows
    result = cursor.fetchall()

    # Close the cursor and connection
    cursor.close()
    connection.close()

    return result

def main():
    # Connect to the MySQL database
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="interiordb"
    )

    # Create a cursor object to execute SQL queries
    cursor = connection.cursor()

    # Query all product names
    cursor.execute("SELECT Name FROM product")
    product_names = [row[0] for row in cursor.fetchall()]

    # Close the cursor and connection
    cursor.close()
    connection.close()

    # Streamlit app
    st.title("Product Information Query")

    # Dropdown for selecting a product
    selected_product = st.selectbox("Select a product:", product_names)

    if st.button("Query Information"):
        # Get information for the selected product
        result = query_product_info(selected_product)

        # Display the results
        st.subheader("Product Information:")
        for row in result:
            st.text(f"Customer Name: {row[0]}")
            st.text(f"Seller Name: {row[1]}")
            st.text(f"Product Name: {row[2]}")
            st.text(f"Transaction Date: {row[3]}")
            st.text("---")

if __name__ == "__main__":
    main()
