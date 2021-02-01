import xml.etree.ElementTree as ET
import urllib.request, urllib.parse, urllib.error
import ssl
sum=0
url = input('Enter - ')
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read()
tree = ET.fromstring(data)
lst = tree.findall('div')
#print(lst)
for line in lst:
    print('Name:',line.find('name').text)
    c=line.find('count').text
    print(c)
    d=int(c)
    sum=sum+d
print(sum)