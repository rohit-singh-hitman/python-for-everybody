import urllib.request, urllib.parse, urllib.error
from urllib.request import urlopen
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import ssl
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl
import json

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro
sum=0
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url = input('Enter - ')
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read()
#print('Retrieved', len(data), 'characters')
#print(data.decode())
info = json.loads(data)
#print(len(info))
c=info['comments']
#print(len(c))
for i in c:

    d=(i['count'])
    e=int(d)
    sum=sum+d
print(sum)





#location = results[0].find('formatted_address').text