# seller_login_page.py
import streamlit as st
import mysql.connector

def seller_login_page():
    st.title("Seller Login")

    # Use st.form to improve user experience
    with st.form(key='seller_login_form'):
        # Get user input
        seller_id = st.text_input("Seller ID")
        password = st.text_input("Password", type="password")
        st.session_state.seller_id = seller_id

        # Dummy login check (you should check against your database)
        if st.form_submit_button("Login"):
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Shreya@2003",
                database="InteriorDB"
            )
            cursor = connection.cursor()

            # Call the stored procedure for seller login
            cursor.callproc("seller_login_procedure", (seller_id, password))

            # Get the result of the procedure
            result = cursor.fetchone()[0]

            if result == 'Login successful':
                st.success(result)
            else:
                st.error(result)

            connection.close()

# Run the app
if __name__ == "__main__":
    seller_login_page()
