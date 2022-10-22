from tkinter import *

#####################################################
#function to print loop in window-interface##########
#####################################################
def loop():
    for i in range(1,11):
        #print(i)                                      #print in terminal
        lb =Label(pro, text=i,fg="red",bg="yellow") # object lb from Labela=>print i in window,and set colors of text and background text
        lb.pack(fill=X)                             # display text and fill background text



pro = Tk()               #creat window
pro.geometry("300x500")  #set size of window   
# creat button(btn) in window(pro)and name this button(loop: for..) and colors
btn = Button(pro,text="Loop: for range",fg="red",bg="yellow",command=loop)
btn.pack()

pro.mainloop()
