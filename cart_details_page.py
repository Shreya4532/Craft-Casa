# cart_details_page.py
import streamlit as st
import mysql.connector

# Function to connect to MySQL database
def connect_to_database():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Shreya@2003",
        database="InteriorDB"
    )

# Function to execute the MySQL query
def get_cart_details(customer_name):
    connection = connect_to_database()
    cursor = connection.cursor(dictionary=True)
    
    query = """
    SELECT P.*
    FROM interiordb.product P
    JOIN interiordb.cart_item CI ON P.ProductID = CI.Product_id
    JOIN interiordb.cart C ON CI.Cart_id = C.Cart_id
    JOIN interiordb.customer Cu ON C.Cart_id = Cu.Cart_id
    WHERE Cu.Name = %s
      AND CI.purchased = 'NO';
    """
    
    cursor.execute(query, (customer_name,))
    cart_details = cursor.fetchall()
    
    connection.close()
    return cart_details

# Function to display the Cart Details page
def cart_details_page():
    st.title("Cart Details Page")

    # Get customer name from user input
    customer_name = st.text_input("Enter Customer Name:")
    
    if st.button("Fetch Cart Details"):
        # Execute the MySQL query and get cart details
        cart_details = get_cart_details(customer_name)

        # Display the results
        if cart_details:
            st.write("## Cart Details:")
            for item in cart_details:
                st.write(f"- Product ID: {item['ProductID']}, Name: {item['Name']}, Type: {item['Type']}, Color: {item['Color']}, Size: {item['Size']}, Price: {item['Price']}")
        else:
            st.write("No items found in the cart for the specified customer.")

# Run the app
if __name__ == "__main__":
    cart_details_page()
