# USC_WebScraping_HW
The purpose of this exercise is to scrape data from web pages using Beautiful Soup for parsing most complex html and Pandas for easiest cases. After getting results, I used Flask to create an API to show and update results. 

File description:

Mars_news.ipynb: Jupyter notebook file to work and get all data from different sources.
scrape_mars.py: Same file in Python format, all instructions were converted into one function.
app.py: API using Flask to show results and save into MongoDB.
templates/index.html: HTML template with variables invoked from app.py

Other Resources
chromedriver.exe: Required for parsing html using Splinter.
config.py: Credentials

Tip: Before execute Flask API (app.py), check if Mongo is running.
