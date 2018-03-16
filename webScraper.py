# Libraries
import time
import urllib
import bs4
import requests
import csv
# Files and functions
from links import getLinks
from headings import getHeaders
from paragraphs import getParagraphs
from images import getImages
from images import storeImages
from tables import getTables

# GLOBAL DECLARATIONS
target_URL = input("Enter target URL - ")
# response = requests.get(target_URL)
# html = response.text
# soup = bs4.BeautifulSoup(html, "html.parser")
# print (soup)
# print (soup.head.title.string)


def testSoup(url):
	'''
		function that tests soup objects
	'''
	# print (soup)
	print (soup.head.title.string)

def writeToFile(list_data):
	file = open("test.txt", "w+")
	for item in list_data:
		file.write("%s\n" % item)
	


choice = input("What would you like to scrape? \n1-Headings 2-Links 3-Images 4-Text in BoldFace 5-Paragraphs 6-Tables\n")
ch = int(choice)
# print ("CHoice is - {}".format(ch))
print("\n")
if (ch==1):
	headers = getHeaders(target_URL)
	print ("\n".join(headers))
	writeToFile(headers)

elif (ch==2):
	links = getLinks(target_URL)
	print ("\n".join(links))
	writeToFile(links)
	
elif (ch==3):
	# urllib.request.urlretrieve("http://djcsi.co.in/Committee_2017-18/Bhavya.jpg", "images/local-filename.jpg")
	images = getImages(target_URL)
	print ("\n".join(images))
	storeImages(target_URL,images)
	print ("Images have been saved to the /images folder")


elif (ch==4):
	pass

elif (ch==5):
	par = getParagraphs(target_URL)
	print ("\n".join(par))
	writeToFile(par)

elif (ch==6):
	tables = getTables(target_URL)
	print (tables)


		

	
	