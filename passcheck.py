from tkinter import *
from tkinter import ttk


def sub(event):
    entry1.config(show='*')

def sub1(event):
    entry1.config(show="")


root=Tk()
label1 = Label(root,text="passcheck")
label1.pack()
entry1=Entry(root,width=40)
entry1.pack()
entry1.insert(0,'Enter your password')
entry1.config(show='*')

sho = Button(root,text="")
sho.pack()

sho.bind('<ButtonPress-1>',sub1)
sho.bind('<ButtonRelease-1>',sub)

logo=PhotoImage(file='eye.png')
sho.config(image=logo,compound=LEFT)
small_logo=logo.subsample(5,5)
sho.config(image=small_logo)






