import requests
# to request for information from a webpage
#beautiful soup helps to sort data( html , xml links/files ) eg to get all "titles , h1s from page source
from bs4 import BeautifulSoup

def crawler():
    url ="https://www.inshorts.com/en/read"
    source_code= requests.get(url)
    plaintext= source_code.text
    obj_soup = BeautifulSoup(plaintext)
    # obj_soup is a object of beautifulSoup class through which we can get all titles , h1s etc from the plain_text
    for data in obj_soup.findAll('a',{'class':'clickable'} ):
        #finding key values
        href ="https://www.inshorts.com" + data.get('href')
        print(href)
        print()
crawler()
