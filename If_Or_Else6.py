from tkinter import *

def if_or_else():
    vr = ent.get()

    if vr =="Ahmed":
        lb = Label(pro,text =f"You are Admin {vr}",fg="green")
        lb.pack()
    else:
        lb = Label(pro,text = "You are not Admin ",fg ="red")
        lb.pack()


pro = Tk()
pro.geometry("400x400")

btn = Button(pro,text="If True or Else",command=if_or_else)
btn.place(x=150,y=150)

text_ent = StringVar()
ent = Entry(pro,textvariable="text_ent")
ent.place(x=150,y=50)


pro.mainloop()
