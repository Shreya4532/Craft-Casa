# intro.py
import streamlit as st
from login_page import login_page
from seller_login_page import seller_login_page  # Import the seller login page function

def intro_page():
    # Set background color to pink
    st.markdown(
        """
        <style>
            body {
                background-color: #FFC0CB;  /* Pink color */
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.title("Welcome to Craft-Casa")
    st.write("Craft-Casa is your destination for all things interior design and decor!")

    st.markdown("---")

    st.header("Choose your role:")
    
    # Link for Customers
    customer_link = st.button("Customer", key="customer_link")

    # Clear the page and display the login form if the "Customer" button is clicked
    if customer_link:
        st.success("You selected Customer. Redirecting...")
        st.empty()  # Clear the page
        login_page()  # Display the login form

    # Link for Sellers
    seller_link = st.button("Seller", key="seller_link")

    # Clear the page and display the appropriate seller form if the "Seller" button is clicked
    if seller_link:
        st.success("You selected Seller. Redirecting...")
        st.empty()  # Clear the page
        seller_login_page()  # Display the seller login form

    st.markdown("---")
    st.write("Explore our platform to discover amazing products and create your dream space!")

# Run the app
if __name__ == "__main__":
    intro_page()
