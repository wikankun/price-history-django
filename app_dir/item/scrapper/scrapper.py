import re
import requests
from bs4 import BeautifulSoup

class ScrapperTokopedia:
    url = None
    price = None

    def __init__(self, url):
        self.url = url
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
        }
        s = requests.Session()
        page = s.get(self.url, headers = headers)
        self.soup = BeautifulSoup(page.content, "html.parser")        

    def getProductName(self):
        try:
            self.price = self.soup.find(attrs={"css-v7vvdw"}).get_text()
            return self.price
        except:
            "Gagal"

    def getPrice(self):
        try:
            price = self.soup.find(attrs={"css-158gcqc"}).get_text()
            price = ''.join(re.findall(r'\d+', price))
            self.price = int(price)
            return self.price
        except:
            "Gagal"
