from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup
import time  
import os

browser = webdriver.Chrome()
url = "http://www.naver.com"
# 1. 네이버 페이지 열기
browser.get(url)

# 2. 뉴스 선택 클릭
elem = browser.find_element(By.CLASS_NAME,"type_news")  # service_icon / type_news  :둘중 하나,둘다 가능
elem.click()

# 상단 탭 리스트 가져오기
tabs = browser.window_handles
# 3. IT/과학 클릭
# 2번째 탭 선택 - tabs[0] : 원본(부모탭-첫번째탭naver), tab[1] : 새창(자식탭-두번째탭IT/과학)
browser.switch_to.window(tabs[1])
browser.find_element(By.XPATH,"/html/body/section/header/div[2]/div/div/div/div/div/ul/li[6]/a/span").click()
# elem = browser.find_element(By.XPATH,"/html/body/section/header/div[2]/div/div/div/div/div/ul/li[6]/a/span")
# elem.click()

# 4. 첫번째 뉴스 클릭
time.sleep(2)  # 2초 대기
browser.find_element(By.CLASS_NAME,"sa_text_strong").click()

# elem = browser.find_element(By.CLASS_NAME,"sa_text_strong")
# elem.click()

# input을 받기위해 화면을 계속 열어놓음 / input없으면 프로그램 종료시 화면 닫힘
input("대기")   