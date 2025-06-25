from bs4 import BeautifulSoup
import requests

# Live Website (will change over time)
response = requests.get("https://news.ycombinator.com/")

yc_web_page = response.text
soup = BeautifulSoup(yc_web_page, 'html.parser')
articles = soup.find_all(name="span", class_="titleline")
article_texts = []
article_links = []
for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.find(name='a').get("href")
    article_links.append(link)

# Finding the upvotes
# If all articles on the page have upvotes, this will work:
# article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

# However, some submissions may not have any upvotes yet.
# This uses a conditional expression to handle cases where there are no upvotes (span is None)
subtexts = soup.find_all(class_="subtext")
article_upvotes = [int(line.span.span.getText().strip(" points")) if line.span.span else 0 for line in subtexts]

largest_number = max(article_upvotes)
largest_index = article_upvotes.index(largest_number)

print(
    f"Most upvoted article: {article_texts[largest_index]}\n"
    f"Number of upvotes: {article_upvotes[largest_index]} points\n"
    f"Available at: {article_links[largest_index]}."
)

#*************************************************************************
# Static practice
response = requests.get("https://appbrewery.github.io/news.ycombinator.com/")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
article_tags = soup.find_all(name="a", class_="storylink")
article_text = []
article_links = []
for article_tag in article_tags:
    text = article_tag.getText()
    article_text.append(text)
    link = article_tag.get("href")
    article_links.append(link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
zipped_data = zip(article_upvotes, article_text, article_links )
data_list = list(zipped_data)
votes, title, link = max(data_list)
print(
    f"Most upvoted article: {title}\n"
    f"Number of upvotes: {votes} points\n"
    f"Available at: {link}."
)
