from tkinter import *
                                                  # print_ent: print contient from filed 
def print_ent():                                  #
    enter_text =ent1.get()                        #enter_text take contient from object ent1 whene it call method get 
    print(enter_text)


pro = Tk()                                         #object from tkinter to make window=>command to only make window
pro.geometry("300x300")                            # creat size of pro(window)
enter_text =StringVar()                            #enter text is a object for string
btn = Button(pro,text="Print",command=print_ent)   #creat object to make button in pro and call def print_ent 
btn.pack()                                         #display btn button in the name Print
ent1 = Entry(pro,textvariable="enter_text")        #property of enter will be tekst(string)=>enter_text
ent1.pack()                                        #display ent1 field



pro.mainloop()                                      #to display window pro in screen
