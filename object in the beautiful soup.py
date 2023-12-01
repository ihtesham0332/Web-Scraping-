"""Tag
Navigable String
BeautifulSoup
Comments"""
import requests
from bs4 import BeautifulSoup
web=requests.get("https://www.tutorialsfreak.com/")
print(web.content)
soup=BeautifulSoup(web.content,"html.parser")
tag=soup.html
print(tag.h1)
print(tag.h2)
print(tag.h3)
print(type(tag))