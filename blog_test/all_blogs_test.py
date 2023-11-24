import re
from utils import url_manager
import requests
from bs4 import BeautifulSoup

root_url = "http://www.crazyant.net"

pattern = r'^http://www.crazyant.net/\d+.html$'

urls = url_manager.UrlManager()
urls.add_new_url(root_url)

fout = open("all_blogs.txt", "w", encoding='utf-8')
while urls.has_new_url():
    current_url = urls.get_url()
    r = requests.get(current_url, timeout=5)
    if r.status_code != 200:
        print("error, skip")
        continue

    soup = BeautifulSoup(r.text, "html.parser")
    title = soup.title.string

    fout.write("%s\t%s\n"%(current_url, title))
    fout.flush()
    print("Found url " + current_url)

    links = soup.find_all("a")
    for link in links:
        href = link.get("href")
        if href is None:
            continue

        # print("Found link" + href)
        if re.match(pattern, href):
            urls.add_new_url(href)

fout.close()