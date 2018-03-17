import time
import urllib
import bs4
import requests
import csv

def getTables(url):

	print("Tables - ")
	response = requests.get(url)
	html = response.text
	soup = bs4.BeautifulSoup(html, "html.parser")
	output = []
	table = soup.find('table')
	rows = table.findAll('tr')
	k = 0
	for tr in rows:
		cols = tr.findAll('th')
		for th in cols:
			text = th.text
			# print (text)
			output.append(text)
			k = k+1
		cols = tr.findAll('td')
		for td in cols:
			# text = ''.join(td)
			text = td.text
			# print (text)
			output.append(text)

	# print(k)
	file = open("table.txt", "w+")
	temp = 1
	for item in output:
		file.write("%s| \t" % item)
		if temp%k == 0:
			file.write("\n")
		temp = temp+1
	return output
	
   