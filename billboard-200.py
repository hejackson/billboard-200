#!/usr/bin/env python3

import requests
import bs4
import re

url = 'https://www.billboard.com/charts/billboard-200'
res = requests.get(url)
soup = bs4.BeautifulSoup(res.text, 'html.parser')

albums = []

for x in range(2, 201):
    temp = soup.findAll("div", {"class": "chart-list-item", "data-rank": str(x)})
    result = temp[0].select('div.chart-list-item__title span')[0].getText()
    m = re.search('\n+(.*)\n+', result)
    album = m.group(1)
    result = temp[0].select('div.chart-list-item__artist')[0].getText()
    m = re.search('\n+(.*)\n+', result)
    artist = m.group(1)
    result = temp[0].select('div.chart-list-item__weeks-on-chart')
    if result:
        weeks = int(temp[0].select('div.chart-list-item__weeks-on-chart')[0].getText())
    else:
        weeks = 0
    # print(f"{weeks}, {x}, {album}, {artist}")
    albums.append([x, album, artist, weeks])


print('Longest ranked albums by Billboard-200:')
print('[Current Ranking, Album, Artist, Number of Weeks on Billboard-200]')
for item in sorted(albums, key=lambda x: x[3], reverse=True)[:20]:
    print(item)



