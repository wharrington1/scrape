#!/usr/bin/python
from BeautifulSoup import BeautifulSoup   
from urllib2 import urlopen               

site = "http://sfbay.craigslist.org/rea/" 
html = urlopen(site)                      
soup = BeautifulSoup(html)                
postings = soup('p')                      

for post in postings:                     
    print post('a')[0].contents[0]        
    print post('a')[0]['href']     
