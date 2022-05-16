from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import random, string, json,discord

def get_gfy(url):
    req = Request(url,  headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    soup = BeautifulSoup(webpage, 'html.parser')
    name_box = soup.find('img')
    return (name_box.get('src'))
