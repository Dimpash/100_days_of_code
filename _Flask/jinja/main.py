from flask import Flask, render_template
import random
from datetime import datetime as dt
import requests



app = Flask(__name__)


def guess_gender(name):
    parameters = {
        "name": name
    }
    response = requests.get('https://api.genderize.io', params=parameters)
    response.raise_for_status()
    data = response.json()
    return data['gender'], data['count']


def guess_age(name):
    parameters = {
        "name": name
    }
    response = requests.get('https://api.agify.io', params=parameters)
    response.raise_for_status()
    data = response.json()
    return data['age'], data['count']


@app.route('/')
def home():
    rand_n = random.randint(0, 10)
    # copyright_year = dt.now().year
    return render_template("index.html", rand_n=rand_n, copyright_year=dt.now().year)


@app.route('/guess/<name>')
def guess(name):
    gender, gender_count = guess_gender(name)
    age, age_count = guess_age(name)
    return render_template("guess.html", name=name.title(), gender=gender, gender_count=gender_count,
                           age=age, age_count=age_count)


@app.route('/blog')
def blog():
    response = requests.get('https://api.npoint.io/61ebc1048f18837f4720')
    data = response.json()
    print(data)
    return render_template("blog.html", posts=data)


if __name__ == "__main__":
    app.run(debug=True)


