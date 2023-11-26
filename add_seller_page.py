# add_seller_page.py
import streamlit as st
import mysql.connector

def add_new_seller(seller_id, password, name, address):
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Shreya@2003",
        database="InteriorDB"
    )
    cursor = connection.cursor()

    # Call the stored procedure to add a new seller
    cursor.execute("INSERT INTO seller (Seller_id, s_pass, Name, Address) VALUES (%s, %s, %s, %s)",
                   (seller_id, password, name, address))
    connection.commit()
    connection.close()

def add_seller_page():
    st.title("Add New Seller")

    # Use st.form to improve user experience
    with st.form(key='add_seller_form'):
        # Changed the order to have "Name" first, then "Password"
        name = st.text_input("Name")
        password = st.text_input("Password", type="password")
        seller_id = st.text_input("Seller ID")
        address = st.text_input("Address")

        if st.form_submit_button("Add Seller"):
            # Call the function to add a new seller
            add_new_seller(seller_id, password, name, address)

            # Display success message
            st.success("New seller added successfully!")

# Run the app
if __name__ == "__main__":
    add_seller_page()
