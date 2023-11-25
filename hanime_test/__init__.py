import sys
import requests
from bs4 import BeautifulSoup

url = "https://hanime1.me/search"

payload = {"genre": "裏番", "page": "2"}
HEADERS = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:110.0) Gecko/20100101 Firefox/110.0.'}

r = requests.get(url, params=payload, headers=HEADERS)

print(r.url)
#print(r.text)

if r.status_code != 200:
    # can not use return without a function
    sys.exit("Request fails with error code:" + str(r.status_code))

soup = BeautifulSoup(r.text, "html.parser")

#nodes = soup.find_all("div")
nodes = soup.find_all('div', class_='home-rows-videos-title')
#print(nodes)

for node in nodes:
    print(node.text)
