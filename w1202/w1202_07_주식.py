import requests
from bs4 import BeautifulSoup

url="https://finance.naver.com/sise/lastsearch2.naver"
headers ={"User-Again":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text,"lxml")
trs = soup.find("div",{"class":"box_type_l"}).table.find_all("tr")  # table안에있는 tr을 모두 갖고옴


# 순위 1,2,3번 출력
for td in trs[2].find_all("td"):   # for문
    print(td.text.strip(),end="\t")
print()  
for td in trs[3].find_all("td"):   # for문
    print(td.text.strip(),end="\t")
print()    
for td in trs[4].find_all("td"):   # for문
    print(td.text.strip(),end="\t")
    




# print(soup.prettify())
# 파일저장 -------------------------------------------
# with open("stock.html","w",encoding="utf8") as f:
#     f.write(soup.prettify())
# print("파일저장완료")

