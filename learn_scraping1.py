import requests
from bs4 import BeautifulSoup
import csv

URL = "https://finance.yahoo.com/quote/MSFT?p=MSFT&.tsrc=fin-srch"
r = requests.get(URL)
soup = BeautifulSoup(r.content, 'html5lib')

data = soup.findAll('span')
for d in data:
	print(d)
	print("\n")
	try:
		print(d.text)
		print("\n\n")
	except:
		print()


