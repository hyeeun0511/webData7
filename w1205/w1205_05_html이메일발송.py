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

## 임시비밀번호 생성함수
def random_pw():
    arr = [ i for i in range(10)]  # 10개의 번호를 받아서 배열에 넣음
    # ranNum = "".join(map(str,arr2))  # 밑에와 같음
    ranNum = "".join(map(str,random.sample(arr,8)))  # join은 문자인 경우만 가능  # str(문자로) 변경
    print("임시비밀번호 : "+ranNum)
    return ranNum


# html소스 



content = f'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>임시비밀번호 안내</title>
</head>
<body>
    <table style="width:760px; margin:0 auto;">
        <colgroup>
          <col width="182px">
          <col width="*">
          <col width="135px">
        </colgroup>
        <tr style="width:100%; height:105px;">
            <td style="height:45px;"><img src='https://mediahub.seoul.go.kr/images/newsletter/renew2025/logo_01.png'></td>
            <td></td>
            <td><img src='https://mediahub.seoul.go.kr/images/newsletter/renew2025/logo_02.png'></td>
        </tr>
        <tr style="height:200px; background: #eee;">
            <td colspan="3" style="text-align: center; font-size: 20px; font-weight: 600;">임시비밀번호 : {random_pw()}</td>
        </tr>
    </table>
</body>
</html>
'''


# url = "https://finance.naver.com/item/main.naver?code=005930"   # 네이버 주소
# browser = webdriver.Chrome()    # 창열기 (웹브라우저 형태로 크롬창 열기)
# browser.maximize_window()       # 최대창 확대
# # 1. naver 페이지 열기
# browser.get(url)
# time.sleep(3)

# # print("완료")  ##

# headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36"}   # what is my user agent? -> 파란박스 코드 복붙

# res = requests.get(url,headers=headers)  # header(user-agent)를 바꿀것
# res.raise_for_status()
# soup = BeautifulSoup(res.text,"lxml")
# # print(soup.find(content))


# # print(soup.find("div",{"class":"DailyBoardView-module__weather_temperature___pOAGy"}))


print(content)






# # 멀티메일내용부분 
msg = MIMEMultipart()
# # 내용부분
# html_part = MIMEText(content,"html","utf-8")
# msg.attach(html_part)
# msg['From'] = "bang48188@naver.com"  # 보내는이 - 네이버 보내는 주소 naver.com
# msg['To'] = "bang48188@naver.com"    # 받는이 - bang48188@naver.com
# msg['Subject'] = "멀티페이지 임시비밀번호를 보내드립니다."

# #   파일첨부
# file_part = MIMEBase('application','octet-stream')

# # 파일일읽어오기
# with open('yeogi.csv',"rb") as f:
#     file_part.set_payload(f.read())
# encoders.encode_base64(file_part)   # 파일을 쪼개서 전송할수 있는 형태로 변경
# file_part.add_header('Content-Disposition','attachment',filename='yeogi.csv')
# msg.attach(file_part)



with open('yeogi.csv','rb') as f:
    attachment = MIMEApplication(f.read())

attachment.add_header('Content-Disposition','attachment',filename='yeogi.csv')
msg.attach(attachment)



# 메일서버정보
s = smtplib.SMTP("smtp.naver.com",587)
# 메일서버접근
s.starttls()
# 메일서버 로그인
s.login("bang48188@naver.com","DWE6BB5BEN3P")  # id,pw
# 메일서버 발송
# 보내는 이메일 주소, 받는 주소, 이메일 내용 부분
s.sendmail("bang48188@naver.com","bang48188@naver.com",msg.as_string())  # 보내는이,받는이,문자화  #문자화해서 보내줌  # msg.as_string() : 메일 내용 (문자화)
print(msg.as_string())
# 메일 닫기
s.close()

print("이메일 발송완료")



# # random_pw()  # 호출 -> 비밀번호 출력됨


# # print(random.sample(arr,8))  # 8개의 랜덤 번호를 뽑아옴
# # 문자로
