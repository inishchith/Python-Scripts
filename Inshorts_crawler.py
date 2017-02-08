import requests
from bs4 import BeautifulSoup

import time
from pync import Notifier

def crawler():
    url ="https://www.inshorts.com/en/read"
    source_code= requests.get(url)
    plaintext= source_code.text
    obj_soup = BeautifulSoup(plaintext)

    for data in obj_soup.findAll('a',{'class':'clickable'} ):
        #finding key values
        find = data.get('href')
        link ="https://www.inshorts.com" + find
        find=str(find)[9:-14].replace('-'," ")
        Notifier.notify(find ,title='InShorts News', open= link)    # Click to Read Full Story
        time.sleep(10)

crawler()
