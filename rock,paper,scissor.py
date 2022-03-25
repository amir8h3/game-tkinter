#******************import********************
from tkinter import *
import tkinter.messagebox
import random

#******************Settings********************
win = Tk()
win.title("rock,paper,scissor")
win.geometry('300x350')
win.resizable(width=False,height=False)
color='#38d963'
win.configure(bg=color)

#******************Function********************

def creator():
    tkinter.messagebox.showinfo('creator','Game maker : amir8h3 ')

def clear():
        btn4['text']= ''
        btn5['text']= ''

def rock():
    z = random.randint(0,2)
    if z == 0:
        btn4['text']= 'rock'
        btn5['text']= 'Equal'
    elif z == 1:
        btn4['text']= 'paper'
        btn5['text']= 'You lose'
    elif z == 2:
        btn4['text']= 'scissor'
        btn5['text']= 'You won'

def paper():
    z = random.randint(0,2)
    if z == 0:
        btn4['text']= 'rock'
        btn5['text']= 'You won'
    elif z == 1:
        btn4['text']= 'paper'
        btn5['text']= 'Equal'
    elif z == 2:
        btn4['text']= 'scissor'
        btn5['text']= 'You lose'

def scissor():
    z = random.randint(0,2)
    if z == 0:
        btn4['text']= 'rock'
        btn5['text']= 'You lose'
    elif z == 1:
        btn4['text']= 'paper'
        btn5['text']= 'You won'
    elif z == 2:
        btn4['text']= 'scissor'
        btn5['text']= 'Equal'

#******************fremes********************

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

#******************Button********************

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
btn6 = Button(fremes8,text='clear', width=30,command=lambda: clear()  )
btn6.pack(side=RIGHT, padx=5, pady=5)
btn7 = Button(fremes8,text='creator', width=30,command= lambda: creator())
btn7.pack(side=LEFT, padx=5, pady=5)

#******************Label********************

label_1 = Label(fremes4, text='computer : ' , bg=color , font=100)
label_1.pack(side=LEFT, padx=5, pady=5)
label_2 = Label(fremes6, text='result : ' , bg=color , font=100)
label_2.pack(side=LEFT, padx=5, pady=5)

#******************RUN********************

win.mainloop()
