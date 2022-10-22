from tkinter import *
import pyttsx3

pro =Tk()
pro.geometry("400x400")

vr = pyttsx3.init()
vr.say("Welcom in ours program")
vr.runAndWait()
