import requests
from bs4 import BeautifulSoup
web =requests.get("https://www.tutorialsfreak.com/")
#print(web.content)
#print(web)
#print(web.status_code)
soup=BeautifulSoup(web.content,"html.parser")
#print(soup.prettify())
"""print(soup.title)#print the title of paragraph
print(soup.title.name)# print the title name of the website
print(soup.p) #print the first paragraph
print(soup.a)#print the  anker tage
print(soup.h1)
print(soup.body)
print(soup.head)#print the heading"""
#function in beautiful scoup
#print(soup.find("h1"))
#Navigable string 
#print(soup.p.string)
print(soup.a.string)
