import requests
from bs4 import BeautifulSoup as BS
import re


def get_links():
    links = []
    with open("catalog_list.txt", 'r') as file:  # Открываю файл в режиме чтения
        for url in file:  # Построчно читаю файл
            url = url[0:-2]
            links.append(url)
    return links


links = get_links()


def get_data():
    data = []

    for url_ in links:
        response = requests.get(url_)
        html = response.text

        code = re.findall(r'\d', url_)
        join_ = ''
        code_ = join_.join(code)
        code_ = f"Код товара - {code_}"

        soup = BS(html, "html.parser")

        title = soup.find('h1', itemprop="name")
        title = title.text

        description = soup.find('div', id="prod")
        description = description.text.replace('\n', '')

        price = soup.find('span', class_='bold')
        price = price.text[4:]

        photos_list = []
        photos = soup.find('ul', class_='photos-inner').find_all('a')
        for li in photos:
            href = li.get('href')
            href = f"https://www.rusplitka.ru{href}"
            photos_list.append(href)
        len_photos = f"Количество фото - {len(photos)}"

        size = soup.find('ul', class_="list-inline list-commas inline")
        size = size.text.replace('\n', '')

        data.append([url_, title, code_, description, size, price, len_photos, photos_list, ])

        print(f"Товар со страницы {url_} добавлен.")

    return data
