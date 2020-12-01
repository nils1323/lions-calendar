#! /bin/python3
import urllib
import requests
from datetime import date
from bs4 import BeautifulSoup
import os
import telegram_send
import sys

confPath = "./user.conf"
firstSetup = not os.path.exists(confPath)
ownNumber=1427

def splitList(lst):
    for i in range(0, len(lst), 3):
        yield lst[i:i + 3]

if(firstSetup):
    telegram_send.configure(confPath, channel=False, group=False, fm_integration=False)

today = date.today()
currentDay = str(today.strftime("%d")).lstrip("0")

resp = requests.get("https://kalender.lions-club-hagen-mark.de/showwinners?q=" + currentDay)
#print(resp.text)
soup = BeautifulSoup(resp.text, 'html.parser')
#print(soup)
soup = soup.findAll('table')[1]
soup = soup.findAll('td')
winners = []
for td in soup:
    winners.append(td.text)
winnerlist = list(splitList(winners))
#print(winnerlist)
won=False
ownList=[]
#print(winnerlist)
for winner in winnerlist:
    if int(winner[0])==int(ownNumber):
        won = True
        ownList = winner
        winnermessage = "you won " + winner[1] + " from " + winner[2]
        print(winnermessage)
        telegram_send.send(conf=confPath, messages=[winnermessage])
        break
        #pass
if not won:
    print("you didn't win")
