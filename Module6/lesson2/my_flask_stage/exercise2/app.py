from flask import Flask, jsonify, request
from flask_marshmallow import Marshmallow
from marshmallow import Schema, fields, ValidationError
import mysql.connector
from mysql.connector import Error
from password import my_password

# ---------------------------------------------------------------------------
app = Flask(__name__)
ma = Marshmallow(app)

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

class AuthorSchema(ma.Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    birth_year = fields.Int(required=True)
    nationality = fields.Str(required=True)
    
class BookSchema(ma.Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    genre = fields.Str(required=True)
    price = fields.Float(required=True)
    publication_date = fields.Date(required=True)
    author_id = fields.Int(required=True)

author_schema = AuthorSchema()
authors_schema = AuthorSchema(many=True)
book_schema = BookSchema()
books_schema = BookSchema(many=True)
    
# -------------------------------------------------------------------------------
# Create author route
@ app.route('/authors', methods=["POST"])
def add_author():
    try:
        author = author_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400

    conn = get_db_connection()
    if conn is None:
        return jsonify({"error": "Database connection failed"}), 500
    
    try:
        cursor = conn.cursor()
        query = "INSERT INTO Authors (name, birth_year, nationality) VALUES (%s, %s, %s)"
        cursor.execute(query, (author['name'], author['birth_year'], author['nationality']))

        conn.commit()
        return jsonify({"message": "Author added succesfully"}), 201

    except Error as e:
        return jsonify({"error": str(e)}), 500
    
    finally:
        cursor.close()
        conn.close()
    
# -------------------------------------------------------------------------------
# Create book route
@ app.route('/books', methods=["POST"])
def add_book():
    try:
        book = book_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400

    conn = get_db_connection()
    if conn is None:
        return jsonify({"error": "Database connection failed"}), 500
    
    try:
        cursor = conn.cursor()
        query = "INSERT INTO Books (title, genre, price, publication_date, author_id) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(query, (book['title'], book['genre'], book['price'], book['publication_date'], book['author_id']))

        conn.commit()
        return jsonify({"message": "Book added succesfully"}), 201

    except Error as e:
        return jsonify({"error": str(e)}), 500
    
    finally:
        cursor.close()
        conn.close()
    
# -------------------------------------------------------------------------------
# Get book
@ app.route('/books', methods=["GET"])
def get_books():
    conn = get_db_connection()
    if conn is None:
        return jsonify({"error": "Database connection failed"}), 500
    
    try:
        cursor = conn.cursor(dictionary=True)

        query = """
                SELECT
                    b.id, b.title, a.name, b.genre, b.price
                FROM
                    Books b, Authors a
                WHERE
                    b.author_id = a.id
                """
        cursor.execute(query)
        books = cursor.fetchall()

        return books_schema.jsonify(books)
    
    except Error as e:
        print(f"Error: {e}")
        return jsonify({"Error": "Internal Server Error"}), 500
    
    finally:
        if conn and conn.is_connected():
            cursor.close()
            conn.close()
    
# -------------------------------------------------------------------------------






# -------------------------------------------------------------------------------