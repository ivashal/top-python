import requests
from bs4 import BeautifulSoup
import json

URL: str = 'https://spys.one'

headers = {
    'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 "
                  "YaBrowser/23.3.3.706 Yowser/2.5 Safari/537.36"}

response = requests.get(URL, headers=headers)

html = response.text
soup = BeautifulSoup(html, 'html.parser')

list_1 = []

for i in soup.find_all('tr', {'class': ['spy1x', 'spy1xx']}):
    row = []
    for j in i:
        substring = j.text
        row.append(substring)
    if len(row) <= 1:
        continue
    else:
        list_1.append(row)

print(response)

dict_1 = {}
id_count = 1

for i in list_1:
    new = {id_count: i}
    dict_1.update(new)
    id_count += 1

with open('spys.json', 'w') as file:
    json.dump(dict_1, file, ensure_ascii=False, indent=2)

data_json: str = json.dumps(dict_1, ensure_ascii=False, indent=2)

print(data_json)
pass
