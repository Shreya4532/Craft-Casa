# trigger_page.py
import streamlit as st
import mysql.connector

def update_total_price_trigger():
    st.title("Update Total Price Trigger")

    # Use st.form to improve user experience
    with st.form(key='update_trigger_form'):
        cart_id = st.text_input("Cart ID")
        product_name = st.text_input("Product Name")
        quantity_wished = st.number_input("Quantity Wished", min_value=1, step=1)

        if st.form_submit_button("Update Total Price"):
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Shreya@2003",
                database="InteriorDB"
            )
            cursor = connection.cursor()

            try:
                # Insert a new cart item with the current timestamp for 'Date_Added'
                cursor.execute("""
                    INSERT INTO interiordb.cart_item (Cart_id, Product_id, Quantity_wished, Date_Added)
                    VALUES (%s, (SELECT ProductID FROM interiordb.product WHERE Name = %s LIMIT 1), %s, NOW())
                """, (cart_id, product_name, quantity_wished))

                connection.commit()

                # Remove duplicates based on Cart_id and Product_id
                cursor.execute("""
                    DELETE n1 FROM interiordb.cart_item n1, interiordb.cart_item n2
                    WHERE n1.Cart_id = n2.Cart_id
                    AND n1.Product_id = n2.Product_id
                    AND n1.Date_Added > n2.Date_Added;
                """)
                connection.commit()

                # Fetch any remaining results to avoid "Unread result found"
                cursor.fetchall()

                # Display success message
                st.success("Cart item added successfully!")

                # Trigger the update
                cursor.execute("SELECT * FROM interiordb.cart_item WHERE Cart_id = %s", (cart_id,))
                new_item = cursor.fetchone()

                cursor.execute("""
                    UPDATE interiordb.cart
                    SET Total_price = Total_price + (%s * (
                        SELECT Price FROM interiordb.product
                        WHERE ProductID = %s
                    ))
                    WHERE Cart_id = %s;
                """, (new_item[2], new_item[1], cart_id))

                connection.commit()

                # Display success message for trigger
                st.success("Total price in the cart updated!")

            except mysql.connector.Error as err:
                st.error(f"Error: {err}")

# Run the app
if __name__ == "__main__":
    update_total_price_trigger()
