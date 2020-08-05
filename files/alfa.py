from bs4 import BeautifulSoup as BS
import requests
all_page_catalog = 1
all_page = 437
if all_page_catalog == 1:
    # Усього товарів 6115
    reapet = range(1, all_page)
    for b in reapet:
        print(b)
        url = 'https://www.rusplitka.ru/catalog/page-'+str(b)+'/'
        #if b == 1:
        #url = 'https://kondicioneri24.ru/product-category/konditsionery/?product_order=menu_order&product_sort=asc&product_count=96#038;product_sort=asc&product_count=96'
        olx = requests.get(url)  # Передаю силку на потрібну сторінку і метод повертає html сторінки
        html = BS(olx.content, 'lxml')  # Створюю обєкт Soup  і вказую анілізатор

        a = html.find_all('div', class_='description-block')
        for i in a:
            i = i.find('a')
            i = i['href']
            f = open('catalog.txt', 'a')
            f.write(i+'\n')
            f.close()