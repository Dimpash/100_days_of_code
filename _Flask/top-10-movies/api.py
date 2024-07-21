import requests
from configparser import ConfigParser


# instantiate ini
config = ConfigParser()

# parse existing file
config.read('../../../Auth/auth.ini')

API_READ_ACCESS_TOKEN = config.get('the_movie_db_api', 'API_READ_ACCESS_TOKEN')
API_SEARCH_URL = 'https://api.themoviedb.org/3/search/movie'
API_MOVIE_URL = 'https://api.themoviedb.org/3/movie'
IMAGE_URL = 'https://image.tmdb.org/t/p/w600_and_h900_bestv2/'


def get_movies_from_site(title):
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {API_READ_ACCESS_TOKEN}"
    }

    params = {
        'query': title,
        'include_adult': 'false',
        'language': 'en-US',
        'page': '1'
    }

    response = requests.get(API_SEARCH_URL, headers=headers, params=params)
    data = response.json()['results']
    return data


def get_movie_from_site_by_id(tmdb_id):
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {API_READ_ACCESS_TOKEN}"
    }

    params = {
        'language': 'en-US'
    }
    response = requests.get(f"{API_MOVIE_URL}/{tmdb_id}", headers=headers, params=params)
    data = response.json()
    return data
