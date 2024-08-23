from connect_mysql import connect_database

# Establishing the connection
conn = connect_database()
if conn is not None:
    try:
        cursor = conn.cursor()

        # SQL query
        query = """
        SELECT o.id AS OrderID, o.date AS OrderDate, c.id AS CustomerID, c.name, c.email
        FROM Customers c, Orders o
        WHERE c.id = o.customer_id AND c.name LIKE 'Carol%';
        """

        # Executing the query
        cursor.execute(query)

        # Fetching and displaying the results
        for row in cursor.fetchall():
            print(row)

    except Exception as e:
        print(f"Error: {e}")

    finally:
        cursor.close()
        conn.close()