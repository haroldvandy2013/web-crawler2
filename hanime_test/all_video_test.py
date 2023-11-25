import sys
import requests
from bs4 import BeautifulSoup

url = "https://hanime1.me/search"

HEADERS = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:110.0) Gecko/20100101 Firefox/110.0.'}

maxPage = 61
index = 1

fout = open("all_video_title.txt", "w", encoding='utf-8')
while index <= maxPage:
    payload = {"genre": "裏番", "page": str(index)}
    r = requests.get(url, params=payload, headers=HEADERS)
    print(r.url)

    if r.status_code != 200:
        # can not use return without a function
        continue

    soup = BeautifulSoup(r.text, "html.parser")
    nodes = soup.find_all('div', class_='home-rows-videos-title')

    for node in nodes:
        title = node.text
        print(title)
        fout.write("%s\n"%title)
        fout.flush()

    index = index + 1

fout.close()