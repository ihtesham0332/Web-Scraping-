import requests
from bs4 import BeautifulSoup
web =requests.get("https://www.tutorialsfreak.com/")
soup=BeautifulSoup(web.content,"html.parser")
#print(soup.name)
#comments
com=soup.p.string
#print(com) 
print(soup.body.prettify())
#find all type of data in paragraph
soup.find_all("p")
soup.find_all("a")