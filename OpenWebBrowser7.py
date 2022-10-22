import webbrowser
from tkinter import *

def search_web():
    vr = ent_filed.get()
    webbrowser.open(vr)

pro = Tk()
pro.geometry("400x400")

lb = Label(pro,text = "Web Browser",fg ="white",bg ="black")
lb.pack(fill=X)

ent_filed = Entry(pro)
ent_filed.pack()

btn =Button(pro,text ="Search",command = search_web)
btn.pack()
pro.mainloop()

