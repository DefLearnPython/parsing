import requests
from bs4 import BeautifulSoup as BS
import re
import csv
from multiprocessing import Pool
from datetime import datetime

#Получаем ссылки на товары из файла
links = []
with open("catalog_list.txt", 'r') as file:
    for url in file:
        url = url.strip()
        links.append(url)
start = datetime.now()


def get_data(url_):
    data = []
    i = 1
    for url_ in links:
        if url_ == "https://www.rusplitka.ru/catalog/land/":
            pass
        else:
            response = requests.get(url_)
            html = response.text

            code = re.findall(r'\d', url_)
            join_ = ''
            code_ = join_.join(code)
            code_ = f"Код товара - {code_}"

            soup = BS(html, "html.parser")

            title = soup.find('h1', itemprop="name") #получаем название товаров
            title = title.text

            description = soup.find('div', id="prod") #получаем описание товара
            description = description.text.replace('\n', '')

            price = soup.find('span', class_='bold') #Получаем цены и обрезаем лишнее
            price = price.text[4:]

            photos_list = []
            photos = soup.find('ul', class_='photos-inner').find_all('a') #получаем количество фото и ссылки на них
            for li in photos:
                href = li.get('href')
                href = f"https://www.rusplitka.ru{href}"
                photos_list.append(href)
            len_photos = f"Количество фото - {len(photos)}"

            size = soup.find('ul', class_="list-inline list-commas inline")#получаем размеры товаров
            size = size.text.replace('\n', '')

            i += 1
            data.append([
                    url_,
                    title,
                    code_,
                    description,
                    size,
                    price,
                    len_photos,
                    photos_list
                    ])#записываем данные в список
            with open('all_data.csv', 'w') as file:
                writer = csv.writer(file)
                for row in data:
                    writer.writerow((row))

        print("Спарсил " + str(i) + " строку")#это чтоб не было скучно смотреть в пустую консоль


    print("Данные записаны в файл")
    return data

if __name__ == "__main__":
    with Pool(40) as p:
        p.map(get_data, links)
    end = datetime.now()
    total = end - start
    print(f"Скрипт отработал за {total} секунд")
