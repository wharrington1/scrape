#!/usr/bin/python
#-----------------------------------------
# Use BeautifulSoup to read the online
# book Python for Beginners.
#-----------------------------------------
from bs4 import BeautifulSoup
import urllib2
 
url = "http://www.pythonforbeginners.com"
 
content = urllib2.urlopen(url).read()
 
soup = BeautifulSoup(content)
 
#print soup.prettify()
 
print soup.title.string
print soup.p
print soup.a

# Print the text.
print(soup.get_text())
