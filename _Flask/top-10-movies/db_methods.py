from models import Movie


def read_all_movies(app, db):
    with app.app_context():
        result = db.session.execute(db.select(Movie).order_by(Movie.ranking.desc())).scalars().all()
        # print(result)
    return result


def read_movie_by_id(app, db, movie_id):
    with app.app_context():
        movie = db.get_or_404(Movie, movie_id)
        # movie = db.session.execute(db.select(Movie).where(Movie.id == id)).scalar()
    return movie


# def read_movie_by_title(app, db, title):
#     with app.app_context():
#         movie = db.session.execute(db.select(Movie).where(Movie.title == title)).scalar()
#     return movie

def recalc_ranking(app, db):
    with app.app_context():
        movies = db.session.execute(db.select(Movie).order_by(Movie.rating.desc())).scalars().all()
        i = 1
        for movie in movies:
            movie.ranking = i
            i += 1
        db.session.commit()


# def add_movie(app, db, title, year, description, rating, ranking, review, img_url):
def add_movie(app, db, new_movie):
    with app.app_context():
        # new_movie = Movie(title=title, year=year, description=description, rating=rating, ranking=ranking,
        #                   review=review, img_url=img_url)
        db.session.add(new_movie)
        db.session.commit()
        return new_movie.id


def edit_movie_by_id(app, db, movie_id, new_rating, new_review):
    with app.app_context():
        # movie_to_update = db.session.execute(db.select(Movie).where(Movie.id == movie_id)).scalar()
        movie_to_update = db.get_or_404(Movie, movie_id)
        movie_to_update.rating = new_rating
        movie_to_update.review = new_review
        db.session.commit()
    recalc_ranking(app, db)


def delete_movie_by_id(app, db, movie_id):
    with app.app_context():
        movie_to_delete = db.session.execute(db.select(Movie).where(Movie.id == movie_id)).scalar()
        # or book_to_delete = db.get_or_404(Movie, movie_id)
        db.session.delete(movie_to_delete)
        db.session.commit()


new_movie = Movie(
    title="Phone Booth",
    year=2002,
    description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
    rating=7.3,
    ranking=10,
    review="My favourite character was the caller.",
    img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
)
# add_movie(app, db, new_movie)
second_movie = Movie(
    title="Avatar The Way of Water",
    year=2022,
    description="Set more than a decade after the events of the first film, learn the story of the Sully family (Jake, Neytiri, and their kids), the trouble that follows them, the lengths they go to keep each other safe, the battles they fight to stay alive, and the tragedies they endure.",
    rating=7.3,
    ranking=9,
    review="I liked the water.",
    img_url="https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg"
)
# add_movie(app, db, second_movie)