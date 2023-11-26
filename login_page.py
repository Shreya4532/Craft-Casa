# login_page.py
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

# Function to call the stored procedure to add a new customer
def add_new_customer(username, password, name, address, pincode, phone_number):
    connection = connect_to_database()
    cursor = connection.cursor()

    # Call the stored procedure
    cursor.execute("INSERT INTO customer (Customer_id, c_pass, Name, Address, Pincode, Phone_number) values( %s,%s,%s,%s,%s,%s)", (username, password, name, address, pincode, phone_number,))
    connection.commit()
    connection.close()

# Function to display the login page
def login_page():
    st.title("Login Page")

    # Use st.form to improve user experience
    with st.form(key='login_form'):
        # Get user input
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        st.session_state.user = username

        # Dummy login check (you should check against your database)
        if st.form_submit_button("Login"):
            connection = connect_to_database()
            cursor = connection.cursor()

            # Call the stored procedure for login
            cursor.callproc("new_procedure", (username, password))

            # Get the result of the procedure
            result = cursor.fetchone()[0]

            if result == 'Login successful':
                st.success(result)
            else:
                st.error(result)

            connection.close()

    # Display section to add new customers
    st.title("Add New Customer")
    with st.form(key='add_customer_form'):
        new_username = st.text_input("New Username")
        new_password = st.text_input("New Password", type="password")
        name = st.text_input("Name")
        address = st.text_input("Address")
        pincode = st.text_input("Pincode")
        phone_number = st.text_input("Phone Number")

        if st.form_submit_button("Add Customer"):
            # Call the stored procedure to add a new customer
            add_new_customer(new_username, new_password, name, address, pincode, phone_number)

            # Display success message
            st.success("New customer added successfully!")

# Run the app
if __name__ == "__main__":
    login_page()
