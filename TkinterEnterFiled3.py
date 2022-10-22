from tkinter import *
###############################################################
def btn_add():
    
    lb1 = Label(pro,text =ent1.get(),fg="red")
    lb1.pack()
    lb2 = Label(pro, text =ent2.get(), fg="green")
    lb2.pack()
    
    
    
#################################################################


pro = Tk()
pro.geometry("400x400")



text_of_ent1 = StringVar()
text_of_ent2 = StringVar()

ent1 = Entry(pro,textvariable="text_of_ent1")
ent1.pack()

ent2 = Entry(pro,textvariable="text_of_ent2")
ent2.pack()

btn = Button(pro,text="Add",command=btn_add)
btn.pack()




pro.mainloop()
