from flask import Flask, jsonify, request
from flask_marshmallow import Marshmallow
from marshmallow import fields, ValidationError
import mysql.connector
from mysql.connector import Error
from password import my_password

app = Flask(__name__)
ma = Marshmallow(app)

class CustomerSchema(ma.Schema):
    name = fields.String(required=True)
    email = fields.String(required=True)
    phone = fields.String(required=True)
    # id = fields.Integer(required=True)
    # Think of 'fields' as columns in your schema

    class Meta:     # Options object for a schema, can put tons of things within here
        fields = ("name", "email", "phone", "id") # List of fields we want included in serialized result
                                            # Serialization = process of converting complex datatype like Python object into a format like JSON
                                            # Deserialization = complete opposite of above

customer_schema = CustomerSchema()      # Single bit of data
customers_schema = CustomerSchema(many=True)    # Many bits of data


def get_db_connection():
    """ Connect to the MySQL database and return the connection object """
    # Database connection parameters
    db_name = "e_commerce_db"
    user = "root"
    password = my_password
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


# Whatever is in this app.route('/') will be the route after your http://0.0.0.0:0000 and can have multiple routes
@app.route('/') 
def home():
    return 'Welcome to the Flask Music Festival!'

@app.route("/customers", methods=["GET"])
def get_customers():
    try:
        conn = get_db_connection()
        if conn is None:
            return jsonify({"error": "Database connection failed"}), 500
        cursor = conn.cursor(dictionary=True)

        query = "SELECT * FROM Customers"
        cursor.execute(query)
        customers = cursor.fetchall()

        return customers_schema.jsonify(customers)
    
    except Error as e:
        print(f"Error: {e}")
        return jsonify({"Error": "Internal Server Error"}), 500
    
    finally:
        if conn and conn.is_connected():
            cursor.close()
            conn.close()

@app.route("/customers", methods=["POST"])
def add_customer():
    try:
        customer_data = customer_schema.load(request.json)
    except ValidationError as e:
        print(f"Error: {e}")
        return jsonify(e.messages), 400
    
    try:
        conn = get_db_connection()
        if conn is None:
            return jsonify({"error": "Database connection failed"}), 500
        cursor = conn.cursor()

        new_customer = (customer_data['name'], customer_data['email'], customer_data['phone'])

        query = "INSERT INTO Customers (name, email, phone) VALUES (%s, %s, %s)"
        cursor.execute(query, new_customer)
        conn.commit()

        return jsonify({"message": "New customer added successfully"}), 201
    except Error as e:
        print(f"Error: {e}")
        return jsonify({"error": "Internal Server Error"}), 500
    finally:
        if conn and conn.is_connected():
            cursor.close()
            conn.close()


@app.route("/customers/<int:id>", methods=["PUT"])
def update_customer(id):
    try:
        customer_data = customer_schema.load(request.json)
    except ValidationError as e:
        print(f"Error: {e}")
        return jsonify(e.messages), 400
    
    try:
        conn = get_db_connection()
        if conn is None:
            return jsonify({"error": "Database connection failed"}), 500
        cursor = conn.cursor()

        updated_customer = (customer_data['name'], customer_data['email'], customer_data['phone'], id)

        query = "UPDATE Customers SET name = %s, email = %s, phone = %s WHERE id = %s"
        cursor.execute(query, updated_customer)
        conn.commit()

        return jsonify({"message": "Updated the customer successfully"}), 201
    except Error as e:
        print(f"Error: {e}")
        return jsonify({"error": "Internal Server Error"}), 500
    finally:
        if conn and conn.is_connected():
            cursor.close()
            conn.close()


@app.route("/customers/<int:id>", methods=["DELETE"])
def delete_customer(id):
    try:
        conn = get_db_connection()
        if conn is None:
            return jsonify({"error": "Database connection failed"}), 500
        cursor = conn.cursor()

        customer_to_remove = (id,)

        # Verify the customer exists
        cursor.execute("SELECT * FROM Customers WHERE id = %s", customer_to_remove)
        customer = cursor.fetchone()
        if not customer:
            return jsonify({"error": "Customer not found"}), 404
        
        query = "DELETE FROM Customers WHERE id = %s"
        cursor.execute(query, customer_to_remove)
        conn.commit()

        return jsonify({"message": "Customer removed successfully"}), 200
    except Error as e:
        print(f"Error: {e}")
        return jsonify({"error": "Internal Server Error"}), 500
    finally:
        if conn and conn.is_connected():
            cursor.close()
            conn.close()


# @app.route("/customers", methods=["UPDATE"])
# @app.route("/customers", methods=["GET"])


# if __name__ == '__main__':
#     app.run(debug=True)
# 
# The above if statement is only used for running within VS Code

# To run a Flask App, the proper way is by typing in your VENV terminal :
# `flask run`

# If you make any adjustments to your app, you will need to make sure to either restart app OR turn debugger on! :
# `flask run --debug`
# This way when you refresh, all updates take place automatically!