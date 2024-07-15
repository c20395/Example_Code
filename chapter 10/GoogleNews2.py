# Example 10.9 feedparser to read news feeds
# https://codeloop.org/how-to-read-google-rss-feeds-in-python/
# pip install feedparser
import feedparser

def getHeadlines(rss_url):
    headlines = []
    feed = feedparser.parse(rss_url)
    for newsitem in feed['items']:
        #print(newsitem)
        item = newsitem['title']+"\n"+newsitem['link']+"\n"+newsitem['published']
        headlines.append(item)
    return headlines

allheadlines = []
newsurls = {
    'googlenews': 'https://news.google.com/news/rss/',
    'bbcnews':"http://feeds.bbci.co.uk/news/rss.xml"
}

for key, url in newsurls.items():   
    allheadlines.extend(getHeadlines(url))

for hl in allheadlines:
    print(hl)
    print("="*80)
