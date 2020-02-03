# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
import datetime as dt
import time


browser = Browser("chrome", executable_path="chromedriver", headless=False)

# Visit initial Mars URL
url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url)

# Parse the resulting html with soup
html = browser.html
hemi_soup = BeautifulSoup(html, 'html.parser')

# find html related to the images
hemi_links = hemi_soup.find_all('a', class_="itemLink product-item")

# create a blank list
image_links = []

# parse and append links to list
for hemi_link in hemi_links:
    image_links.append(hemi_link['href'])

# create a set from the list to eliminate duplicates
image_links = set(image_links)

# loop the list of links
for image_link in image_links:
    # visit link page
    url = f'https://astrogeology.usgs.gov{image_link}'
    browser.visit(url)

    # get html soup
    html = browser.html
    image_soup = BeautifulSoup(html, 'html.parser')

    tifs = []
    # find TIF links and append
    links = image_soup.find_all('a')
    for link in links:
        if link.text == 'Original':
            tifs.append(link['href'])
    time.sleep(5)

    # return data


# browser.quit()
