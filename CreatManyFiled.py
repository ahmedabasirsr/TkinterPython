from  tkinter import *


pro = Tk()

for i in range(6):
    for j in range(6):
        filed=Entry(pro,text=" ")
        filed.grid(row=i,column=j)


pro.mainloop()
