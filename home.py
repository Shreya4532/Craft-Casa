# home.py
import streamlit as st
from login_page import login_page
from seller_login_page import seller_login_page
from product_page import product_page
from cart_page import cart_page
from cart_details_page import cart_details_page
from intro import intro_page
from trigger_page import update_total_price_trigger
from update_price_page import update_price_page
from average_earnings_page import average_earnings_page
from add_product import add_product_page
from filter_by_seller import filter_by_seller_page
from add_seller_page import add_seller_page
from seller_sales_page import seller_sales_page  # Import the new page

def main():
    # Call set_page_config only once at the beginning of your script
    st.set_page_config(
        page_title="Craft-Casa",
        page_icon="👋",
    )

    st.sidebar.success("InteriorDB-options.")
    
    # Add a sidebar selectbox for page navigation
    selected_page = st.sidebar.selectbox(
        "Select a page:",
        ["Introduction", "Login Page", "Product Page", "Cart Page", "Cart Details Page", "New Customer Page", "Trigger Page", "Update Product Price", "Average Seller Earnings", "Add New Product", "Filter by Seller", "Add Seller", "Seller Sales Page"]
    )

    # Display the selected page based on user choice
    if selected_page == "Introduction":
        intro_page()  # Display the intro page
    elif selected_page == "Login Page":
        login_page()
    elif selected_page == "Product Page":
        product_page()
    elif selected_page == "Cart Page":
        cart_page()
    elif selected_page == "Cart Details Page":
        cart_details_page()
    elif selected_page == "New Customer Page":
        # Add your logic for the new customer page
        pass
    elif selected_page == "Trigger Page":
        update_total_price_trigger()  # Display the trigger page
    elif selected_page == "Update Product Price":
        update_price_page()  # Display the update price page
    elif selected_page == "Average Seller Earnings":
        average_earnings_page()  # Display the average earnings page
    elif selected_page == "Add New Product":
        add_product_page()  # Display the add product page
    elif selected_page == "Filter by Seller":
        filter_by_seller_page()  # Display the filter by seller page
    elif selected_page == "Add Seller":
        add_seller_page()  # Display the add seller page
    elif selected_page == "Seller Sales Page":
        seller_sales_page()  # Display the seller sales page

# Run the app
if __name__ == "__main__":
    main()
