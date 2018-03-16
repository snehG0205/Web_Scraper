# Libraries
import time
import urllib
import bs4
import requests

def getLinks(url):
	'''
	funtion retrieves all links (values in href)
	stores them in a list
	returns the list
	'''
	response = requests.get(url)
	html = response.text
	soup = bs4.BeautifulSoup(html, "html.parser")
	output = []
	print  ("Links - \n")
	# print(soup.find_all("a"))
	# print ("Loop starts - ")
	stuff = soup.select("a")
	for data in stuff:

		if data.get("href") == "#":
			continue
		else:
			if data.get("href") not in output:
				output.append(data.get("href"))

	return output
		
	



