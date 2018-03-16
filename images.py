# Libraries
import time
from urllib.parse import urlparse
import urllib
import bs4
import requests


def getImages(url):
	'''
	funtion retrieves all src attributes of img tag
	stores them in a list
	returns the list
	'''
	response = requests.get(url)
	html = response.text
	soup = bs4.BeautifulSoup(html, "html.parser")
	output = []
	print  ("Images - \n")
	# print(soup.find_all("a"))
	# print ("Loop starts - ")
	stuff = soup.select("img")
	for data in stuff:
		if data.get("src") not in output:
			output.append(data.get("src"))
		else:
			break
	# print (output)
	return output

def storeImages(url, img_list):
	o = urlparse(url)
	# print (o)
	# print (o.netloc)
	domain_url = o.netloc
	for img_name in img_list:
		new_url = domain_url+"/"+img_name
		# print(new_url)
		img_arr = img_name.split("/")
		# print(img_arr[-1])
		urllib.request.urlretrieve("http://"+new_url, "images/"+img_arr[-1])