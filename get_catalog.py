import requests
from bs4 import BeautifulSoup as BS
from multiprocessing import Pool


def get_links():
    pages_list = []
    with open("pages_list.txt", 'r') as file:
        for url in file:
            url = url.strip()
            pages_list.append(url)
    return pages_list


pages_list = get_links()

# Получаем ссылки на все товары
def get_catalog():
    cat_links = []

    for page in pages_list:
        response = requests.get(page)
        html_ = response.text
        soup = BS(html_, "html.parser")
        catalog = soup.find_all('a', class_='title')
        print(f"Распарсил {page}, перехожу к следующей странице.")

        for link in catalog:
            a = link.get('href')
            cat_links.append(a)
    return cat_links


catalog_list = get_catalog()

#Сохраняем ссылки на товары в файл
with open("catalog_list.txt", 'w') as file:
    for line in catalog_list:
        file.write(f"https://www.rusplitka.ru{line}\n")
    file.close()

