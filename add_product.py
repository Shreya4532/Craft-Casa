import mysql.connector
import streamlit as st

def connect_to_database():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Shreya@2003",
        database="InteriorDB"
    )

def add_product_page():
    st.title("Add New Product")

    seller_id = st.text_input("Seller ID", max_chars=6)
    product_name = st.text_input("Product Name")
    category = st.text_input("Category")
    color = st.text_input("Color")
    size = st.text_input("Size")
    price = st.number_input("Price", min_value=0.0)

    if st.button("Add Product"):
        connection = connect_to_database()
        cursor = connection.cursor()

        try:
            # Insert the new product into the Product table
            query = """
                INSERT INTO Product (Name,  Color, Size, Price, Seller_id)
                VALUES (%s, %s, %s, %s, %s);
            """
            cursor.execute(query, (product_name, color, size, price, seller_id))
            connection.commit()

            st.success("Product added successfully!")

        except mysql.connector.Error as err:
            st.error(f"Error: {err}")

        finally:
            cursor.close()
            connection.close()

# Uncomment the line below if you want to run this script independently
# add_product_page()
