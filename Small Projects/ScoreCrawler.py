# Scoreboard crawler for espncricinfo
import schedule
import time
import requests
from bs4 import BeautifulSoup

def job():
    url = "http://www.espncricinfo.com/west-indies-v-india-2016/engine/match/1022597.html"
    raw = requests.get(url)
    plain_text = raw.text
    obji = BeautifulSoup(plain_text)
    for data in obji.findAll('span', {'class': "innings-1-score innings-current"}):
        href = data.string
        print(href)
        print()

schedule.every(10).seconds.do(job)
#schedule.every().hour.do(job)
#schedule.every().day.at("10:30").do(job)

while 1:
    schedule.run_pending()
    time.sleep(1)
