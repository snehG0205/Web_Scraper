# Libraries
import time
import urllib
import bs4
import requests

def getParagraphs(url):
	'''
	funtion retrieves all paragraph
	text enclosed in p tags
	'''
	print("Paragraphs - ")
	response = requests.get(url)
	html = response.text
	soup = bs4.BeautifulSoup(html, "html.parser")
	output = []
	for para in soup.find_all('p'):
		output.append("P - "+para.text)
	
	return output

