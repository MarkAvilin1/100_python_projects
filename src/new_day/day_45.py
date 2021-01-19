from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://news.ycombinator.com/")
response.raise_for_status()
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

article_texts = []
article_links = []

articles = soup.find_all("a", class_="storylink")
for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)

article_upvotes = [int(vote.getText().split()[0]) for vote in (soup.find_all(name="span", class_="score"))]
#
# print(*article_texts)
# print(*article_links)
# print(*article_upvotes)


max_upvote = max(article_upvotes)
# print(max_upvote)
max_upvote_index = article_upvotes.index(max_upvote)

print(article_texts[max_upvote_index])
print(article_links[max_upvote_index])

with open("website.html") as file:
    contents = file.read()
    soup = BeautifulSoup(contents, "html.parser")
    print(soup.title.string)
