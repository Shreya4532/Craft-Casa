# product_page.py
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

# Function to fetch product data from the database
def get_product_data():
    connection = connect_to_database()
    cursor = connection.cursor()
    cursor.execute("SELECT ProductID, Name FROM Product")
    data = cursor.fetchall()
    connection.close()
    return data

# Function to display the Product page
def product_page():
    # Initialize st.session_state.user if not already initialized
    if 'user' not in st.session_state:
        st.session_state.user = None

    st.title("Choose Your Product")  # Change the title here

    # Use st.form to encapsulate input fields and button
    with st.form(key='product_form'):
        # Fetch product data from the database
        product_data = get_product_data()

        # Display product dropdown
        selected_product = st.selectbox("Select a product:", product_data, format_func=lambda x: x[1])

        # Display quantity input
        quantity = st.number_input("Quantity", min_value=1, value=1)

        # Display add to cart button
        if st.form_submit_button("Add to Cart"):
            # Store selected product in session state
            if 'cart' not in st.session_state:
                st.session_state.cart = []
            st.session_state.cart.append({"product": selected_product[1], "quantity": quantity})
            st.success(f"Added {quantity} units of {selected_product[1]} to the cart!")
