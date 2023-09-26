
import requests as rq
from lxml import html

URL = 'https://www.boletinoficial.gob.ar/seccion/segunda'

def get_titles(url:str):
    USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
    r = rq.get(URL, headers={'User-Agent':USER_AGENT})
    dom = html.fromstring(r.content)
    titles = dom.xpath('//p[@class="item"]/text()')
    return [t.strip() for t in titles]

def save_data(titles):
  with open('titles.csv', 'w') as out:
    out.write(','.join(titles))

if __name__ == '__main__':
    titles = get_titles(URL)
    save_data(titles)
    print(f'Guardados {len(titles)} títulos.')
