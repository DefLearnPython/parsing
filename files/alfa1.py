from bs4 import BeautifulSoup as BS
import requests

catalog = []
with open("catalog.txt", 'r') as f:  # Відкриваю файл в режимі читання
    for line in f:  # Построчно прочитую файл
        line = 'https://www.rusplitka.ru'+line
        catalog.append(line)  # Додаю строку в перемінну як частину списка
catalog = catalog[:2500]
k = 1
for cat in catalog:
    print(str(k)+'/'+str(len(catalog)))
    k += 1
    cat = cat.strip()
    df = cat.find('/oputstvuyuschie-tovary/')
    if df != -1:
        with open('oputstvuyuschie_tovary.txt''a') as f:
            f.write(cat + '\n')
        continue
    content = requests.get(cat)
    html = BS(content.content, 'html.parser')  # Створюю обєкт Soup  і вказую анілізатор
    if content.status_code != 200:
        print('Забанили')

    a = html.find('div', class_='plitka grid')
    a = a.find_all_next('a', class_='title')
    for i in a:
        i = i['href']
        with open('full_cataloc.txt', 'a') as f:
            f.write(i+'\n')

print(1)

