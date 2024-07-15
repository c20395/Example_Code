#Example 10.7 Read RSS news feeds
# https://www.w3resource.com/python-exercises/basic/python-basic-1-exercise-8.php
# pip install BeautifulSoup4
# pip install lxml

import bs4
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen

url="https://news.google.com/news/rss"
url="http://feeds.bbci.co.uk/news/rss.xml"
Client=urlopen(url)
page=Client.read()
Client.close()

soup_page=soup(page,"xml")
news_list=soup_page.findAll("item")
word = "UK"
# Print news contains key words
for news in news_list:
    if word in news.title.text:
        #print(news)
        print(news.title.text)
        print(news.description.text)
        print(news.link.text)
        print(news.pubDate.text)
        print("="*80)
