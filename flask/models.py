from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)
# Configure the database connection; the URI points to a SQLite database named books.db.
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Unique ID for each book.
    title = db.Column(db.String(250), nullable=False)  # Title of the book; cannot be null.
    author = db.Column(db.String(250), nullable=False)  # Author of the book; cannot be null.
    rating = db.Column(db.Float, nullable=False)  # Rating of the book; cannot be null.

    def __repr__(self):
        return f'<Book {self.title}>'
