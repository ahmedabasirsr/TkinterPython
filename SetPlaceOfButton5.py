from tkinter import *

pro = Tk()
pro.geometry("400x400")

btn1 = Button(pro,text ="Button1")
btn1.grid(row=0,column=0)         # set place of button and display it

btn2 = Button(pro,text ="Button2")
#btn2.grid(row=0,column=1)
btn2.place(x=200,y=200)           # set place where you like

btn3 = Button(pro,text ="Button3")
btn3.grid(row=1,column=0)

btn4 = Button(pro,text ="Button4")
btn4.grid(row=1,column=1)

pro.mainloop()
