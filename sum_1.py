import tkinter as tk

root=tk.Tk()
root.title("1과 2의 합")

def sumsum():
    num1 = int(entry1.get())
    num2 = int(entry2.get())
    sum_1 = num1 + num2
    label.config(text="1과2의 합은"+ str(sum_1)+" 입니다",)




entry1=tk.Entry(root)
entry1.insert(0, "첫 번째 숫자")
entry1.pack()

entry2=tk.Entry(root)
entry2.insert(0, "두 번째 숫자")
entry2.pack()

label = tk.Label(root, text="결과값은?")
label.pack()

button = tk.Button(root, text="1과2의 합은?", command=sumsum)
button.pack()







root.mainloop()
