import requests
from bs4 import BeautifulSoup
import re

# URL = 'https://ru.wikipedia.org/wiki/Python'
#
# headers = {
#     'accept-ranges': 'bytes',
#     'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 '
#                   'YaBrowser/23.3.3.706 Yowser/2.5 Safari/537.36'
# }
#
# response = requests.get(URL, headers=headers)
# html = response.text
# soup = BeautifulSoup(html, 'html.parser')

# with open('index.html', 'w') as file:
#     file.write(html)

with open("index.html") as file:
    src = file.read()

soup = BeautifulSoup(src, "lxml")
links = soup.find(id='bodyContent').find_all('a')

for item in links:
    item_text = item.text
    if "https" in item.get("href"):
        item_href = item.get("href")
    else:
        item_href = "https://ru.wikipedia.org/" + item.get("href")
    print(f"{item_text}: {item_href}")

# print(response)
