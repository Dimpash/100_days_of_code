from models import Book


def read_all_books(app, db):
    with app.app_context():
        result = db.session.execute(db.select(Book).order_by(Book.title)).scalars().all()
        print(result)
        # all_books = result.scalars()
        # print(all_books)
    return result


def read_book_by_id(app, db, id):
    with app.app_context():
        book = db.get_or_404(Book, id)
        # book = db.session.execute(db.select(Book).where(Book.id == id)).scalar()
    return book


def read_book_by_title(app, db, title):
    with app.app_context():
        book = db.session.execute(db.select(Book).where(Book.title == title)).scalar()


def add_book(app, db, title, author, rating):
    with app.app_context():
        new_book = Book(title=title, author=author, rating=rating)
        db.session.add(new_book)
        db.session.commit()


def update_book_rating_by_id(app, db, book_id, new_rating):
    with app.app_context():
        book_to_update = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
        # or book_to_update = db.get_or_404(Book, book_id)
        book_to_update.rating = new_rating
        db.session.commit()


def delete_book_by_id(app, db, book_id):
    with app.app_context():
        book_to_delete = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
        # or book_to_delete = db.get_or_404(Book, book_id)
        db.session.delete(book_to_delete)
        db.session.commit()
