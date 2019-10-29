#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Setup Dependencies 
# !pip install splinter
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
import requests
from splinter import Browser


# In[2]:

def init_browser(): 

    # Set up Chromedriver to visit Nasa's Mars News
    executable_path = {'executable_path': 'chromedriver.exe'}
    return Browser('chrome', **executable_path, headless=False)

# Importable Dictionary 
mars_info = {}


# # Mars News from NASA.gov

# In[3]:

def scrape_mars_news():
    try: 
        # Initialize browser 
        browser = init_browser()

        # Scrape the NASA Mars News Site and collect the latest News Title and Paragraph Text. 
        url = 'https://mars.nasa.gov/news/'
        browser.visit(url)

        html = browser.html

        # Parse HTML with Beautiful Soup
        soup = BeautifulSoup(html, 'html.parser')

        # Retrieve the latest  news title and news_paragraph
        news_title = soup.find('div', class_='content_title').find('a').text
        news_p = soup.find('div', class_='article_teaser_body').get_text()

        # Dictionary append
        mars_info['news_title'] = news_title
        mars_info['news_paragraph'] = news_p

        return mars_info

    finally:

        browser.quit()


# # Featured Mars Image

# In[4]:

def scrape_mars_image():
    try: 

        # Initialize browser 
        browser = init_browser()

        # JPL Mars Space Images - Featured Image
        image_featured = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
        browser.visit(image_featured)

        # Parse HTML Object 
        html_image = browser.html

        soup = BeautifulSoup(html_image, 'html.parser')

        # Retrieve background-image url 
        featured_image_url  = soup.find('article')['style'].replace('background-image: url(','').replace(');', '')[1:-1]

        # Website URL 
        main_url = 'https://www.jpl.nasa.gov'

        # Concatenate website URL 
        featured_image_url = main_url + featured_image_url

        # Display full URL of the featured image
        featured_image_url

        # Dictionary append
        mars_info['featured_image_url'] = featured_image_url 
        
        return mars_info
    finally:

        browser.quit()


# # Weather on Mars

# In[5]:

def scrape_mars_weather():

    try: 

        # Initialize browser 
        browser = init_browser()

        # Scrape the latest Mars Weather tweets
        weather_url = 'https://twitter.com/marswxreport?lang=en'
        browser.visit(weather_url)

        # Parse HTML Object 
        html_weather = browser.html

        soup = BeautifulSoup(html_weather, 'html.parser')

        # Find all elements that contain tweets
        latest_tweets = soup.find_all('div', class_='js-tweet-text-container')

        # Retrieve only elements that display weather related words
        for tweet in latest_tweets: 
            mars_weather = tweet.find('p').text
            if 'Sol' and 'pressure' in mars_weather:
                print(mars_weather)
                break
            else: 
                pass

        # Dictionary append
        mars_info['mars_weather'] = mars_weather
        
        return mars_info
    finally:

        browser.quit()

# # Facts on Mars

# In[6]:

def scrape_mars_facts():


    # Visit Mars facts webpage 
    facts_url = 'http://space-facts.com/mars/'

    # Parse the url with Pandas
    mars_facts = pd.read_html(facts_url)

    # Facts DataFrame
    mars_df = mars_facts[0]

    # Investigate column headers 
    mars_df.columns

    # Set the index column 
    mars_df.set_index('Mars - Earth Comparison', inplace=True)

    # Convert data to html 
    mars_data = mars_df.to_html()

    # Dictionary append
    mars_info['mars_facts'] = mars_data

    return mars_info


# # The Hemispheres of Mars

# In[7]:

def scrape_mars_hemispheres():

    try: 

        # Initialize browser 
        browser = init_browser()

        # Visit Website through splinter  
        hemispheres = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
        browser.visit(hemispheres)

        # HTML Object 
        html_hemispheres = browser.html

        soup = BeautifulSoup(html_hemispheres, 'html.parser')

        # Retreive any item that contains Mars hemispheres info
        items = soup.find_all('div', class_='item')

        # Create empty placeholder for the URL 
        hemisphere_image_urls = []

        # Set main url variable
        hemispheres_main_url = 'https://astrogeology.usgs.gov'

        # Loop through the item and store Title, Full Image URL, Information
        for i in items: 
            title = i.find('h3').text
            
            partial_img_url = i.find('a', class_='itemLink product-item')['href']
            browser.visit(hemispheres_main_url + partial_img_url)
            
            partial_img_html = browser.html
            
            soup = BeautifulSoup( partial_img_html, 'html.parser')
                
            img_url = hemispheres_main_url + soup.find('img', class_='wide-image')['src']
                
            hemisphere_image_urls.append({"title" : title, "img_url" : img_url})
            

        mars_info['hemisphere_image_urls'] = hemisphere_image_urls

        
        # Return mars_data dictionary 

        return mars_info
    finally:

        browser.quit()


# In[ ]:




