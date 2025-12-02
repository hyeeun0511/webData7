import requests
from bs4 import BeautifulSoup

url = "http://www.google.com"
res = requests.get(url)
res.raise_for_status()

# 파일저장방법 w:저장, r:읽기, a:추가
f = open("aaa.html","w",encoding='utf8')
f.write(res.text)
f.close()
soup = BeautifulSoup(res.text,"lxml")
# f = open("aaa.html","w",encoding='utf8')
# f.write(res.text)
# f.close()   # 필수

# with -> f.close() 필요없음
# soup.prettify() 문서가 정리되어 출력됨
with open("aaa2.html","w",encoding="utf8") as f:
    f.write(soup.prettify())  # html태그가 정리
    
# with open("aaa2.html","w",encoding="utf8") as f:
#     f.write(res.text)     # 그냥 출력

print("파일이 저장되었습니다.")
# print(res.text)   # html소스코드를 가져와서 출력할수 있음