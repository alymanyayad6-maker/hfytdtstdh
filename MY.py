from tkinter import *

root = Tk()
root.title("Simple Calculator")
root.geometry("300x400")
root.resizable(width=0, height=0)
root.configure(bg="black")

e = Entry(root, bd=10, width=30, font="Arial 21", bg="LightGrey")
e.pack()

def equal():
    CURRENT = e.get()
    # Only support addition, handle exceptions for robustness
    try:
        operands = CURRENT.split("+")
        if len(operands) == 2:
            result = int(operands[0]) + int(operands[1])
            clear()
            e.insert(0, result)
        else:
            clear()
            e.insert(0, "Error")
    except Exception:
        clear()
        e.insert(0, "Error")

def clear():
    e.delete(0, END)

def click(value):
    e.insert(END, value)

# Numeric buttons
btn1 = Button(root, text="1", font="Arial 19 bold", bg="Grey", bd=10, padx=10, pady=5, command=lambda: click(1))
btn1.place(x=10, y=60)
btn2 = Button(root, text="2", font="Arial 19 bold", bg="Grey", bd=10, padx=10, pady=5, command=lambda: click(2))
btn2.place(x=85, y=60)
btn3 = Button(root, text="3", font="Arial 19 bold", bg="Grey", bd=10, padx=10, pady=5, command=lambda: click(3))
btn3.place(x=160, y=60)
btn4 = Button(root, text="4", font="Arial 19 bold", bg="Grey", bd=10, padx=10, pady=5, command=lambda: click(4))
btn4.place(x=10, y=145)
btn5 = Button(root, text="5", font="Arial 19 bold", bg="Grey", bd=10, padx=10, pady=5, command=lambda: click(5))
btn5.place(x=85, y=145)
btn6 = Button(root, text="6", font="Arial 19 bold", bg="Grey", bd=10, padx=10, pady=5, command=lambda: click(6))
btn6.place(x=160, y=145)
btn7 = Button(root, text="7", font="Arial 19 bold", bg="Grey", bd=10, padx=10, pady=5, command=lambda: click(7))
btn7.place(x=10, y=230)
btn8 = Button(root, text="8", font="Arial 19 bold", bg="Grey", bd=10, padx=10, pady=5, command=lambda: click(8))
btn8.place(x=85, y=230)
btn9 = Button(root, text="9", font="Arial 19 bold", bg="Grey", bd=10, padx=10, pady=5, command=lambda: click(9))
btn9.place(x=160, y=230)
btn0 = Button(root, text="0", font="Arial 19 bold", bg="Grey", bd=10, padx=10, pady=5, command=lambda: click(0))
btn0.place(x=10, y=320)

# Operator and control buttons
btn_add = Button(root, text="+", font="Arial 19 bold", height=4, bg="skyBlue", bd=10, command=lambda: click("+"))
btn_add.place(x=235, y=60)
btn_clear = Button(root, text="C", font="Arial 19 bold", width=8, height=1, bg="crimson", bd=10, command=clear)
btn_clear.place(x=85, y=320)
btn_equal = Button(root, text="=", font="Arial 19 bold", height=4, bg="khaki", bd=10, command=equal)
btn_equal.place(x=235, y=230)

root.mainloop()
