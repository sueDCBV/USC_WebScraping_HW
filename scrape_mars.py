# Dependencies
from bs4 import BeautifulSoup as bs
import requests
import tweepy
import pymongo
from splinter import Browser
import json
from config import consumer_key,consumer_secret,access_token,access_token_secret
import pandas as pd

# Scrape function
def Scrape():

    # Empty dictionary
    dic_mars_info = {}

    ## Mars News
    print("Scraping Mars News")
    #Initialize chrome browser
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)

    #Open url in browser
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)

    #Parsing html
    html = browser.html
    soup = bs(html, 'html.parser')
    #print(soup.prettify())

    #Scrapping latest news: title and content
    news_title = soup.find('div', 'content_title', 'a').text
    news_content = soup.find('div', 'rollover_description_inner').text

    # Adding to dict
    dic_mars_info["news_title"] = news_title
    dic_mars_info["news_content"] = news_content

    print("Mars News Results:")
    print(news_title,news_content)


    ## JPL Mars URL
    print("Scraping JPL Nasa")
    #Open url in browser
    url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url)

    #Parsing html
    html = browser.html
    soup = bs(html, 'html.parser')
    #print(soup.prettify())

    #Scraping feature image of mars
    results = soup.find("article")["style"]

    #Cleaning results
    extension=(results.split("url('",1)[1]).rstrip("');")

    link = "https://www.jpl.nasa.gov"
    featured_image_url = link + extension

    # Adding to dict
    dic_mars_info["JPL_image"] = featured_image_url

    print("JPL NASA Results:")
    print(featured_image_url)

    ## Tweeter Mars Weather
    print("Scraping Tweeter Mars Weather")


    # Setup Tweepy API Authentication
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

    # Target User
    target_user = "@MarsWxReport"

    # Get last tweet or mars weather
    public_tweets = api.user_timeline(target_user,count=1)
    type(public_tweets)

    mars_current_weather=public_tweets[0]["text"]

    # Adding to dict
    dic_mars_info["mars_weather"] = mars_current_weather

    print("Mars Weather Tweet Results:")
    print(mars_current_weather)

    ## Mars Facts with Pandas
    print("Scraping Mars Facts")


    # Mars Facts URL
    url = "https://space-facts.com/mars/"

    #Reading html with pandas library
    tables = pd.read_html(url)

    #Create dataframe and store results
    df = tables[0]
    df.columns = ['Description', 'Values']

    #Convert dataframe into html table
    html_table = df.to_html()

    # Adding to dict
    dic_mars_info["mars_facts_table"] = html_table

    print("Mars Facts Results:")
    print(html_table)

    ### Mars Hemispheres
    print("Scraping Mars Hemispheres")
    # Mars Hemispheres URL
    url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url)

    ## Mars Valles Marineris Hemisphere Enhanced
    # Empty urls
    hemisphere_image_urls = []

    #Click first image
    browser.click_link_by_partial_text('Valles Marineris Hemisphere Enhanced')

    # Parsing address
    html = browser.html
    soup = bs(html, 'lxml')
    #print(soup.prettify())

    # Store link
    img_url_valles = soup.find('div', 'downloads').a['href']

    # Create dictionary
    dic_mars_valles = {
        "title": "Valles Marineris Hemisphere",
        "img_url": img_url_valles
    }

    # Filling Dictionary
    hemisphere_image_urls.append(dic_mars_valles)

    ##Cerberus Hemisphere
    browser.visit(url)

    #Click first image
    browser.click_link_by_partial_text('Cerberus Hemisphere Enhanced')

    # Parsing address
    html = browser.html
    soup = bs(html, 'lxml')
    #print(soup.prettify())

    # Store link
    img_url_cerberus = soup.find('div', 'downloads').a['href']

    # Create dictionary
    dic_mars_cerberus = {
        "title": "Cerberus Hemisphere",
        "img_url": img_url_cerberus
    }

    # Filling Dictionary
    hemisphere_image_urls.append(dic_mars_cerberus)

    ##Schiaparelli Hemisphere
    browser.visit(url)
    #Click first image
    browser.click_link_by_partial_text('Schiaparelli Hemisphere Enhanced')

    # Parsing address
    html = browser.html
    soup = bs(html, 'lxml')
    #print(soup.prettify())

    # Store link
    img_url_schiaparelli = soup.find('div', 'downloads').a['href']

    # Create dictionary
    dic_mars_schiaparelli = {
        "title": "Schiaparelli Hemisphere",
        "img_url": img_url_schiaparelli
    }

    # Filling Dictionary
    hemisphere_image_urls.append(dic_mars_schiaparelli)

    ##Syrtis Major Hemisphere
    browser.visit(url)
    #Click first image
    browser.click_link_by_partial_text('Syrtis Major Hemisphere Enhanced')

    # Parsing address
    html = browser.html
    soup = bs(html, 'lxml')
    #print(soup.prettify())

    # Store link
    img_url_syrtis = soup.find('div', 'downloads').a['href']

    # Create dictionary
    dic_mars_syrtis = {
        "title": "Syrtis Major Hemisphere",
        "img_url": img_url_syrtis
    }

    # Filling Dictionary
    hemisphere_image_urls.append(dic_mars_syrtis)

        # Adding to dict
    dic_mars_info["mars_hemisphere_images"] = hemisphere_image_urls

    print("Mars Hemisphere Results:")
    print(hemisphere_image_urls)

    return dic_mars_info