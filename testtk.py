from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import smtplib
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email import encoders


root = Tk()
root.geometry("750x750+0+0")
root.title("Send Your Mail")

def sub(event):
    pas.config(show='*')

def sub1(event):
    pas.config(show="")


def file():
    filenam=filedialog.askopenfile()
    global filename
    filename = filenam.name

def mail():
    global filename
    sender=str(send.get())
    receiver=str(recv.get())
    password=str(pas.get())
    subject=str(subj.get('1.0','end'))
    message=str(mseg.get('1.0','end'))
    mail=smtplib.SMTP('smtp.gmail.com',587)
    
    msg=MIMEMultipart()
    msg['From']=sender
    msg['To']=receiver
    msg['Subject']=subject
    msg.attach(MIMEText(message,'plain'))
    #filename=file()
    attachment = open(filename,'rb')
    part=MIMEBase('application','octet=stream')
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition','attachment; filename= '+filename)
    msg.attach(part)
    text=msg.as_string()
    mail.ehlo()
    mail.starttls()
    mail.login(sender,password)
    mail.sendmail(sender,receiver,text)
    mail.close()
    

def save():
    text="From: "+str(send.get())+"\nTo: "+str(recv.get())+"\nMessage:"+str(mseg.get('1.0','end'))
    file=open("mymails.txt",'a')
    file.write(text)
    file.close()

def clear():
    send.delete(0,END)
    pas.delete(0,END)
    recv.delete(0,END)
    subj.delete('1.0','end')
    mseg.delete('1.0','end')

label1 = Label(root,text="sender",width=40,font=("bold",10))
label1.place(x=0,y=100)
send = Entry(root,width=40)
send.place(x=200,y=100)

label2 = Label(root,text="password",width=40,font=("bold",10))
label2.place(x=0,y=150)
pas = Entry(root,width=40)
pas.place(x=200,y=150)
pas.config(show='*')
#pas.state(['disabled'])

label3 = Label(root,text="receiver",width=40,font=("bold",10))
label3.place(x=0,y=200)
recv = Entry(root,width=40)
recv.place(x=200,y=200)

label5 = Label(root,text="subject",width=40,font=("bold",10))
label5.place(x=0,y=250)
subj = Text(root,width=40,height=2)
subj.place(x=200,y=250)

label4 = Label(root,text="message",width=40,font=("bold",10))
label4.place(x=0,y=300)
mseg = Text(root,width=40,height=10)
mseg.place(x=200,y=300)
mseg.config(wrap="word")

sho = Button(root,text="SHOW")
sho.place(x=550,y=150)
sho.bind('<ButtonPress-1>',sub1)
sho.bind('<ButtonRelease-1>',sub)
logo=PhotoImage(file='eye.png')
sho.config(image=logo,compound=LEFT)
small_logo=logo.subsample(5,5)
sho.config(image=small_logo)

button=Button(root,text="Attachment",fg='red',command=file)
button.place(x=50,y=500)

sav=Button(root,text="Save",fg='red',command=save)
sav.place(x=250,y=700)

clean=Button(root,text="Clear fields",fg='red',command=clear)
clean.place(x=450,y=700)

mail=ttk.Button(root,text="MAIL",command=mail)
mail.place(x=50,y=700)

Exit=ttk.Button(root,text="EXIT",command=root.destroy)
Exit.place(x=650,y=700)




