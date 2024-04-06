import tkinter

tk = tkinter.Tk()
def click():
    z = e1.get()
    print(z)
e1 = tkinter.Entry()
btn = tkinter.Button(text="red",command = click)

e1.grid(row=0,column=0)
btn.grid(row=1,column=0)
tk.geometry("400x500")
tk.mainloop()