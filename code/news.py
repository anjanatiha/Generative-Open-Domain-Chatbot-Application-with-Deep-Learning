import bs4
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
import feedparser
from lib import nltk

def fetch_news(newsurls):

	for key,url in newsurls.items():
		try:
			news_url=url
			Client=urlopen(news_url)
			xml_page=Client.read()
			Client.close()

			soup_page=soup(xml_page,"xml")
			news_list=soup_page.findAll("item")
			# Print news title, url and publish date
			for news in news_list:
			  print(news.title.text)
			  print(news.link.text)
			  print(news.pubDate.text)
			  print("-"*60)

		except:
			print('could not fetch url:', url)



worldnewsurls = {
	'bbcnews'       : 'http://feeds.bbci.co.uk/news/world/rss.xml',
	'cnn'           : 'http://rss.cnn.com/rss/edition_world.rss',
	'guardian'      : 'https://www.theguardian.com/world/rss',
	'Reuters'       : 'http://feeds.reuters.com/Reuters/worldNews',
	'washingtonpost': 'http://feeds.washingtonpost.com/rss/world',
	'aljajeera'     : 'https://www.aljazeera.com/xml/rss/all.xml',
	'googlenews'    : 'https://news.google.com/news/rss/',
	'yahoonews'     : 'http://news.yahoo.com/rss/',
	'yahooworld'    : 'https://www.yahoo.com/news/rss/world',    
	'buzzfeed'      : 'https://www.buzzfeed.com/world.xml'
}

buisnessnewsurls = {
	'cnnmoney' : 'http://rss.cnn.com/rss/money_topstories.rss', 
	'cnbc' : 'http://www.cnbc.com/id/19746125/device/rss/rss.xml', 
	'yahoofinance' : 'https://finance.yahoo.com/news/rssindex', 
	'investing' : 'https://www.investing.com/rss/news.rss', 
	'investing' : 'https://prod-qt-images.s3.amazonaws.com/production/c/feed.xml', 
	'chicagobusiness' : 'http://www.chicagobusiness.com/section/news?template=rss&mime=xml', 
	'businessinsider' : 'http://markets.businessinsider.com/rss/news'
}

technewsurls = {
	'techmeme'          :'https://www.techmeme.com/feed.xml',
	'TechCrunch'        :'http://feeds.feedburner.com/TechCrunch',
	'arstechnica'       :'http://feeds.arstechnica.com/arstechnica/technology-lab',
	'reddittech'        :'https://www.reddit.com/r/technology/.rss',
	'computerworld'     :'https://www.computerworld.com/index.rss',
	'nytimestech'       :'http://rss.nytimes.com/services/xml/rss/nyt/Technology.xml',
	'cnettech'          :'https://www.cnet.com/rss/news/',
	'washingtonposttech':'http://feeds.washingtonpost.com/rss/business/technology',
	'huffingtonposttech':'https://www.huffingtonpost.com/section/technology/feed',
	'alleyinsider'      :'http://feeds.feedburner.com/typepad/alleyinsider/silicon_alley_insider',
	'reuterstech'       :'http://feeds.reuters.com/reuters/technologyNews',
	'mirrortech'        :'https://www.mirror.co.uk/tech/?service=rss',
	'howtogeektech'     :'https://feeds.howtogeek.com/HowToGeek'

}

fashionnewsurls = {
	'elle'            : 'https://www.elle.com/rss/all.xml/',
	'vogue'           : 'https://www.vogue.com/feed',
	'nytimesfasion'   : 'https://www.nytimes.com/svc/collections/v1/publish/http://www.nytimes.com/section/fashion/rss.xml',
	'whowhatwear'     : 'http://www.whowhatwear.com/rss',
	'popsugar'        : 'https://www.popsugar.com/fashion/feed',
	'fashionmagazine' : 'https://fashionmagazine.com/feed/',
	'lookbook'        : 'http://lookbook.nu/rss',
	'refinery29'      : 'https://www.refinery29.com/fashion/rss.xml'

}

def get_news(news_type):
	if news_type == 'world':
		fetch_news(worldnewsurls)
	elif news_type == 'buisness':
		fetch_news(buisnessnewsurls)
	elif news_type == 'tech':
		fetch_news(technewsurls)
	elif news_type == 'fashion':
		fetch_news(fashionnewsurls)
	else:
		fetch_news(worldnewsurls)
		print('news type not matched, showing world news')


def find_news(search_string, news_url_type_list):
	
	for news_url_type in news_url_type_list:
		for key,url in news_url_type.items():
			try:
				news_url=url
				Client=urlopen(news_url)
				xml_page=Client.read()
				Client.close()

				soup_page=soup(xml_page,"xml")
				news_list=soup_page.findAll("item")

				for news in news_list:
					title = news.title.text
					tok_match_count = nltk.sen_tok_match_count(search_string, title)
					if tok_match_count > 0:
						print(news.title.text)
						print(news.link.text)
						print(news.pubDate.text)
						print("-"*60)
			except:
				pass



news_url_type_list = [worldnewsurls, buisnessnewsurls, technewsurls, fashionnewsurls] 

#news_type = 'fashion'
#get_news(news_type)
search_string = "amazon"

find_news(search_string, news_url_type_list)