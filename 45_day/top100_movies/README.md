# 🎬 Empire's 100 Best Movies Scraper
This Python script scrapes the archived Empire Online's "100 Greatest Movies" list 
and saves it to a local .txt file.

## 📌 Overview
The script:
+ Sends a GET request to a snapshot of Empire Online's 100 Greatest Movies using the Wayback Machine. 
+ Parses the HTML using BeautifulSoup. 
+ Extracts movie titles from all `<h3 class="title">` elements. 
+ Reverses the list (to match ranking order: #1 at the top). 
+ Saves the final list to a file named top100_movies.txt.
