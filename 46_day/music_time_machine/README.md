# 🎵 Billboard Hot 100 Spotify Playlist Creator

This Python script scrapes the Billboard Hot 100 chart for a specific date, 
searches for the corresponding songs on Spotify, 
and creates a private Spotify playlist with those songs.

## Features
- Scrapes top 100 songs from Billboard for a given date.
- Searches Spotify for the tracks matching the Billboard list.
- Creates a private Spotify playlist named `YYYY-MM-DD Billboard 100`.
- Adds found songs to the newly created playlist.

## Prerequisites

- Python 3.7+
- Spotify Developer account with a created Spotify App
- Spotify App credentials: **Client ID**, **Client Secret**, and **Redirect URI**
- Billboard website access


### Create a .env file in your project directory with your Spotify credentials

+ SPOTIFY_CLIENT_ID=your_client_id_here
+ SPOTIFY_CLIENT_SECRET=your_client_secret_here
+ SPOTIFY_REDIRECT_URI=your_redirect_uri_here 

**Note:** Your redirect URI must match exactly the one configured in your Spotify Developer Dashboard.

### Modify the script or input your target date

By default, the script is set to scrape Billboard Hot 100 for the date "2000-08-12".
To change it, update the date variable in the script or uncomment the input line to enter the date interactively.

## Important Notes
+ The Spotify scope used is playlist-modify-private, so the playlist will be private by default.
+ Some songs might not be found on Spotify; the script will notify you about these.
+ The script adds all songs found in one go (Spotify API allows up to 100 tracks per request).
