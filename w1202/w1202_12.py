import requests
from bs4 import BeautifulSoup
import os
headers = {"User-Again":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36"}

# 파일 불러오기
with open("daum_movie.html","r",encoding="utf8") as f:
    soup = BeautifulSoup(f,"lxml")


#  selenium으로 파일 저장--------------------------------------
# import requests
# from bs4 import BeautifulSoup
# from selenium import webdriver
# import time

# # requests라이브러리, selenium라이브러리 차이점.
# # 크롬드라이버를 활용해서 크롬브라우저를 제어할수 있음.
# browser = webdriver.Chrome()

# # 크롬브라우저 창이 열림.
# browser.get("https://search.daum.net/search?w=tot&m=&q=%EC%98%81%ED%99%94%20%EC%98%88%EB%A7%A4%EC%88%9C%EC%9C%84&nzq=%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=NSJ")
# time.sleep(7) # 7초 대기후 실행   # 창이 열린 후 7초후 닫힘
# soup = BeautifulSoup(browser.page_source,"lxml")
# # 파일저장
# with open("daum_movie.html","w",encoding="utf8") as f:
#     f.write(soup.prettify())
    





#---------------------------------------



# print(soup.prettify())



#-----------------------------------------------------------
# url ="https://search.daum.net/search?w=tot&m=&q=%EC%98%81%ED%99%94%20%EC%98%88%EB%A7%A4%EC%88%9C%EC%9C%84&nzq=%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=NSJ"
# res = requests.get(url,headers=headers)
# print(res.text) 확인
# soup = BeautifulSoup(res.text,"lxml")
##----  1등~10등  제목,예매율,날짜 ----##
## 파일 저장
# with open ("daum_movie.html","w",encoding="utf8") as f:
#     f.write(soup.prettify())
    
# print("저장완료")





##-----------[실시간 예매율]---------------------##
# # print(soup.find("div",{"class":"c-carousel"}))
# section = soup.find("div",{"id":"morColl"}).find("div",{"class":"c-section-subtab"})
# atxts = section.find_all("a")
# print(atxts[0].contents)  #['실시간 예매율']
# atxts = section.find_all("a")
# for a in atxts:
#     print(a.contents[0])  # text -> contents

# print(soup.find("ul",{"class":"grid_xscroll"}))
## 실시간 예매율, 일일 관객수
