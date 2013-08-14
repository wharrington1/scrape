#!/usr/bin/python

from bs4 import BeautifulSoup
from urllib2 import urlopen

site = "http://richmond.craigslist.org/rea/"
table = BeautifulSoup(urlopen(site))
items = table('p')
linkdict = {}
i = 0
for item in items[:-1]:
    i=i+1
    itempostlink = item('a')[0]['href']
    itemlink = site[:-5] + itempostlink
    linkdict[i] = itemlink

for i, link in linkdict.iteritems():
    print i, linkdict[i]
    images = BeautifulSoup(urlopen(linkdict[i]))('img')
    imagecounter = 0
    for image in images:
        imagecounter +=1
        image_url =image['src']
        print image_url
        image = urlopen(image_url)
        local = open("c:\\temp\\"+str(i)+"."+str(imagecounter)+".jpg",'wb')
        local.write(image.read())
        local.close()
    print
