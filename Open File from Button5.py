from tkinter import *

def open_file(): # open file from Button 
    import sys
    import os
    os.system("C:\\Users\\Nastavnik\AppData\\Local\\Programs\\Python\\Python37-32\\Py7072022\\file.txt")


pro = Tk()
pro.geometry("400x400")

btn1 = Button(pro,text="Open File",command=open_file)
btn1.place(x=150,y=100)

pro.mainloop()
