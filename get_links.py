import requests
from bs4 import BeautifulSoup as BS
from multiprocessing import Pool


# Получаем все страницы с товаром
def get_all_collections():
    links = []
    link = "https://www.rusplitka.ru/catalog/"

    for i in range(1, 438):  # Первая цифра, начало, вторая количество страниц + 1
        new_link = link + 'page-' + str(i) + '/'
        i += 1
        if i <= 438:
            links.append(new_link)
    return links


# Сохраняем все ссылки на страницы в список, и записываем его в текстовый файл
pages_list = get_all_collections()
with open("pages_list.txt", 'w') as file:
    for line in pages_list:
        file.write(line + '\n')
    file.close()

