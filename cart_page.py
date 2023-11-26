# cart_page.py
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

# Function to fetch unique cart IDs from the database
def get_cart_ids():
    connection = connect_to_database()
    cursor = connection.cursor()
    cursor.execute("SELECT DISTINCT Cart_id FROM interiordb.cart_item")
    cart_ids = [row[0] for row in cursor.fetchall()]
    connection.close()
    return cart_ids

# Function to fetch cart items based on the selected cart ID
def get_cart_items(selected_cart_id):
    connection = connect_to_database()
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM interiordb.cart_item WHERE Cart_id = '{selected_cart_id}'")
    cart_items = cursor.fetchall()
    connection.close()
    return cart_items

# Function to update the quantity of a product in the cart
def update_quantity(cart_id, product_id, new_quantity):
    connection = connect_to_database()
    cursor = connection.cursor()
    cursor.execute(f"UPDATE interiordb.cart_item SET Quantity_wished = {new_quantity} WHERE Cart_id = '{cart_id}' AND Product_id = {product_id}")
    connection.commit()
    connection.close()

# Function to remove a product from the cart
def remove_product(cart_id, product_id):
    connection = connect_to_database()
    cursor = connection.cursor()
    cursor.execute(f"DELETE FROM interiordb.cart_item WHERE Cart_id = '{cart_id}' AND Product_id = {product_id}")
    connection.commit()
    connection.close()

# Function to display the Cart page
def cart_page():
    st.title("Cart Page")

    # Display unique cart IDs in a dropdown
    cart_ids = get_cart_ids()
    selected_cart_id = st.selectbox("Select Cart ID:", cart_ids)

    # Display cart items based on the selected cart ID
    cart_items = get_cart_items(selected_cart_id)
    if cart_items:
        st.write(f"## Cart Contents for Cart ID: {selected_cart_id}")

        # Display cart items in a table
        st.table(cart_items)

        # Update Quantity Form
        st.subheader("Update Quantity")
        product_to_update = st.selectbox("Select Product to Update:", [f"{item[3]} - {item[0]}" for item in cart_items])
        new_quantity = st.number_input("Enter New Quantity:", min_value=1, value=1)
        if st.button("Update Quantity"):
            product_id_to_update = int(product_to_update.split(" - ")[1])
            update_quantity(selected_cart_id, product_id_to_update, new_quantity)
            st.success(f"Quantity updated for Product ID {product_id_to_update} in Cart ID {selected_cart_id}.")

        # Remove Product Form
        st.subheader("Remove Product")
        product_to_remove = st.selectbox("Select Product to Remove:", [f"{item[3]} - {item[0]}" for item in cart_items])
        if st.button("Remove Product"):
            product_id_to_remove = int(product_to_remove.split(" - ")[1])
            remove_product(selected_cart_id, product_id_to_remove)
            st.success(f"Product removed with Product ID {product_id_to_remove} from Cart ID {selected_cart_id}.")
    else:
        st.write(f"No items found for Cart ID: {selected_cart_id}")

# Save this file as "cart_page.py"
