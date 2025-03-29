import tkinter as tk


def say_hello():
    label.config(text="안녕할까요?")

def greet():
    name = entry.get()
    label.config(text="당신의 이름은?")  
    label.config(text="안녕하세요"+ name+"님!")  # 라벨에 인사 


root = tk.Tk()
root.title("나의 첫 프로그램")

entry=tk.Entry(root)
entry.pack()

label = tk.Label(root, text="hello, tkinter")
label.pack()

button = tk.Button(root, text="게임시작", command=say_hello)
button.pack()

button = tk.Button(root, text="안녕할까?", command=greet)
button.pack()

root.mainloop()






