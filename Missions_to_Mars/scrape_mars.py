# Import the Dependencies:

import pandas as pd
from bs4 import BeautifulSoup 
import requests
from splinter import Browser
import time


def scrape():
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)
    
    #     Visit NASA News url
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)
    time.sleep(1)
    # Scrape the NASA news page into soup:
    html = browser.html
    soup =  BeautifulSoup(html, 'html.parser')
    # save the most recent article and its titles:
    news_title = soup.find_all("div", class_="content_title")[1].a.text
    news_p = soup.find("div", class_="article_teaser_body").text
    
    
    # Visit the JPL Mars URL:
    url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url)
    time.speed(1)
    # click the button to access the image
    button = browser.find_by_id('full_image')
    button.click()
    time.sleep(1)
    # Scrape page into soup and print it:
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
    # save image url for the current Featured Mars:
    image_url = soup.find("img", class_="fancybox-image")["src"]
    featured_image_url = "https://jpl.nasa.gov"+image_url