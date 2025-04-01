from bs4 import BeautifulSoup

html = """
<html>
  <body>
    <h1>블로그 제목</h1>
    <p class="desc">이 블로그는 웹 크롤링 연습용입니다.</p>
    <p class="desc">파이썬을 이용해 데이터를 추출해보세요!</p>
    <a href="https://blog1.com">블로그1</a>
    <a href="https://blog2.com">블로그2</a>
  </body>
</html>
"""

soup = BeautifulSoup(html, "html.parser")



part = soup.find_all("p", class_="desc").text
print(part)


links = soup.find_all("a")
for link in links:
    print(link["href"])


