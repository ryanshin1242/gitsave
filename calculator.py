import tkinter as tk

def allsum():
    num1 = int(entry1.get())
    num2 = int(entry2.get())
    opop = entry_op.get()

    if opop == "+":
        result = num1 + num2
    elif opop == "-":
        result = num1 - num2
    elif opop == "*":
        result = num1 * num2  
    elif opop == "/":
        if num2 != 0:
            result = round(num1 / num2,2)
        else:
            result = "0으로 나눌수 없습니다."
    else:
        result = "잘못된 연산자입니다다"
    
    label.config(text="결과값은"+ str(result)+" 입니다",)


root=tk.Tk()
root.title("사칙연산 계산기기")

entry1=tk.Entry(root)
entry1.insert(1, "첫 번째 숫자")
entry1.pack()

entry2=tk.Entry(root)
entry2.insert(2, "두 번째 숫자")
entry2.pack()

entry_op=tk.Entry(root)
entry_op.insert(5, "사칙연산 부호를 넣으시오")
entry_op.pack()

label = tk.Label(root, text="결과값은?")
label.pack()

button = tk.Button(root, text="1과2의 합은?", command=allsum)
button.pack()

root.mainloop()
