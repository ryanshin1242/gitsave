import tkinter as tk

def calc(op):
    num1 = int(entry1.get())
    num2 = int(entry2.get())

    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2  
    elif op == "/":
        if num2 != 0:
            result = round(num1 / num2,2)
        else:
            result = "0으로 나눌수 없습니다."
    else:
        result = "잘못된 연산자입니다다"
    
    label.config(text="결과값은"+ str(result)+" 입니다",)




root=tk.Tk()
root.title("사칙연산 계산기")

entry1=tk.Entry(root)
entry1.insert(0, "첫 번째 숫자")
entry1.grid(row=0, column=0,columnspan=10)

entry2=tk.Entry(root)
entry2.insert(0, "두 번째 숫자")
entry2.grid(row=1, column=0,columnspan=10)
font_setting = ("Arial", 12, "bold")
button_add = tk.Button(root, text="+", width=7,command= lambda : calc("+"))
button_add.grid(row=2, column=0,padx=5, pady=5)
button_min = tk.Button(root, text="-", width=7,command= lambda : calc("-"))
button_min.grid(row=2, column=1,padx=5, pady=5)
button_mul = tk.Button(root, text="*", width=7, command= lambda : calc("*"))
button_mul.grid(row=2, column=2,padx=5, pady=5)
button_div = tk.Button(root, text="/", width=7, command= lambda : calc("/"))
button_div.grid(row=2, column=3,padx=5, pady=5)


## entry_op=tk.Entry(root)
## entry_op.insert(5, "사칙연산 부호를 넣으시오")
## entry_op.pack()


label = tk.Label(root, text="결과값은?")
label.grid(row=3, column=0,columnspan=10)


def clear_entry1(event):
    if entry1.get() == "첫 번째 숫자":
        entry1.delete(0, tk.END)

entry1.bind("<FocusIn>", clear_entry1)  # 포커스 들어오면 실행

def clear_entry2(event):
    if entry2.get() == "두 번째 숫자":
        entry2.delete(0, tk.END)

entry2.bind("<FocusIn>", clear_entry2)  # 포커스 들어오면 실행

root.mainloop()
