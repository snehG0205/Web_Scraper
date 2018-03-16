# Libraries
import time
import urllib
import bs4
import requests

def getHeaders(url):
	'''
	funtion retrieves all headings
	that are enclosed in h1 through h6
	'''
	print("Headings - ")
	response = requests.get(url)
	html = response.text
	soup = bs4.BeautifulSoup(html, "html.parser")
	output = []
	for heading in soup.find_all('h1'):
		output.append("h1 - "+heading.text)
		# print(heading.text)

	for heading in soup.find_all('h2'):
		output.append("h2 - "+heading.text)
		# print(heading.text)

	for heading in soup.find_all('h3'):
		output.append("h3 - "+heading.text)
		# print(heading.text)

	for heading in soup.find_all('h4'):
		output.append("h4 - "+heading.text)
		# print(heading.text)

	for heading in soup.find_all('h5'):
		output.append("h5 - "+heading.text)
		# print(heading.text)

	for heading in soup.find_all('h6'):
		output.append("h6 - "+heading.text)
		# print(heading.text)
	return output;
	