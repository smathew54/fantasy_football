#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 14:22:06 2021

@author: Shawn
"""

#import packages needed
import requests
from requests import get
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np


#take in only english characters
headers = {"Accept-Language": "en-US, en;q=0.5"}

url = "https://fantasy.espn.com/football/leaders?lineupSlot=0%2C2%2C23%2C4%2C6&scoringPeriodId=0&statSplit=lastSeason"

results = requests.get(url, headers = headers)

#places the HMTL into the beautiful soup
soup = BeautifulSoup(results.text, "html.parser")

print(soup.prettify())

espn_div = soup.find_all('div', class_= 'layout is-full')

#containers
player_name = []
passing_completion = []
passing_yards = []
passing_td = []
passing_int = []

rushing_carries = []
rushing_yards = []
rushing_td = []

receiving_rec = []
receiving_yds = []
receiving_td = []

misc_2pc = []
misc_fuml = []
misc_td = []

fpts = []
avg = []

for container in espn_div:
    print(container)

