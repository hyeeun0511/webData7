import time
import os
import random
# 웹스크래핑
import requests
from bs4 import BeautifulSoup
# selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
# 이메일 발송 라이브러리
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.base import MIMEBase
from email import encoders
# 날짜 함수
from datetime import datetime
# 마우스 제어  (pip install pyautogui 설치 후)
import pyautogui

#### selenium 방법
url = "http://www.naver.com"
browser = webdriver.Chrome() # 창열기
browser.maximize_window()  # 최대창 확대
browser.get(url)

# 마우스 제어 부분
pyautogui.sleep(1)   # 1초간 대기
pyautogui.scroll(-700)  # -700만큼 스크롤 내리라는 의미
pyautogui.scroll(700)  # -700만큼 스크롤 내리라는 의미
pyautogui.sleep(1)
pyautogui.moveTo(870,300)  
pyautogui.click()         # 한벅클릭
# pyautogui.doubleClick()   # 더블클릭


input("대기")