from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import random, string, json,discord

x = 0
string = "abcdefjhijklmnopqrstuvwrxyz0123456789"


def randurl():
    a = random.choice(string.lower())
    b = random.choice(string.lower())
    c = random.choice(string.lower())
    d = random.choice(string.lower())
    e = random.choice(string.lower())
    f = random.choice(string.lower())
    rand_url = str(a) + str(b) + str(c) + str(d) + str(e) + str(f)

    return rand_url


def getimage():
    x = False
    while x == False:
        rand_url = randurl()
        req = Request('https://prnt.sc/' + rand_url, headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req).read()
        soup = BeautifulSoup(webpage, 'html.parser')
        name_box = soup.find(id="screenshot-image")
        try:
            Request(name_box.get('src'), headers={'User-Agent': 'Mozilla/5.0'})
        except (AttributeError, ValueError):
            x = False
        else:
            x = True
            embed = discord.Embed(title = rand_url, url = "https://prnt.sc/" + rand_url, colour = 0xFF00CC)
            embed.set_image(url = name_box.get('src'))
            return embed