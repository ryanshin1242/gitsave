from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import tkinter as tk
from tkinter import ttk


## 블로거 크롤링 함수수
def search_word():
    print("검색시작")
    progress.start()  # 바 움직이기 시작
    root.after(100, simulate_search)  # 약간의 지연 후 작업 실행
    



#tkinter를 사용하여 GUI 구성
#1. GUI 구성 기본틀 만들기

root=tk.Tk()
root.title("네이버서로이웃자동추가")

entry1=tk.Entry(root)
entry1.insert(0, "ID 입력")
entry1.grid(row=0, column=0,padx=5, pady=5)

entry2=tk.Entry(root)
entry2.insert(0, "패스워드입력")
entry2.grid(row=1, column=0,padx=5, pady=5)

entry3=tk.Entry(root)
entry3.insert(0, "검색어")
entry3.grid(row=3, column=0,padx=5, pady=5)

progress = ttk.Progressbar(root, length=200, mode='indeterminate')
progress.grid(row=5, column=0, padx=5, pady=5)

def clear_entry1(event):
    if entry1.get() == "ID 입력":
        entry1.delete(0, tk.END)

entry1.bind("<FocusIn>", clear_entry1)  # 포커스 들어오면 실행

def clear_entry2(event):
    if entry2.get() == "패스워드입력":
        entry2.delete(0, tk.END)

entry2.bind("<FocusIn>", clear_entry2)  # 포커스 들어오면 실행

def clear_entry3(event):
    if entry3.get() == "검색어":
        entry3.delete(0, tk.END)

entry3.bind("<FocusIn>", clear_entry3)  # 포커스 들어오면 실행



button = tk.Button(root, text="서칭 시작", command=search_word)
button.grid(row=4, column=0,padx=5, pady=5)



root.mainloop()







### 일단 실행 중지##
# 드라이버 자동 설치 및 실행
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://www.naver.com")
time.sleep(5)
driver.quit()


