import urllib.parse
import urllib.request
import re
from bs4 import BeautifulSoup
# parsing through beautiful soup &&&& regular expessions


url ='https://pythonprogramming.net'
values = {'s':'basics' , 'submit':'search'}
data=urllib.parse.urlencode(values)
data=data.encode('utf-8')
req=urllib.request.Request(url,data)
resp=urllib.request.urlopen(req)
r=resp.read()
#soup = BeautifulSoup(r, 'html.parser')
#for c in soup.find_all('p',):
    #print(c)
    #print(c.text)
    #print("")

p=re.findall('<p>(.*?)</p>',str(r))
for line in p:
    line.rstrip()
    print(line)
