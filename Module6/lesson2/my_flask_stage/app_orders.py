from flask import Flask, jsonify, request
from flask_marshmallow import Marshmallow
from marshmallow import Schema, fields, ValidationError
import mysql.connector
from mysql.connector import Error
from password import my_password

# ---------------------------------------------------------------------------
app_orders = Flask(__name__)
ma = Marshmallow(app_orders)

# Order Schema using Marshmallow
class OrderSchema(ma.Schema):
    id = fields.Int(dump_only=True)     # dump_only = read-only; load_only = write-only
    customer_id = fields.Int(required=True)
    date = fields.Date(required=True)

# Initialize schema
order_schema = OrderSchema()
orders_schema = OrderSchema(many=True)

# -----------------------------------------------------------------------------
def get_db_connection():
    """ Connect to the MySQL database and return the connection object """
    # Database connection parameters
    db_name = "e_commerce_db"
    user = "root"
    password = my_password      # <-- Your own password
    host = "localhost"

    try:
    # Attempting to establish a connection
        conn =  mysql.connector.connect(
            database = db_name,
            user = user,
            password = password,
            host = host
        )

        # Check if the connection is successful
        print("Connected to MySQL database successfully")
        return conn

    except Error as e:
        # Handling any connection errors
        print(f"Error: {e}")
        return None
    
# -------------------------------------------------------------------------------
# POST route with validation
@app_orders.route("/orders", methods=["POST"])
def add_order():
    try:
        order_data = order_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400
    

    conn = get_db_connection()
    if conn is None:
        return jsonify({"error": "Database connection failed"}), 500
    
    try:
        cursor = conn.cursor()
        query = "INSERT INTO Orders (date, customer_id) VALUES (%s, %s)"
        cursor.execute(query, (order_data['date'], order_data['customer_id']))
        conn.commit()
        return jsonify({"message": "Order added successfully"}), 201
    
    except Error as e:
        return jsonify({"error": str(e)}), 500
    
    finally:
        cursor.close()
        conn.close()

# -------------------------------------------------------------------------------
# GET route for all orders
@app_orders.route('/orders', methods=['GET'])
def get_orders():
    conn = get_db_connection()
    if conn is None:
        return jsonify({"error": "Database connection failed"}), 500
    
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Orders")
    orders = cursor.fetchall()
    cursor.close()
    conn.close()
    return orders_schema.jsonify(orders)

# -------------------------------------------------------------------------------
# GET route for a single order
@app_orders.route('/orders/<int:order_id>', methods=['GET'])
def get_order(order_id):
    conn = get_db_connection()
    if conn is None:
        return jsonify({"error": "Database connection failed"}), 500
    
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Orders WHERE id = %s", (order_id,))
    order = cursor.fetchone()
    cursor.close()
    conn.close()

    if order:
        return order_schema.jsonify(order)
    else:
        return jsonify({"error": "Order not found"}), 404

# -------------------------------------------------------------------------------
# PUT route with validation
@app_orders.route('/orders/<int:order_id>', methods=["PUT"])
def update_order(order_id):
    try:
        # validate and deserialize input
        order_data = order_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400

    conn = get_db_connection()
    if conn is None:
        return jsonify({"error": "Database connection failed"}), 500
    
    try:
        cursor = conn.cursor()
        query = "UPDATE Orders SET date = %s, customer_id = %s WHERE id = %s"
        cursor.execute(query, (order_data['date'], order_data['customer_id'], order_id))
        conn.commit()
        return jsonify({"message": "Order updated successfully"}), 200
    
    except Error as e:
        return jsonify({"error": str(e)}), 500
    
    finally:
        cursor.close()
        conn.close()

# -------------------------------------------------------------------------------
# DELETE route
@app_orders.route('/orders/<int:order_id>', methods=["DELETE"])
def delete_order(order_id):
    conn = get_db_connection()
    if conn is None:
        return jsonify({"error": "Database connection failed"}), 500
    
    try:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Orders WHERE id = %s", (order_id,))
        conn.commit()
        return jsonify({"message": "Order deleted succesfully"}), 200
    
    except Error as e:
        return jsonify({"error": str(e)}), 500

    finally:
        cursor.close()
        conn.close()

if __name__ == '__main__':
    app_orders.run(debug=True)