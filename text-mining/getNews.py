# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import wordgram
import urllib2
import sys
if __name__ == "__main__":
	reload(sys)
	sys.setdefaultencoding("utf-8")

user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }
menu = {
	1:"정치",
	3:"사회",
}
for i in "13" :
	url = "http://www.ytn.co.kr/news/news_list_010"+i+".html"

	htmltext = urllib2.urlopen(url).read()
	soup = BeautifulSoup(htmltext, from_encoding="utf-8")

	newsList = soup.findAll('dl',attrs={"class","news_list_v2014"})
	newsLink = []
	for news in newsList:
		newsLink.append('http://www.ytn.co.kr'+news.find('a')['href'])

	fileContent=""
	content_dict=[]

	for link in newsLink : 
		htmltext = urllib2.urlopen(link).read()
		soup = BeautifulSoup(htmltext, from_encoding="utf-8")
		content = soup.find('div',attrs={"class","newsContent_text"}).get_text()
		content_dict.append(wordgram.wordgram_analyze_string(content))
	print menu[int(i)]+"\n"
	result = wordgram.addup(content_dict)
	wordgram.print_dict(result)
	# print result