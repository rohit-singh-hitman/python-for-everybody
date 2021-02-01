import urllib.request, urllib.parse, urllib.error
from urllib.request import urlopen
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
count = input("enter count")
c=int(count)
pos = input("enter position")
p=int(pos)
url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
i=0
for i in range(0,c):
    soup = BeautifulSoup(urlopen(url, context=ctx))
    a = soup.find_all('a', href=True)  # all <a href> links
    if len(a) < 3:  # no 3rd link
        break  # exit the loop
    url = urljoin(url, a[p-1]['href'])
    print(url)



#for i in range(0,p):
    #@for tag in tags:
        #b=(tag.get('href', None))
#print(b)
    #for j in range(0,p):

