import sp as sp
from bs4 import BeautifulSoup
import requests
import spotipy

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}")
html_content = response.text
"""<span class="chart-element__rank__number">1</span>
<span class="chart-element__information__song text--truncate color--primary">Mood</span>"""

soup = BeautifulSoup(html_content, "html.parser")

ranks = soup.find_all(name="span", class_="chart-element__rank__number")
songs = soup.find_all(name="span", class_="chart-element__information__song")

ranks_list = [rank.getText() for rank in ranks]
songs_list = [song.getText() for song in songs]

print(ranks_list)
print(songs_list)

"""Client ID ae50503d65b8431392ae08490ebed141
Client Secret 0de64b8d049d41abb4e8e22a14625400 """


user_id = sp.current_user()["id"]
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
song_names = ["The list of song", "titles from your", "web scrape"]

song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")
