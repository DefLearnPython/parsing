import requests
from bs4 import BeautifulSoup as BS
import re


"""
headers = [
	'Код товара',class_="label label-force label-primary js-product-code" код товара
	'Название',h1
	'Краткое описание',class="text expansible full"
	'РРЦ',class="bold"
	'Размер',class="list-inline list-commas inline"
	'Категория',itemprop="name"
	'Подробное описание',
	'Материал',
	'Цвет'class="tagsBlock" по цвету
]
num_list = [int(num) for num in filter(lambda num: num.isnumeric(), word_list)]
"""


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

	for url_ in links :
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

		data.append([url_, title, code_, description, price])
		print(f"Товар со страницы {url_} добавлен.")
	return data


