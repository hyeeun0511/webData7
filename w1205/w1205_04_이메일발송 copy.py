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
import requests
from datetime import datetime  # 날짜 함수

### 임시비밀번호 생성함수
# def random_pw():
#     arr = [ i for i in range(10)]  # 10개의 번호를 받아서 배열에 넣음
#     # ranNum = "".join(map(str,arr2))  # 밑에와 같음
#     ranNum = "".join(map(str,random.sample(arr,8)))  # join은 문자인 경우만 가능  # str(문자로) 변경
#     print("임시비밀번호 : "+ranNum)
#     return ranNum

### 웹스크래핑
# url = "http://www.naver.com"
# headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36"}   # what is my user agent? -> 파란박스 코드 복붙
# res = requests.get(url,headers=headers)  # header(user-agent)를 바꿀것
# res.raise_for_status()
# soup = BeautifulSoup(res.text,"lxml")
# # print(soup.find("div",{"class":"DailyBoardView-module__weather_temperature___pOAGy"}))


# ####--날씨--####--------------------------------------------------------------------!!!!
# ### selenium
# ## naver 정보를 naver1.html로 받음
# url = "https://www.naver.com"   # 네이버 주소
# browser = webdriver.Chrome()    # 창열기 (웹브라우저 형태로 크롬창 열기)
# browser.maximize_window()       # 최대창 확대
# # 1. naver 페이지 열기
# browser.get(url)
# time.sleep(3)

# soup = BeautifulSoup(browser.page_source,"lxml")
# with open('naver1.html','w',encoding="utf8") as f:
#     f.write(soup.prettify())

# time.sleep(2)


# with open('naver1.html','r',encoding='utf8') as f:
#     soup = BeautifulSoup(f,"lxml")



# ## 날짜
# today = datetime.today()
# now = today.strftime('%Y-%m-%d %H:%M:%S')
# print(now)                                           ## ==>  2025-12-05 15:35:57


# # 온도/날씨
# weather = soup.find("div",{"class":"DailyBoardView-module__weather_temperature___pOAGy"}).text.strip().replace(" ","").split("\n")
# print(weather[0],weather[2])     ## ==>  1.8° 맑음     weather[0]:1.8°   weather[2]:맑음

# today_weather = f"기온:{weather[0]} / 날씨 : {weather[2]}"



# # # 최저기온
# low_temp = soup.find("span",{"class":"DailyBoardView-module__temperature_low___aC6Fe"}).text.strip().replace(" ","").split("\n")
# print(low_temp[0],low_temp[2])     ## ==>  최저기온 -6°

# today_low_temp = f"{low_temp[0]} : {low_temp[2]}"





# # # content = f'''
# # # 임시비밀번호 : {random_pw()}
# # # '''
# content = f'''
# {now}
# {today_weather}
# {today_low_temp}
# '''
# print(content)    
# ## ==> 2025-12-05 15:48:58
# ## ==> 기온:1.8° / 날씨 : 맑음
# ## ==> 최저기온 : -6°

# #------------------------------------------------ 1. 날씨





#------------------------------------------------ 2. 엔비디아 주식 가격

url = "https://finance.naver.com/item/main.naver?code=005930"   # 네이버 주소
browser = webdriver.Chrome()    # 창열기 (웹브라우저 형태로 크롬창 열기)
browser.maximize_window()       # 최대창 확대
# 1. naver 페이지 열기
browser.get(url)
time.sleep(3)

# print("완료")  ##

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36"}   # what is my user agent? -> 파란박스 코드 복붙

res = requests.get(url,headers=headers)  # header(user-agent)를 바꿀것
res.raise_for_status()
soup = BeautifulSoup(res.text,"lxml")
# print(soup.find(content)


# print(soup.find("div",{"class":"DailyBoardView-module__weather_temperature___pOAGy"}))




#------------------------------------------------ 3. 삼성전자 주식 가격






# smtpName = "smtp.naver.com"
# smtpPort = 587
# send_email = "bang48188@naver.com"  # 보내는이 - 네이버 보내는 주소 naver.com
# re_email = "bang48188@naver.com"  # 받는이
# pw = "DWE6BB5BEN3P"

# # 메일내용부분 (메일에 노출되는 내용들)
# msg = MIMEText(content)
# msg['From'] = "bang48188@naver.com"  # 보내는이 - 네이버 보내는 주소 naver.com
# msg['To'] = "banggrasia4818@gmail.com"    # 받는이 - bang48188@naver.com
# msg['Subject'] = "임시비밀번호를 보내드립니다."
# # 메일서버정보
# s = smtplib.SMTP("smtp.naver.com",587)
# # 메일서버접근
# s.starttls()
# # 메일서버 로그인
# s.login("bang48188@naver.com","DWE6BB5BEN3P")  # id,pw
# # 메일서버 발송
# # 보내는 이메일 주소, 받는 주소, 이메일 내용 부분
# s.sendmail("bang48188@naver.com","banggrasia4818@gmail.com",msg.as_string())  # 보내는이,받는이,문자화  #문자화해서 보내줌  # msg.as_string() : 메일 내용 (문자화)
# print(msg.as_string())
# # 메일 닫기
# s.close()

# # print("이메일 발송완료")



# # random_pw()  # 호출 -> 비밀번호 출력됨


# # print(random.sample(arr,8))  # 8개의 랜덤 번호를 뽑아옴
# # 문자로
