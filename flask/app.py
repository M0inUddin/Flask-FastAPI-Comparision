from flask import Flask, request, render_template, redirect
from models import db, Book

app = Flask(__name__)
db.init_app(app)

@app.route('/')
def index():
    # Fetches all book entries from the database to display them on the main page.
    books = Book.query.all()
    return render_template('index.html', books=books)

@app.route('/book', methods=['POST'])
def add_book():
    # Retrieves book details from the form data submitted via POST.
    title = request.form['title']
    author = request.form['author']
    rating = request.form['rating']
    
    # Creates a new book object and adds it to the database.
    new_book = Book(title=title, author=author, rating=float(rating))
    db.session.add(new_book)
    db.session.commit()
    
    # Redirects to the homepage after the book is added to display the updated list of books.
    return redirect('/')

if __name__ == '__main__':
    # The db.create_all() can be used here to create all the tables at the start if they don't exist.
    with app.app_context():
        db.create_all()
    app.run(debug=True)
