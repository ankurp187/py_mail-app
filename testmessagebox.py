from tkinter import *
from tkinter import ttk
from tkinter import messagebox

root=Tk()

def check():
    messagebox.showinfo(title='A Friendly Message',message='Hello Tkinter!')
def check1():
    messagebox.askquestion(title="Selection",message="which one to select?")
def onclick(event):
    global spam
    global b
    spam.get()
    b.get()
def check2():
    global spam
    root1=Tk()
    checkbutton=ttk.Checkbutton(root1,text='SPAM!')
    checkbutton.pack()
    spam=StringVar()
    checkbutton.config(variable=spam,onvalue='SPAM Please!',offvalue='BOO Spam!')
    button=Button(root1,text="check",command=onclick).pack()
    global b
    b=StringVar()
    ttk.Radiobutton(root1,text="A",value="A", variable=b).pack()
    ttk.Radiobutton(root1,text="B",value="B", variable=b).pack()
    ttk.Radiobutton(root1,text="C",value="A", variable=b).pack()
    checkbutton.config(textvariable=b)

button=ttk.Button(root,text="Check",command=check2)
button.pack()
