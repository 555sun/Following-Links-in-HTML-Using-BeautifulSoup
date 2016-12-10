import urllib
from BeautifulSoup import *
k=raw_input("Enter the URL of Site you want to parse \n")
i= int(raw_input("Enter the count "))
j= int (raw_input("Enter the position "))
t=list()
while i>0:
    soup=urllib.urlopen(k).read()
    soup=BeautifulSoup(soup)
    tags=soup('a')
    for tag in tags:
        x=tag.get('href',None)
        t.append(x)
    print "Retrieving URL === ",t[j-1]
    k=t[j-1]
    i=i-1
    t=list()
    

          
    
