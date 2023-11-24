import sys
import requests
from bs4 import BeautifulSoup

url = "http://www.crazyant.net"

r = requests.get(url)

if r.status_code != 200:
    # can not use return without a function
    sys.exit("Request fails with error code:" + str(r.status_code))

soup = BeautifulSoup(r.text, "html.parser")

h2_nodes = soup.find_all("h2", class_="entry-title")

for h2_node in h2_nodes:
    link = h2_node.find("a")
    print(link['href'], link.get_text())