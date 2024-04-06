import tkinter

tk = tkinter.Tk()
def plus():
    p = int(num1.get())
    q = int(num2.get())
    r=p+q
    
    l.config(text=str(r))

def minus():
    p = int(num1.get())
    q = int(num2.get())
    r=p-q
    
    l.config(text=str(r))

def multiply():
    p = int(num1.get())
    q = int(num2.get())
    r=p*q
    
    l.config(text=str(r))
    
def divide():
    p = int(num1.get())
    q = int(num2.get())
    r=p/q
    
    l.config(text=str(r))
    
num1 = tkinter.Entry()
num2 = tkinter.Entry()

l=tkinter.Label()
l.grid(row=8,column=0)

btn1 = tkinter.Button(text="+",command = plus)
btn2 = tkinter.Button(text="-",command = minus)
btn3 = tkinter.Button(text="*",command = multiply)
btn4 = tkinter.Button(text="/",command = divide)

num1.grid(row=1,column=0)
num2.grid(row=3,column=0)
tk.config(bg="magenta")

btn1.place(x=4, y=1)
btn2.grid(row=5,column=0)
btn3.grid(row=6,column=0)
btn4.grid(row=7,column=0)

tk.geometry("500x500")
tk.mainloop()