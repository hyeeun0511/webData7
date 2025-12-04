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
# browser.get() : 페이지 열기
browser.get(url)
# 2. 검색창에 시가총액 순위 입력
elem = browser.find_element(By.ID,"query")  
elem.click()  # 클릭 명령어
elem.send_keys("시가총액 순위")
# 3. enter키 입력
elem.send_keys(Keys.ENTER)  # Keys에 ENTER키를 쳐달라는 의미
time.sleep(1)  # 1초 대기
elem = browser.find_element(By.XPATH,'//*[@id="main_pack"]/section[2]/div/div[2]/div[2]/div[1]/div[1]/table/tbody/tr[1]/th/a')
elem.click()

# input을 받기위해 화면을 계속 열어놓음 / input없으면 프로그램 종료시 화면 닫힘
input("대기")

#-----------------------------------------------
# # selenium 4.3버전에서 찾기 find_element로 변경됨
# elem = browser.find_element(By.CLASS_NAME,"MyView-module__link_login___HpHMW")
# # time.sleep(2)  # 2초동안 대기
# # 클릭 명령어
# elem.click()   # 후 클릭  
# elem.send_keys("시가총액")
# # input후 enter입력
# elem.send_keys("Keys.ENTER")





