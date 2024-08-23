from connect_mysql import connect_database

conn = connect_database()
if conn is not None:
    try:
        cursor = conn.cursor()

        # New customer details
        new_customer = ("John Doe", "john.doe@example.com", "1234567890")

        # SQL query
        query = "INSERT INTO Customers (name, email, phone) VALUES (%s, %s, %s)"

        # Executing the query
        cursor.execute(query, new_customer)
        conn.commit()
        print("New customer added succesfully.")

        # query = "SELECT * FROM Customers"
        # cursor.execute(query)
        # for row in cursor.fetchall():
        #     print(row)


    finally:
        cursor.close()
        conn.close()


# query = "SELECT * FROM Customers"
#     cursor.execute(query)
#     for row in cursor.fetchall():
#         print(row)