from bs4 import BeautifulSoup
import requests
import ctypes
import time

while True:
    try:
        source = requests.get("https://www.cricbuzz.com/live-cricket-scores/22778/nz-vs-ind-1st-odi-india-tour-of-new-zealand-2020").text
        soup = BeautifulSoup(source, 'lxml')
        score = soup.find('div', class_= 'cb-min-bat-rw')
        ctypes.windll.user32.MessageBoxW(0, score.text, "SCORE:", 64)
        time.sleep(300)
    except:
        ctypes.windll.user32.MessageBoxW(0, "Update the link of today's match", "!!!!!", 64)
        break