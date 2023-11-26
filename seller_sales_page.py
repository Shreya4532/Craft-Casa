# seller_sales_page.py
import streamlit as st
import mysql.connector

def fetch_seller_sales(seller_id):
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Shreya@2003",
        database="InteriorDB"
    )
    cursor = connection.cursor(dictionary=True)

    try:
        query = """
            SELECT CI.Quantity_wished, CI.Date_Added, P.Name AS Product_Name
            FROM Cart_item CI
            INNER JOIN Product P ON CI.Product_id = P.ProductID
            WHERE P.Seller_id = %s AND CI.purchased = 'YES';
        """

        cursor.execute(query, (seller_id,))
        results = cursor.fetchall()

        # Display the results in a table
        if results:
            st.write("## Seller Sales Information:")
            sales_table = {"Quantity": [], "Date Added": [], "Product Name": []}

            for item in results:
                sales_table["Quantity"].append(item['Quantity_wished'])
                sales_table["Date Added"].append(item['Date_Added'])
                sales_table["Product Name"].append(item['Product_Name'])

            st.table(sales_table)
        else:
            st.write("No sales information found for the specified seller.")

    except mysql.connector.Error as err:
        st.error(f"Error: {err}")

    finally:
        cursor.close()
        connection.close()

def seller_sales_page():
    st.title("Seller Sales Page")

    # Get seller ID from user input
    seller_id = st.text_input("Enter Seller ID:")

    if st.button("Fetch Seller Sales"):
        fetch_seller_sales(seller_id)

# Run the app
if __name__ == "__main__":
    seller_sales_page()
