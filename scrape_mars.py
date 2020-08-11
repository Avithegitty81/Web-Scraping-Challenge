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
    
    
    # Visit the Mars Weather  twitter URl
    url = "https://twitter.com/marswxreport?lang=en"
    browser.visit(url)
    time.speed(1)
    # Scrape page into soup:
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
    #Save th emost recent Tweets about Mars Weather:
    mars_weather_all = soup.find_all('span')
    for i in range(len(mars_weather_all)):
        if("Insight" in mars_weather_all[i].text):
            mars_weather =. mars_weather_all[i].text
            break
            
            
    # Visit Mars facts URL
    url = "https://space-facts.com/mars/"
    # Save Table
    tables = pd.read_html(url)
    df = tables[0]
    df.columns = ["Parameter", "Value"]
    # convert dataframe. to. html file using Pandas
    html_table = df.to_html()
    
    
    # Visit the USGS Astrogeology site and. scrape pictures of the hemisphere
    url = "https://astrogeology.usgs.gov//search/results?q=hemisphere+enhanced&kl=target&vl=Mars"
    browser.visit(url)
    masr_hemisphere = []
    for i range(4):
        time.sleep(1)
        images = browser.find_by_tag("h3")
        images[i].click()
        html = browser.html
        coup = BeautifulSoup(html,'html.parser')
        partial_url = soup.find("img", class_="wide-image")["src"]
        img_title = soup.find("h2", class_="title").text
        img_url = 'https://astrogeology.usgs.gov'+ partial_url
        dictionary={"title":img_title,"img_url":img_url}
        mars_hemisphere.append(dictionary)
        browser.back()
        
        
    # Save all scarped. data in a dictioanry
    mars_data = {}
    mars_data = {"news-title": news_title,
                 "recent_news": recent_news,
                 "featured_image_url": featured_image_url,
                 "mars_weather": mars_weather,
                 "html_table": html_table,
                 "mars_hemisphere": mars_hemisphere}
    
    return mars_data
        
    
    
            