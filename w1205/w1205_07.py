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

# 상단 Chrome이 자동화된 테스트 소프트웨어에 의해 제어되고 있습니다 제거
options = Options()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
options.add_argument("--disable-blink-features=AutomationControlled")


# [1. 다음 창 열기] ------------
#### selenium 방법
url = "https://www.daum.net/"
# headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36"}   # what is my user agent? -> 파란박스 코드 복붙
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
res = requests.get(url, headers=headers)
browser = webdriver.Chrome(options=options) # 창열기
soup = BeautifulSoup(browser.page_source,"lxml")
browser.maximize_window()  # 최대창 확대
browser.get(url)
time.sleep(1)


# [2. 검색창 -> 서울특별시 용산구 이태원동 아파트 ]---------
#### input 데이터 넣기
elem=browser.find_element(By.XPATH,'//*[@id="q"]')
time.sleep(1)
elem.click()
elem.send_keys("서울특별시 용산구 이태원동 아파트")
# time.sleep(1)

# 마우스 제어 -> 검색 클릭
pyautogui.moveTo(1190,190)
pyautogui.click()
time.sleep(1)


url = "https://search.daum.net/search?nil_suggest=btn&w=tot&DA=SBC&q=%EC%84%9C%EC%9A%B8%ED%8A%B9%EB%B3%84%EC%8B%9C+%EC%9A%A9%EC%82%B0%EA%B5%AC+%EC%9D%B4%ED%83%9C%EC%9B%90%EB%8F%99+%EC%95%84%ED%8C%8C%ED%8A%B8"
## 정보
list = soup.find("div",{"id":"estateCollTabContents"})  # 리스트
# A남산대림
# a=lists[0].find('a',{'class':'fn_tit'})
# A = soup.find("li",{"class":"fst"})
print(list)



# J = soup.find_all("div",{"id":"estateCollTabContents"})  # 리스트
# first = J.find("li",{"class":"fst"})

# A = J.find("div",{"class":"wrap_tit"})/





input("대기")