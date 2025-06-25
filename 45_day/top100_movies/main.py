from bs4 import BeautifulSoup
import requests

URL = ("https://web.archive.org/web/20200518073855/"
       "https://www.empireonline.com/movies/features/best-movies-2/")

response = requests.get(URL)
website_data =  response.text
soup = BeautifulSoup(website_data, "html.parser")

all_movies =  soup.find_all(name="h3", class_="title")
movie_titles = [movie.getText() for movie in all_movies][::-1]

with open("top100_movies.txt", mode="w") as file:
    for title in movie_titles:
        file.write(f"{title}\n")

