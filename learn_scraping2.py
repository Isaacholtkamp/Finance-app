import requests
from bs4 import BeautifulSoup
import csv

URL = "https://finance.yahoo.com/quote/MSFT?p=MSFT"
r = requests.get(URL)
soup = BeautifulSoup(r.content, 'html5lib')
#print(soup.prettify())

#figuring out general commands and how to get table data
#tables = soup.findAll('table')
#table_data = tables[0].findAll('tr')
#print(table_data)
#print("\n")
#values = table_data[0].findAll('td')
#print(values)
#print("\n")
#specific = values[0].findAll('span')
#print(specific)
#print("\n")

#print(specific[0].text)

#trying to get all texts but have issues with ranges and special characters
tables = soup.findAll('table')

for table in tables:
	table_data = table.findAll('tr')
	for val in table_data:
		values = val.findAll('td')
		for spec in values:
			specific = spec.findAll('span')
			try:
				print(specific[0].text)
			except:
				print(specific)
				print("\n")
				
				


	

