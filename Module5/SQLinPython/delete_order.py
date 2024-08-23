from connect_mysql import connect_database

# Establishing the connection
conn = connect_database()
if conn is not None:
    try:
        cursor = conn.cursor()

        # Assuming we have John Doe's customer ID
        customer_id = 5
        # Order ID to be deleted
        order_id = 1    # Example order ID to be deleted

        # SQL query
        query = "DELETE FROM Orders WHERE id = %s AND customer_id = %s"

        # Executing the query
        cursor.execute(query, (order_id, customer_id))
        conn.commit()
        print("Order deleted successfully!")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        cursor.close()
        conn.close()