from urllib.request import urlopen
from urllib.parse import urljoin
from bs4 import BeautifulSoup # $ pip install beautifulsoup4
url = input('Enter - ')
for _ in range(18):  # repeat 18 times
    soup = BeautifulSoup(urlopen(url))
    a = soup.find_all('a', href=True)  # all <a href> links
    if len(a) < 3:  # no 3rd link
        break  # exit the loop
    url = urljoin(url, a[2]['href'])