# Scoreboard crawler for espncricinfo
import schedule
import time
import requests
from bs4 import BeautifulSoup
from pync import Notifier
import os

def job():
    url = "http://www.espncricinfo.com/west-indies-v-india-2016/engine/match/1022597.html"  #link here , default invalid for now
    raw = requests.get(url)
    plain_text = raw.text
    obji = BeautifulSoup(plain_text)
    for data in obji.findAll('span', {'class': "innings-1-score innings-current"}): #search tags
        href = data.string
        Notifier.notify(href, title="Match Score")

schedule.every(10).seconds.do(job)
#schedule.every().hour.do(job)
#schedule.every().day.at("10:30").do(job)

while 1:
    schedule.run_pending()
    time.sleep(1)
