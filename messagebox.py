from tkinter import *          #importing every methods from tkinter module

from tkinter import messagebox #importing messagebox from tkinter 

master=Tk()                     #creating master

master.geometry("100x100")           #setting the geometry of the window

def info():                     #this function will show the show info message
    messagebox.showinfo("information","Information")

def error():                    #this function will show the show warning message
    messagebox.showwarning("warning","Warning")

def warn():                     #this function will show the show error message
    messagebox.showerror("error","Error")

def ask():                      #this function will show the show askinfo message
    messagebox.askquestion("confirm","Are you sure?")

#creating and placing the button widget

b1=Button(master,text="info",command=info)
b1.pack()
b2=Button(master,text="error",command=error)
b2.pack()
b3=Button(master,text="warn",command=warn)
b3.pack()
b4=Button(master,text="exit",command=ask)
b4.pack()

