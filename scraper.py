import requests
from bs4 import BeautifulSoup
page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")
#print(page.content)
soup = BeautifulSoup(page.content, 'html.parser')
#print(soup.prettify())
#print(list(soup.children))
html = list(soup.children)[2]
print(list(html.children))
body = list(html.children)[3]
print("\n")
print(list(body.children))
list = list(body.children)[1]
print(list.get_text())
print("\n\n\n")

#finding all instances of a tag at onces
soup = BeautifulSoup(page.content, 'html.parser')
s = soup.find_all('p')
s2 = soup.find_all('p')[0].get_text()
print(s2)