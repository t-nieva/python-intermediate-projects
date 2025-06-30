from bs4 import BeautifulSoup
import requests
from dotenv import load_dotenv
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from pprint import pprint

load_dotenv()

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=os.getenv("SPOTIFY_CLIENT_ID"),
    client_secret=os.getenv("SPOTIFY_CLIENT_SECRET"),
    redirect_uri=os.getenv("SPOTIFY_REDIRECT_URI"),
    scope="playlist-modify-private"
))

user_id = None
try:
    user_id = sp.current_user()["id"]
    print(f"[INFO] Your Spotify user ID: {user_id}")
except Exception as e:
    print(f"[ERROR] Unable to get user ID: {e}")
    exit(1)

# date = input("What year do you want to travel to? Tape the date in this format YYYY-MM-DD: ")
date = "2000-08-12"
year = date.split("-")[0]
playlist_name = f"{date} Billboard 100"

URL = "https://www.billboard.com/charts/hot-100/2000-08-12/"

header = {"USER-AGENT": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36"}

try:
    response = requests.get(URL, headers=header)
    response.raise_for_status()
    website_data = response.text
except requests.RequestException as e:
    print(f"[ERROR] Failed to fetch Billboard page: {e}")
    exit(1)

soup = BeautifulSoup(website_data, "html.parser")

# *********************** Scraping top 100 songs ***********************
titles = soup.select("li ul li h3")
song_titles = [item.getText().strip() for item in titles]
print(f"[INFO] Found {len(song_titles)} song titles.")

# *********************** Search Spotify for the Songs ***********************
song_uris = []

for song in song_titles:
    try:
        query = f"track:{song} year:{year}"
        result = sp.search(q=query, type="track", limit=1)

        tracks = result["tracks"]["items"]
        if tracks:
            uri = tracks[0]["uri"]
            song_uris.append(uri)
            print(f"Found: {song} — {uri}")
        else:
            print(f"Not found: {song}")

    except Exception as e:
        print(f"Error with song {song}: {e}")

print("\nList of found URIs:")
pprint(song_uris)

# *********************** Create a private playlist ***********************
try:
    playlist = sp.user_playlist_create(
        user=user_id,
        name=playlist_name,
        public=False,
        description=f"Top 100 Billboard songs for {date}"
    )

    playlist_id = playlist["id"]
    print(f"[INFO] Playlist created: {playlist_name} — ID: {playlist_id}")
except Exception as e:
    print(f"[ERROR] Failed to create playlist: {e}")
    exit(1)

# *********************** Add songs to the playlist ***********************
sp.playlist_add_items(playlist_id, song_uris)
print("Songs successfully added to the playlist!")
