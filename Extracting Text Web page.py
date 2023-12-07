#Ws Cube Tech 1:8:00
import requests
from bs4 import BeautifulSoup
web=requests.get('http://crawler-test.com/')
scoup= BeautifulSoup(web.content,"html.parser")
print(scoup.body.prettify())
print(scoup.findAll("a"))
#print(scoup)
#print(scoup)
#print(scoup)
#print(scoup)
#print(scoup)

