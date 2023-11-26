# filter_by_seller.py
import mysql.connector
import streamlit as st

def connect_to_database():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Shreya@2003",
        database="InteriorDB"
    )

def filter_by_seller_page():
    st.title("Filter Products by Seller")

    seller_name = st.text_input("Enter Seller Name:")
    if st.button("Filter Products"):
        connection = connect_to_database()
        cursor = connection.cursor(dictionary=True)

        try:
            # SQL query to filter products based on the seller's name
            query = """
                SELECT p.ProductID, p.Name AS Product_Name, p.Color, p.Size, p.Price
                FROM Product p
                JOIN Seller s ON p.Seller_id = s.Seller_id
                WHERE s.Name = %s;
            """
            cursor.execute(query, (seller_name,))
            results = cursor.fetchall()

            # Display the filtered products
            st.title(f"Products Sold by {seller_name}")
            st.table(results)

        except mysql.connector.Error as err:
            st.error(f"Error: {err}")

        finally:
            cursor.close()
            connection.close()

# Uncomment the line below if you want to run this script independently
# filter_by_seller_page()
