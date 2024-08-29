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
# List Distinct Genres
@ app.route('/genres', methods=["GET"])
def list_genres():
    conn = get_db_connection()
    if conn is None:
        return jsonify({"error": "Database connection failed"}), 500
    
    try:
        cursor = conn.cursor()
        query = "SELECT DISTINCT genre FROM Books"
        cursor.execute(query)
        genres = [genre[0] for genre in cursor.fetchall()]
        return jsonify(genres)
    
    except Error as e:
        print(f"Error: {e}")
        return jsonify({"Error": "Internal Server Error"}), 500
    
    finally:
        if conn and conn.is_connected():
            cursor.close()
            conn.close()

# -------------------------------------------------------------------------------
# Search Books with Similar Titles
@app.route('/search_books', methods=['GET'])
def search_books():
    keyword = request.args.get('keyword')
    search_query = f"%{keyword}%"

    conn = get_db_connection()
    if not conn:
        return jsonify({"error": "Database connection failed"}), 500
    
    try:
        cursor = conn.cursor(dictionary=True)
        query = "SELECT id, title, genre, publication_date, price FROM Books WHERE title LIKE %s"
        cursor.execute(query, (search_query,))
        books = cursor.fetchall()
        return books_schema.jsonify(books)

    except Error as e:
        return jsonify({"error": str(e)}), 500
    
    finally:
        cursor.close()
        conn.close()

# -------------------------------------------------------------------------------
# Select Books by Authors
@app.route('/books_by_authors', methods=['POST'])
def books_by_authors():
    authors = request.json.get('authors')
    authors = authors.split(", ")   # "J.K. Rowling, J.R.R Tolkien" ==> ["J.K. Rowling", "J.R.R Tolkien"]
    placeholders = ', '.join(['%s'] * len(authors))     # %s, %s, etc...
    print(authors, placeholders)

    conn = get_db_connection()
    if not conn:
        return jsonify({"error": "Database connection failed"}), 500
    
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute(
            f"""
            SELECT
                B.id, B.title, B.genre, B.publication_date, B.price, A.name AS AuthorName
            FROM
                Books B, Authors A
            WHERE
                B.author_id = A.id AND A.name in ({placeholders})
            """, tuple(authors)
        )
        books = cursor.fetchall()
        return books_schema.jsonify(books)

    except Error as e:
        return jsonify({"error": str(e)}), 500
    
    finally:
        cursor.close()
        conn.close()

# -------------------------------------------------------------------------------
# Books Published in a Period
@app.route('/books_by_period', methods=['GET'])
def books_published_in_period():
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')

    conn = get_db_connection()
    if not conn:
        return jsonify({"error": "Database connection failed"}), 500
    
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT id, title, genre, publication_date, price FROM Books WHERE publication_date BETWEEN %s AND %s", (start_date, end_date))
        books = cursor.fetchall()
        return books_schema.jsonify(books)

    except Error as e:
        return jsonify({"error": str(e)}), 500
    
    finally:
        cursor.close()
        conn.close()

# -------------------------------------------------------------------------------
# if __name__ == '__main__':
#     app.run(debug=True)