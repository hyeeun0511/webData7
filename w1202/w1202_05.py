import requests
from bs4 import BeautifulSoup

url = "http://www.naver.com"
headers ={"User-Again":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()  
soup = BeautifulSoup(res.text,"lxml")

### html태그,css문법으로 검색이 가능
# find() : 하나만 찾는것  findall() : 모두 찾는것
# 태그입력시 검색됨
# text : 태그안에 글자를 출력

# print(soup.find("title")) # soup에있는 find("title")를 찾을것                                                                 # title태그 가져오기
# print(soup.title.text)  # 태그를 입력해도 찾을수 있음                                                                           # title글자 가져오기
# print(soup.a)  # 가장 가까운 정보를 찾아옴                                                                                      # a태그 속성값 가져오기
# print(soup.a.attrs)  # 속성이 있는 모든값 찾아옴                                                                                # a태그 href속성값 가져오기
# print(soup.a['href'])  # 속성값만 찾아옴   # href만 들고와라                                                                    # 먼저 오는 div태그 가져오기 가져오기 
# print(soup.find("div"))  # 제일 첫번째 div에 들어있는 모든 정보 찾아옴
# print(soup.find_all("div")[0])  # div의 여러개(find_all)중 0([0])번째꺼 찾음   //  [1]:두번째, [2]:세번째, ...                    # div태그 여러개 가져오기
# print(len(soup.find_all("div")))  # div의 개수                                                                                # len() : 검색된 개수
# print(soup.find_all("div")[1].find("div"))                                                                                   # find_all() : div태그 여러개 가져오기
# print(soup.find_all("div")[1].find("div").attrs)
 
# idHeader = soup.find("div",{"id":"header"})
# print(soup.find("div",{"id":"header"}))   # header를 바로 찾아올수있음
# print(soup.find("h1",{"class":"search_logo"}))   # (naver2에서) h1찾기
# 옛날버전
# print(soup.find("legend",{"class":"blind"}))   # legend에 있는 class가 blind인 것 바로 찾아올수 있음
# 최신버전
print(soup.find("legend",class_="blind"))   # class가 예약어이기 때문에 -> class_=""
print(soup.find("div",id='header'))         # id는 예약어가 아니기 때문에 -> id=''


# 형제
# tag.next_sibling
# tag.previous_sibling




#---------------------------------------------------
#### 파일저장 ####
# # naver1.html 파일저장
# with open("naver1.html","w",encoding="utf8") as f:
#     f.write(res.text)
    
# # naver2.html 파일저장
# with open("naver2.html","w",encoding="utf8") as f:
#     f.write(soup.prettify()) 
    
# print("파일 저장완료")
