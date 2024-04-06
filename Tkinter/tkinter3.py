import tkinter

tk=tkinter.Tk()

list=[]
def add():
    a=username.get()
    b=age.get()
    c=contact.get()
    list.append(a)
    list.append(b)
    list.append(c)
    
    l.config(text="Data succeddfully added")
    
def remove():
    l.config(text="Data successfully removed")
 
tk.config(bg="#14213D") 
l=tkinter.Label()
l.place(x=0,y=100)


username = tkinter.Entry()
age = tkinter.Entry()
contact = tkinter.Entry()

username.grid(rows=1,column=0)
age.grid(rows=2,column=0)
contact.grid(rows=3,column=0)

btn1 = tkinter.Button(text="Add",command=add)
btn2 = tkinter.Button(text="Add",command=remove)

btn1.place(x=0,y=60)
btn2.place(x=45,y=60)

tk.geometry("500x500")
tk.mainloop()