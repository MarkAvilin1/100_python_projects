from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://www.empireonline.com/movies/features/best-movies-2/")
response.raise_for_status()
data = response.text

soup = BeautifulSoup(data, "html.parser")

titles = soup.find_all("h3", class_="title")

movies_title = [movie.getText() for movie in titles]

movies = movies_title[::-1]

with open("movies.txt", "w", encoding="utf8") as file:
    file.write("1) ")
    for movie in movies:
        file.write(movie + "\n")
