from tkinter import *

def add_2number():
    n1 = int(ent1.get())#get() alawayes return string 
    n2 = int(ent2.get()) #for this reason i write int
    s = n1 + n2
    lb = Label(pro,text = s, fg="red")
    lb.pack()

pro = Tk()
pro.geometry("400x400")
num1 = IntVar()
num2 = IntVar()

btn =Button(pro,text="Add", command =add_2number)
btn.pack()
ent1 = Entry(pro,textvariable="num1")
ent1.pack()
ent2 = Entry(pro,textvariable="num2")
ent2.pack()

pro.mainloop()
