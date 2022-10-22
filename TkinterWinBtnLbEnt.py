from tkinter import *
import random

def creat():
    #creat new Button ==> action from Button2
    x = random.randint(1,5)
    Button(text=f"Button{x}").pack()

def take_tex_ent():
    # take text from button ent1 and print
    val_ent = ent1.get()
    print (val_ent)



########################### Creat Window ##########################################
win = Tk()
#creat win object from Tk==> creat windows
win.geometry("600x500")
# set size windows
win.title("ExWin")
# set title for windows
win.iconbitmap("bird.ico")
# set icon for window
########################### Creat Lable #######################################
lb1 = Label(text="Welcome ")
lb1.pack()
# label in defualt place in window
lb2 = Label(text="Welcome ",fg="yellow",bg="gray",font=("Arial",15))
lb2.pack(fill=X)
# label in defualt place in window but with style
lb3 = Label(text="Welcome ",fg="blue",bg="gray",font=("Arial",15))
lb3.place(x=500,y=60)
# label in desire place in window with style
####################### Creat Button ##########################################

btn1 = Button(text="Print Entry Field", command=take_tex_ent)
btn1.pack()

var_tex_ent =StringVar()
# variable takes string(the text that is found in Button ent1) of StringVar
ent1 = Entry(textvariable="var_tex_ent")
ent1.pack()

# Button2 withe action to creat
btn2 = Button(text="Button2",fg="blue",bg="gray",font=("Arial",15),command=creat )
btn2.place(x=5,y=60)







win.mainloop()
# mainloop waite to works any action in your window