from pprint import pprint

from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from models import db, Movie
from db_methods import read_all_movies, edit_movie_by_id, read_movie_by_id, delete_movie_by_id, add_movie
from forms import MovieEditForm, MovieAddForm
from api import IMAGE_URL, get_movie_from_site_by_id, get_movies_from_site


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
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///top_movies.db"
Bootstrap5(app)

# CREATE DB
db.init_app(app)

# CREATE TABLE
with app.app_context():
    db.create_all()



@app.route("/")
def home():
    movies = read_all_movies(app, db)
    return render_template("index.html", movies=movies)


@app.route("/edit", methods=['GET', 'POST'])
def edit():
    movie_id = request.args.get('movie_id', type=int)
    form = MovieEditForm()
    if form.validate_on_submit():
        edit_movie_by_id(app, db, movie_id, float(form.rating.data), form.review.data)
        return redirect(url_for('home'))
    movie = read_movie_by_id(app, db, movie_id)
    # form.rating.label.text += str(movie.rating)
    form.rating.data = movie.rating
    form.review.data = movie.review
    return render_template('edit.html', form=form)


@app.route("/delete", methods=['GET'])
def delete():
    movie_id = request.args.get('movie_id', type=int)
    delete_movie_by_id(app, db, movie_id)
    return redirect(url_for('home'))


@app.route("/add", methods=['GET', 'POST'])
def add():

    tmdb_id = request.args.get('tmdb_id', type=int)
    # print(tmdb_id)
    form = MovieAddForm()
    if form.validate_on_submit():
        movies = get_movies_from_site(form.title.data)
        return render_template('select.html', movies=movies, output_type='movies')
    elif tmdb_id is not None:
        data = get_movie_from_site_by_id(tmdb_id)
        # pprint(data)
        # print(f"{IMAGE_URL}/{data['poster_path']}")
        new_movie = Movie(
            title=data['title'],
            year=int(data['release_date'][:4]),
            description=data['overview'],
            rating=0,
            ranking=0,
            review='',
            img_url=f"{IMAGE_URL}/{data['poster_path']}"
        )
        print(new_movie)
        new_id = add_movie(app, db, new_movie)
        # print(new_movie)
        # added_movie = read_movie_by_title(app, db, data['title'])
        return redirect(url_for('edit', movie_id=new_id))
    else:
        return render_template('add.html', form=form, output_type='form')


if __name__ == '__main__':
    app.run(debug=True)
