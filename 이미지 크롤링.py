from bs4 import BeautifulSoup
from urllib.request import urlopen

response = urlopen('https://finance.naver.com/news/market_notice.naver?&page=1')
soup = BeautifulSoup(response, 'html.parser')
for anchor in soup.select('td.on'):
    print(soup.get_text())