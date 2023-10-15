# name1 ='Linne'
# name2 ='Heaven'

# print(f'{name1} and {name2} are friends')


# import numpy as np


# friends = np.array(['tom', 'jane', 'Brian', 'carol', 'jack'])

# i = 0
# for friend in enumerate(friends):
#     print(f'{i+1}:{friend}')
#     i += 1


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

from google.colab import files

uploaded_file = files.upload()
uploaded_file_name = next(iter(uploaded_file))

import cv2
import matplotlib.pyplot as plt

img = cv2.imread(uploaded_file_name)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

height = img.shape[0]
width = img.shape[1]


img = cv2.resize(img, None, fx=0.1, fy=0.1)
img = cv2.resize(img, (width, height),interpolation=cv2.INTER_NEAREST)

plt.imshow(img)
