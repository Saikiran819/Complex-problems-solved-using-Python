from bs4 import BeautifulSoup
import requests
import ctypes
import time
import re

source = requests.get("https://www.youtube.com/").text
soup = BeautifulSoup(source, 'lxml')
vid = soup.find_all("a")
for v in vid:
    pat = r"watch?"
    if re.search(pat, str(v)):
        print("https://www.youtube.com"+v.get("href"))
        print(v.text+"\n")