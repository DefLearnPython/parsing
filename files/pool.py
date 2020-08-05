from bs4 import BeautifulSoup as BS
import requests

from multiprocessing import Pool

file = open('catalog.txt', 'r')
file_list = []
for page in file:
    file_list.append(page)

characters_list = []
k = 1
def x(cat):
    f = file_list.index(cat)
    print(f)
    cat = cat.strip()
    cat = 'https://www.rusplitka.ru'+cat
    df = cat.find('/oputstvuyuschie-tovary/')
    if df != -1:
        with open('oputstvuyuschie_tovary.txt''a') as f:
            f.write(cat + '\n')
    if df == -1:
        content = requests.get(cat)
        html = BS(content.content, 'html.parser')  # Створюю обєкт Soup  і вказую анілізатор
        if content.status_code != 200:
            print('Забанили')
        if content.status_code == 200:
            a = html.find('div', class_='plitka grid')
            a = a.find_all_next('a', class_='title')
            for i in a:
                i = i['href']
                with open('../full_cataloc.txt', 'a') as f:
                    f.write(i + '\n')


if __name__ == '__main__':
    with Pool(10) as p:
        p.map(x, file_list)