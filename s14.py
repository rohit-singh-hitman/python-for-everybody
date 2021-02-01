import urllib.request, urllib.parse, urllib.error
from urllib.request import urlopen
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import ssl
sum=0
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url = 'https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M'
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
records=[]
a=[]

e=soup.find('table',class_="wikitable sortable")
c=1
for c in range(0,10):
    r=e.find_all('tr')
    a=r[c].text.split("\n")[1]
    b = r[c].text.split("\n")[3]
    d = r[c].text.split("\n")[5]
    print(a,b,d)
#print(len(a))
