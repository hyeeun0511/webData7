import requests   # url정보를 가져오기위해

# 멜론
# url = "https://www.whatismybrowser.com/detect/what-is-my-user-agent/"
url = "http://www.melon.com/"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36"}   # what is my user agent? -> 파란박스 코드 복붙
res = requests.get(url,headers=headers)  # header(user-agent)를 바꿀것
res.raise_for_status()

print(res.text)

# 파일에 저장
with open("agent3.html","w",encoding="utf8") as f:
    f.write(res.text)
    
print("파일저장완료")