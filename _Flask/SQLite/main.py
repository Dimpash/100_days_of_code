from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from models import db
from db_methods import read_all_books, add_book, update_book_rating_by_id, read_book_by_id, delete_book_by_id

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''


app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///my_library.db"
# initialize the app with the extension
db.init_app(app)

with app.app_context():
    db.create_all()


# all_books = []
# all_books = [
#     {
#         "title": "Harry Potter",
#         "author": "J. K. Rowling",
#         "rating": 9,
#     }
# ]


@app.route('/')
def home():
    all_books = read_all_books(app, db)
    return render_template("index.html", all_books=all_books)


@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        # book = {
        #     "title": request.form['book'],
        #     "author": request.form['author'],
        #     "rating": request.form['rating']
        # }
        # all_books.append(book)
        add_book(app, db, request.form['book'], request.form['author'], request.form['rating'])
        return redirect(url_for('home'))
    return render_template("add.html")


@app.route("/update_rating", methods=['GET', 'POST'])
def update_rating():
    if request.method == 'POST':
        update_book_rating_by_id(app, db, request.form['book_id'], request.form['new_rating'])
        return redirect(url_for('home'))
    else:
        book_id = request.args.get('book_id', type=int)
        book = read_book_by_id(app, db, book_id)
    return render_template("update_rating.html", book=book)


@app.route("/delete", methods=['GET'])
def delete():
    book_id = request.args.get('book_id', type=int)
    delete_book_by_id(app, db, book_id)
    all_books = read_all_books(app, db)
    return render_template("index.html", all_books=all_books)

    # if request.method == 'POST':
    #     update_book_rating_by_id(app, db, request.form['book_id'], request.form['new_rating'])
    #     return redirect(url_for('home'))
    # else:
    #     book_id = request.args.get('book_id', type=int)
    #     book = read_book_by_id(app, db, book_id)
    # return render_template("update_rating.html", book=book)
    # return render_template("update_rating.html", book_id=book_id, description=description, rating=rating)


if __name__ == "__main__":
    app.run(debug=True)

