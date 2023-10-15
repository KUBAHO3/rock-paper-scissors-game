# Define variables name1 and name2 with values 'Linne' and 'Heaven' respectively.
name1 ='Linne'
name2 ='Heaven'

# Print a string that includes the values of name1 and name2.
print(f'{name1} and {name2} are friends')


# Import the NumPy library and create a NumPy array called friends.
import numpy as np
friends = np.array(['tom', 'jane', 'Brian', 'carol', 'jack'])
# Iterate over each element of friends using a for loop and the enumerate() function.
i = 0
for friend in enumerate(friends):
    # Print the index of each friend along with the friend's name.
    print(f'{i+1}:{friend}')
    i += 1


# Import the requests and BeautifulSoup libraries.
import requests
from bs4 import BeautifulSoup
# Define a URL to scrape news headlines from.
url = 'https://www.bbc.com/news/world'
# Send a GET request to the URL using requests.get() and store the response in the response variable.
response = requests.get(url)
# Create a BeautifulSoup object called element by passing the response text and parser type ('lxml') to the BeautifulSoup constructor.
element = BeautifulSoup(response.text, 'lxml')
# Use the find_all() method of the element object to find all HTML tags with the specified class name ('gs-c-promo-heading__title gel-pica-bold nw-o-link-split__text').
# Store the found tags in the tags variable.
tags = element.find_all('h3', class_='gs-c-promo-heading__title gel-pica-bold nw-o-link-split__text')
i = 1
# Iterate over each tag in tags using a for loop.
for tag in tags:
    # Print the index of each tag along with its text content using tag.getText().
    print(f'{i}:{tag.getText()}')
    i += 1


# Import the files module from the google.colab library.
from google.colab import files
# Upload a file from the user's local machine using files.upload().
uploaded_file = files.upload()
# Store the name of the uploaded file in the uploaded_file_name variable.
uploaded_file_name = next(iter(uploaded_file))

# Import the OpenCV (cv2) and Matplotlib (plt) libraries.
import cv2
import matplotlib.pyplot as plt
# Read the uploaded image file using cv2.imread().
img = cv2.imread(uploaded_file_name)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
height = img.shape[0]
width = img.shape[1]
# Resize the image to 10% of its original size using cv2.resize().
img = cv2.resize(img, None, fx=0.1, fy=0.1)
# Resize the image back to its original size using nearest-neighbor interpolation.
img = cv2.resize(img, (width, height),interpolation=cv2.INTER_NEAREST)
# Display the image using plt.imshow().
plt.imshow(img)