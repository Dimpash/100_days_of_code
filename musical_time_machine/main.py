import os
from bs4 import BeautifulSoup
from selenium import webdriver
from pprint import pprint
import spotipy
from spotipy.oauth2 import SpotifyOAuth

SPOTIFY_APP_CLIENT_ID = os.environ.get('SPOTIFY_APP_CLIENT_ID')
SPOTIFY_APP_CLIENT_SECRET = os.environ.get('SPOTIFY_APP_CLIENT_SECRET')

URL = "https://www.billboard.com/charts/hot-100/"


def get_list_of_songs(travel_date):
    # webdriver setup
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--incognito')
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)

    driver.get(f"{URL}{travel_date}/")
    web_page = driver.page_source
    # with open('ddd.txt', 'r', encoding="utf-8") as file:
    #     web_page = file.read()

    soup = BeautifulSoup(web_page, "html.parser")

    # with open('ddd.txt', 'w', encoding="utf-8") as file:
    #     file.write(web_page)

    sel_titles = soup.select(selector="li.o-chart-results-list__item > h3.c-title")
    titles = [tag.getText().strip() for tag in sel_titles]

    sel_labels = soup.select(selector="li.o-chart-results-list__item > span.a-no-trucate")
    labels = [tag.getText().strip() for tag in sel_labels]

    result = [{'title': title, 'label': label, 'year': travel_date[:4]} for title, label in zip(titles, labels)]
    return result


def spotify_connect():
    scope = "playlist-modify-private"
    redirect_uri = "https://example.com/callback/"

    sp = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            scope=scope,
            redirect_uri=redirect_uri,
            client_id=SPOTIFY_APP_CLIENT_ID,
            client_secret=SPOTIFY_APP_CLIENT_SECRET,
            show_dialog=True,
            cache_path=".cache"
        )
    )
    user_id = sp.current_user()["id"]
    # print(user_id)

    # print(sp.get_access_token())
    return sp


def get_spotipy_playlist(sp, list_of_songs):
    song_uris = []
    for song in list_of_songs:
        result = sp.search(q=f"track:{song['title']} year:{song['year']}", type="track")
        # pprint(result['tracks']['items'][0]['uri'])
        try:
            song_uris.append(result['tracks']['items'][0]['uri'])
        except IndexError:
            print(f"Song: <{song['title']}> doesn't exist in Spotify. Skipped.")
    return song_uris


def create_my_playlist(sp, song_uris, songs_date):
    playlist = sp.user_playlist_create(user=sp.current_user()["id"], name=f'{songs_date} Billboard 100', public=False)
    # sp.user_playlist_add_tracks(user=sp.current_user()["id"], playlist_id=playlist, tracks=song_uris)
    sp.playlist_add_items(playlist_id=playlist['id'], items=song_uris)



songs_date = input("Which date do you want to travel to? Type the date in format YYYY-MM-DD: ")

songs = get_list_of_songs(songs_date)

sp = spotify_connect()

song_uri_list = get_spotipy_playlist(sp, songs)
# pprint(song_uri_list)

create_my_playlist(sp, song_uri_list, songs_date)


# pprint(song_uri_list)


