from tkinter import *
import os
import sys

pro =Tk()
pro.geometry("800x450+280+50") # size window +move x osa=>280  and y osa =>50
pro.resizable(False,False)      # do not change size window and it not move
pro.title("SUPER MARKET:")      
pro.iconbitmap("C:\\Users\\Nastavnik\\Desktop\\Projects\\SuperMarkit.ico ")
lb =Label(pro,text="Super Market",fg="yellow",bg="gray",font=("Arial",15))
lb.pack(fill=X)

#creat the frame in window(pro)
fram_left = Frame(pro, width=230 , height=420,bg ="pink")
fram_left.place(x=570,y=37)

#creat 3 label in frame_left
lb1 = Label(fram_left,text =" Project of the Super Market",bg="gray", fg="black",font=("Arial",10) )
lb1.place(x=42,y=10)
lb2= Label(fram_left,text ="Developer: Ahmed Abas ", bg="gray", fg="black", font=("Arial",10))
lb2.place(x=42,y=50)
lb3= Label(fram_left, text =" Contact",bg="gray", fg="black", font=("Arial",10))
lb3.place(x=42,y=90)

btn1 =Button(fram_left, text=" FaceBook Adress",bg="gray", fg="black", font=("Arial",10))
btn1.place(x=42, y=130)
btn2 =Button(fram_left, text="Email Adress ",bg="gray", fg="black", font=("Arial",10))
btn2.place(x=42, y=170)
btn3 =Button(fram_left, text="chanal Youtub ",bg="gray", fg="black", font=("Arial",10))
btn3.place(x=42, y=210)
btn4 =Button(fram_left, text="Location Adress ",bg="gray", fg="black", font=("Arial",10))
btn4.place(x=42, y=250)
btn5 =Button(fram_left, text="Who is mi ",bg="gray", fg="black", font=("Arial",10))
btn5.place(x=42, y=290)
btn6 =Button(fram_left, text="Close program ",bg="gray", fg="black", font=("Arial",10))
btn6.place(x=42, y=330)



















pro.mainloop()
