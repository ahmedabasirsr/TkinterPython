from tkinter import *

pro = Tk()
pro.geometry("400x400")

btn1 = Button(pro,text="Button1")
btn1.pack()

btn2 = Button(pro,text="Button2",activebackground ="black",activeforeground="white")
btn2.pack()

btn3 = Button(pro,
              text="Button3",
              activebackground ="blue",
              activeforeground ="red")
btn3.pack()



pro.mainloop()
