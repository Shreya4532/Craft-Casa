# update_price_page.py
import streamlit as st
import mysql.connector

def connect_to_database():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Shreya@2003",
        database="InteriorDB"
    )

def update_product_price(product_id, new_price):
    connection = connect_to_database()
    cursor = connection.cursor()

    try:
        # Update the product price
        cursor.execute("UPDATE Product SET Price = %s WHERE ProductID = %s", (new_price, product_id))
        connection.commit()

        # Display success message
        st.success(f"Price for ProductID {product_id} updated successfully to {new_price}")

        # Trigger the update for affected carts
        # You may need to adjust the import based on your project structure
        from trigger_page import update_total_price_trigger
        update_total_price_trigger()

    except mysql.connector.Error as err:
        st.error(f"Error: {err}")

    finally:
        cursor.close()
        connection.close()

def update_price_page():
    st.title("Update Product Price")

    # Use st.form to improve user experience
    with st.form(key='update_price_form'):
        product_id = st.text_input("Product ID")
        new_price = st.number_input("New Price")

        if st.form_submit_button("Update Price"):
            # Call the function to update product price
            update_product_price(product_id, new_price)

# Uncomment the line below if you want to run this script independently
# update_price_page()
