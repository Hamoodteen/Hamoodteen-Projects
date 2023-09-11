from tkinter import Tk, Label, Button, ttk

class abc:
    def __init__(self , Windows10):
        self.Windows10= Windows10
        Windows10.title("Welcome to Windows 10")
        Windows10.geometry("640x480")
        self.b = Button(Windows10, text="open new window" , command=Windows10.destroy).pack()


win = Tk()
a = abc(win)
win.mainloop()

def www():
    l = Label(qqq , text="hello").pack()

Windows = Tk()
qqq = Tk()
Windows.geometry("640x480")
qqq.geometry("640x480")
Windows.title("1")
qqq.title("2")
t = Button(Windows , text="hi" , command = www).pack()

Windows.mainloop()
        