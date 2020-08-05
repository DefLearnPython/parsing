import requests
from bs4 import BeautifulSoup as BS
import re
import csv
from multiprocessing import Pool
from datetime import datetime


start = datetime.now()
links = []
with open('full_cataloc.txt.txt', 'r') as file:
    for url in file:
        url = url.strip()
        links.append(url)


def parsing(url):
    data = []
    len_photos = []
    exceptions = []
    i = 0
    for url in links[0:300]:
        try:
            link = f'https://www.rusplitka.ru{url}'
            response = requests.get(link)
            soup = BS(response.content, 'html.parser')
            if response.status_code != 200:
                print("Что то не так!")
            elif response.status_code == 200:
                specifications = soup.find('ul', class_='list-unstyled attrs').find_all('span',class_='label')
                specifications = str(specifications).replace('<span class="label">', '').replace('</span>', '')
                specifications = str(specifications).replace(',', '\n').replace(':', '').replace('<sup>','').replace('</sup>','')
                if str(specifications) not in data:
                    data.append(specifications)

                photos = soup.find('ul', class_='photos-inner').find_all('a')
                len_photos.append(len(photos))

                i += 1
                t = datetime.now()
                iteration = t - start
                print(f'Строка № {i} пройдена за {iteration} времени')
        except Exception as e:
            result = f'{str(e)} + {link}'
            exceptions.append(result)
            print(e)
    max_len = max(len_photos)

    with open('maxlen.txt', 'w')as file:
        file.write(str(max_len))
        file.close()

    return data


data = parsing(url)

with open('specification.txt', 'w') as file:
    for line in data:
        file.write(str(line) + '\n')

end = datetime.now()
total = end - start
print(f'Скрипт отработал за {total}')