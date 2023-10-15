# name1 ='Linne'
# name2 ='Heaven'

# print(f'{name1} and {name2} are friends')
import numpy as np


friends = np.array(['tom', 'jane', 'Brian', 'carol', 'jack'])

i = 0
for friend in enumerate(friends):
    print(f'{i+1}:{friend}')
    i += 1
# import requests
# from bs4 import BeautifulSoup

# url = 'https://www.bbc.com/news/world'

# response = requests.get(url)
# element = BeautifulSoup(response.text, 'lxml')

# tags = element.find_all('h3', class_='gs-c-promo-heading__title gel-pica-bold nw-o-link-split__text')

# i = 1
# for tag in tags:
#     print(f'{i}:{tag.getText()}')
#     i += 1
