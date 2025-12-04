from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup
import time  
import os
import random

url = "https://nid.naver.com/nidlogin.login?mode=form&url=https://www.naver.com/"
browser = webdriver.Chrome()
# 1. naver 페이지 열기
browser.get(url)

# input데이터 넣기
input_js = '''
document.getElementById("id").value = "{id}";
document.getElementById("pw").value = "{pw}";
'''.format(id='bang48188',pw='grasia48188')

time.sleep(3)  # 3초 대기
# time.sleep(random.uniform(1,5))  # 1~5초 사이에 랜덤으로 돌려서 대기
# naver에서 elem라는 요소로 찾기해서 데이터 입력시 차단
# 자바스크립트를 사용해서 데이터 입력
browser.execute_script(input_js)  # 스크립트 실행  # input됨
time.sleep(3)
browser.find_element(By.ID,"log.login").click()

# 메일 클릭
browser.find_element()



# 에러나면 멈췄다가 천천히 다시 (안그러면 차단당함)

input("대기")  # 창 닫히지 않게 하기위해 