from tkinter import *
import tkinter.messagebox
import random


win = Tk()
win.title("rock,paper,scissor")
win.geometry('300x350')
win.resizable(width=False,height=False)
color='#38d963'
win.configure(bg=color)

def creator():
    tkinter.messagebox.showinfo('creator','Game maker : amir8h3 ')

def clear():
    return

def rock():
    return

def paper():
    return

def scissor():
    return





fremes1= Frame(win, width=400, height=50, bg=color )
fremes1.pack(side="top")
fremes2= Frame(win, width=400, height=50, bg=color )
fremes2.pack(side="top")
fremes3= Frame(win, width=400, height=50, bg=color )
fremes3.pack(side="top")
fremes4= Frame(win, width=400, height=50, bg=color )
fremes4.pack(side="top")
fremes5= Frame(win, width=400, height=50, bg=color )
fremes5.pack(side="top")
fremes6= Frame(win, width=400, height=50, bg=color )
fremes6.pack(side="top")
fremes7= Frame(win, width=400, height=50, bg=color )
fremes7.pack(side="top")
fremes8= Frame(win, width=400, height=50, bg=color )
fremes8.pack(side="top")


btn1 = Button(fremes1,text='rock', width=30, command=lambda: rock())
btn1.pack(side=LEFT, padx=5, pady=5)
btn2 = Button(fremes2,text='paper', width=30, command=lambda: paper())
btn2.pack(side=LEFT, padx=5, pady=5)
btn3 = Button(fremes3,text='scissor', width=30, command=lambda: scissor())
btn3.pack(side=LEFT, padx=5, pady=5)
btn4 = Button(fremes5,text='', width=30,  )
btn4.pack(side=LEFT, padx=5, pady=5)
btn5 = Button(fremes7,text='', width=30,  )
btn5.pack(side=LEFT, padx=5, pady=5)
btn6 = Button(fremes8,text='creator', width=30,command= lambda: creator())
btn6.pack(side=RIGHT, padx=5, pady=5)
btn7 = Button(fremes8,text='clear', width=30,command=lambda: clear()  )
btn7.pack(side=LEFT, padx=5, pady=5)
# btn8 = Button(fremes8,text='', width=30,  )
# btn8.pack(side=LEFT, padx=5, pady=5)













win.mainloop()




















