import mysql.connector
import streamlit as st

def connect_to_database():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Shreya@2003",
        database="InteriorDB"
    )

def average_earnings_page():
    st.title("Seller Earnings")

    # Create a dropdown to choose between total and average earnings
    earnings_type = st.selectbox("Select Earnings Type:", ["Total", "Average"])

    connection = connect_to_database()
    cursor = connection.cursor(dictionary=True)

    try:
        # SQL query to calculate total or average earnings for each seller
        if earnings_type == "Total":
            query = """
                SELECT s.Seller_id, s.Name AS Seller_Name, SUM(ci.Quantity_wished * p.Price) AS Total_Earnings
                FROM Seller s
                LEFT JOIN Product p ON s.Seller_id = p.Seller_id
                LEFT JOIN Cart_item ci ON p.ProductID = ci.Product_id
                GROUP BY s.Seller_id, s.Name;
            """
        elif earnings_type == "Average":
            query = """
                SELECT s.Seller_id, s.Name AS Seller_Name, AVG(ci.Quantity_wished * p.Price) AS Average_Earnings
                FROM Seller s
                LEFT JOIN Product p ON s.Seller_id = p.Seller_id
                LEFT JOIN Cart_item ci ON p.ProductID = ci.Product_id
                GROUP BY s.Seller_id, s.Name;
            """
        else:
            st.error("Invalid earnings type selected.")

        cursor.execute(query)
        results = cursor.fetchall()

        # Display the results
        st.table(results)

    except mysql.connector.Error as err:
        st.error(f"Error: {err}")

    finally:
        cursor.close()
        connection.close()

# Uncomment the line below if you want to run this script independently
# average_earnings_page()
