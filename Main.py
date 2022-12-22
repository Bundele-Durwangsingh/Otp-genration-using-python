import os
from tkinter import *
from tkinter import messagebox
Window=Tk()
Window.geometry("1920x1080")
Window.title("OTP Verification")
def Phone():
    os.system("firstsms.py")

def Email():
    os.system("firstscreen.py")


label1=Label(Window,text="OTP Verification",relief="solid",font=("arial",26,"bold"),fg='blue').pack(fill=BOTH)
a=StringVar()
Re=Label(Window,text="Select the mode of verification",font=("arial",22,"bold")).place(x=0,y=50)

log = Button(Window, text="Email",relief="raised", bg='yellow', font=("arial", 26, "bold"), fg='black',command=Email).place(x=900,y=150)
log = Button(Window, text="Phone",relief="raised", bg='yellow', font=("arial", 26, "bold"), fg='black',command=Phone).place(x=900,y=300)
Window.mainloop()
