import pygame
from tkinter import *


pygame.init()

#""
def play_mu():
    pygame.mixer.music.load C:\\Users\Nastavnik\Desktop\\Enta.3omry.mp3()
    pygame.mixer.music.play(loops=0)

def stop_mu():
    pygame.mixer.music.stop()



pro =Tk()
pro.geometry("400x400")


lb =Label(pro,text="WindowPlayAndStop",fg ="white",bg ="black")
lb.pack(fill=X)

btn1 = Button(pro,text ="PlayMusic",fg ="green",bg="white",command=play_mu)
btn1.pack()

btn = Button(pro,text ="StopMusic",fg ="red",bg="white",command=play_mu)
btn2.pack()

pro.mainloop()
