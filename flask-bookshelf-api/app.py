from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bookshelf.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Define the Book model
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    genre = db.Column(db.String(50), nullable=False)
    publication_year = db.Column(db.Integer, nullable=False)

# Create Book - POST /books
@app.route('/books', methods=['POST'])
def create_book():
    # Use request.get_json() to retrieve JSON data from the request body
    data = request.get_json()
    if not data:
        abort(400, description="Invalid request. JSON data required.")
    if not all(key in data for key in ('title', 'author', 'genre', 'publication_year')):
        abort(400, description="Missing required fields")
    
    new_book = Book(
        title=data['title'],
        author=data['author'],
        genre=data['genre'],
        publication_year=data['publication_year']
    )
    db.session.add(new_book)
    db.session.commit()
    return jsonify(new_book.id), 201

# Retrieve All Books - GET /books
@app.route('/books', methods=['GET'])
def get_books():
    books = Book.query.all()
    return jsonify([book.to_dict() for book in books])

# Retrieve Single Book - GET /books/<id>
@app.route('/books/<int:id>', methods=['GET'])
def get_book(id):
    book = Book.query.get_or_404(id)
    return jsonify(book.to_dict())

# Update Book - PUT /books/<id>
@app.route('/books/<int:id>', methods=['PUT'])
def update_book(id):
    book = Book.query.get_or_404(id)
    data = request.get_json()
    for key in ('title', 'author', 'genre', 'publication_year'):
        if key in data:
            setattr(book, key, data[key])
    db.session.commit()
    return jsonify(book.to_dict())

# Delete Book - DELETE /books/<id>
@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    book = Book.query.get_or_404(id)
    db.session.delete(book)
    db.session.commit()
    return '', 204

# Utility function to convert book objects to dictionary
def to_dict(self):
    return {
        'id': self.id,
        'title': self.title,
        'author': self.author,
        'genre': self.genre,
        'publication_year': self.publication_year
    }

Book.to_dict = to_dict

if __name__ == '__main__':
    app.run(debug=True)
