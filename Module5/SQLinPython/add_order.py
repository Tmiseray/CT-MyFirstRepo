from connect_mysql import connect_database

# Establishing the connection
conn = connect_database()
if conn is not None:
    try:
        cursor = conn.cursor()

        # Assuming we have John Doe's customer ID
        john_doe_id = 5
        order_date = "2024-01-15"

        # SQL query
        query = "INSERT INTO Orders (date, customer_id) VALUES (%s, %s)"

        # Executing the query
        cursor.execute(query, (order_date, john_doe_id))
        conn.commit()
        print("Order added successfully for John Doe")

    finally:
        cursor.close()
        conn.close()
