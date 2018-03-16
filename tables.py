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
	text_data = []
	k = 0
	for tr in rows:
		cols = tr.findAll('th')
		for th in cols:
			text = th.text
			# print (text)
			text_data.append(text)
			k = k+1
		cols = tr.findAll('td')
		for td in cols:
			# text = ''.join(td)
			text = td.text
			# print (text)
			text_data.append(text)

	output.append(text_data)


	writer = csv.writer(open("res.csv","w+"))
	i=0
	j=0
	for j in range(0,len(output)):
		while i<k:
			writer.writerow(output[j])
		writer.writerow('\n')

	
		

	# print(k)
	
	return output
	
   