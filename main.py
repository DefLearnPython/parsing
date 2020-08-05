import  requests


with open('catalog_list.txt', 'r') as f:
    for url in f:
        r = requests.get(url)
        print(str(url) + '-----' + str(r))