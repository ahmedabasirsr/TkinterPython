from tkinter import *
import pyttsx3          # for read text to the voice


def speak():
    vr = pyttsx3.init()
    vr.setProperty("rate",150) #speed voice
    vr.say(filed.get())        # read from filed
    vr.runAndWait()
    filed.delete(0,END)         # delet text from filed


pro = Tk()
pro.geometry("300x300")

filed = Entry(pro)
filed.pack()

bnt = Button(pro, text="Speack",command = speak)
bnt.pack()

pro.mainloop()
