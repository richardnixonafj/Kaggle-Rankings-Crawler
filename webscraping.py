#import requests
#import pandas as pd
from bs4 import BeautifulSoup as bs
from selenium import webdriver
#from selenium.webdriver.firefox.options import Options
#import json

url = "https://www.kaggle.com/rankings?group=competitions"


class Page:
    def __init__(self, driver):
        self.driver = driver

ff = webdriver.Firefox()
ff.get(url)
html = bs(ff.page_source, 'html.parser')

ranking = html.find_all('div', {'class': 'leaderboards__item-wrapper null'})

print(ranking)