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
url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
for a in soup.find_all('tr',class_="comments"):
   # print(soup)
    print(a.text)
    b=a.text
    c=int(b)
    sum=sum+c
print(sum)

