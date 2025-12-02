import requests
from bs4 import BeautifulSoup

url="https://finance.naver.com/sise/lastsearch2.naver"
headers ={"User-Again":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text,"lxml")
trs = soup.find("div",{"class":"box_type_l"}).table.find_all("tr")  # table안에있는 tr을 모두 갖고옴
# print(soup.find("div",{"class":"box_type_l"}))   # soup에 있는 div를 찾을것. class가 box_type_l로.
# print(len(trs))      # 50개
# print(trs[2].find_all("td")[1].text)         # 0,1,2,... # 삼성전자
# print(trs[11].find_all("td")[1].text)  # 두산에너빌리티
# print(trs[11].find_all("td")[3].text)  # 75,000
# print(len(trs[11].find_all("td")))     # 12

for td in trs[11].find_all("td"):   # for문
    print(td.text.strip(),end="\t")   # strip() : 공백제거   # end="\t" : 옆쪽으로 정렬
    

# print(len(trs))    





# print(soup.prettify())
# 파일저장 -------------------------------------------
# with open("stock.html","w",encoding="utf8") as f:
#     f.write(soup.prettify())
# print("파일저장완료")

