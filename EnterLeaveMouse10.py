from tkinter import *

def enterr(e):
    btn["background"] ="red"

def leavv(e):
    btn["background"] ="gray"

pro =Tk()
pro.geometry("400x400")

btn = Button(pro,text="EneterLeav",bg="gray",fg="white")
btn.pack()

btn1 = Button(pro,text="Bottun")
btn1.pack()

btn.bind("<Enter>",enterr)
btn.bind("<Leave>",leavv)

pro.mainloop()
