import requests
from bs4 import BeautifulSoup as BS
import re
import csv
from multiprocessing import Pool
from datetime import datetime


start = datetime.now()
links = []
with open('full_cataloc.txt', 'r') as file:
    for url in file:
        url = url.strip()
        links.append(url)


def parsing(url):
    products = []
    exceptions = []
    i = 0
    for url in links[0:3]:
        try:
            link = f'https://www.rusplitka.ru{url}'
            response = requests.get(link)
            soup = BS(response.content, 'html.parser')
            if response.status_code != 200:
                print("Что то не так!")
            elif response.status_code == 200:
                title = soup.find('h1', itemprop="name").text #получаем название товаров

                code = soup.find('span', class_="label label-force label-primary js-product-code").text

                # specifications = soup.find('ul', class_="list-unstyled attrs").text
                # specs = specifications.replace('	', ' ').replace('\n', ' ')
                # specs = ' '.join(specs.split())
                # print(specs)

                price = soup.find('div', class_="sum bold opt-hidden").text.replace('	', '')

                specifications = soup.find('ul', class_="list-unstyled attrs")
                for s in specifications:
                    s.find('a')

                    print(s.text)
                i += 1
                t = datetime.now()
                iteration = t - start
                print(f'Строка № {i} пройдена за {iteration} времени')
        except Exception as e:
            result = f'{str(e)} + {link}'
            exceptions.append(result)
            print(e)



parsing(url)
end = datetime.now()
total = end - start
print(f'Скрипт отработал за {total}')