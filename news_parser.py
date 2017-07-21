import requests  
from bs4 import BeautifulSoup  
import re
import random


def random_links():
    hrefs = []
    URL = "http://store.steampowered.com/search/?category1=998&specials=1&page=1"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    
    for links in soup.findAll('a', attrs={'href': re.compile('http://store.steampowered.com/app')}):    
        hrefs.append(links.get('href'))

    hrefs = [x for x in hrefs if str(x) != 'http://store.steampowered.com/app/353370/?snr=1_7_7_204_12' and
          str(x) !='http://store.steampowered.com/app/353380/?snr=1_7_7_204_12' 
          and str(x) !='http://store.steampowered.com/app/358040/?snr=1_7_7_204_12']
    
        
    return hrefs[random.randint(1, 20)]

