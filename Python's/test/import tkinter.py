import datetime as dt
import os
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msg
from tkinter.filedialog import asksaveasfile
import subprocess
import threading
a = tk.Tk()
a.title("ana")
a.geometry('640x480')
a.config(bg='azure')
b = tk.Frame(width=30, height=30, bg='blue')
b.place(x=0, y=0)
c = tk.Frame(width=30, height=30, bg='red')
c.place(x=50, y=50)


def q(event=None):
    a.quit()


mm0 = tk.Menu(a, tearoff=0)
mm1 = tk.Menu(mm0, tearoff=0)
mm2 = tk.Menu(mm1, tearoff=0)
mm3 = tk.Menu(mm2, tearoff=0)
mm4 = tk.Menu(mm3, tearoff=0)
mm0.add_cascade(label="0", menu=mm1)
mm1.add_cascade(label="1", menu=mm2)
mm2.add_cascade(label="2", menu=mm3)
mm3.add_cascade(label="3", menu=mm4)
mm4.add_command(label="quit", accelerator="Ctrl+0", command=q)
a.config(menu=mm0)
a.bind('<Control-0>', q)
bt = tk.Button(a, text="a", command=lambda: print(cbx.get()))
bt.pack(side='top')
cbx = ttk.Combobox(values=("hi", "bye"))
cbx.pack()
nm = "nm"
tv = tk.Label(a, text=nm)
tv.pack()
lst = tk.Listbox(a)
lst.insert(0, 1, 2, 3, "a", "b", "c")
lst.pack()
rb00 = ttk.Radiobutton(a, value=0)
rb00.place(x=0, y=0)
rb01 = ttk.Radiobutton(a, value=1)
rb01.place(x=50, y=50)
global ldt


def show_date():
    ld['text'] = dt.datetime.now()


btd = tk.Button(a, relief='ridge', command=show_date)
btd.pack()
ld = tk.Label(a, text="")
ld.pack()


def upb():
    pbar["value"] = 100


def dob():
    pbar["value"] = 0


bpbar1 = tk.Button(a, text="Up", command=upb)
bpbar1.pack()
bpbar2 = tk.Button(a, text="Down", command=dob)
bpbar2.pack()
pbar = ttk.Progressbar(a, orient='horizontal', length=100, mode='determinate')
pbar.pack()
spb = tk.Spinbox(a, from_=10, to=50)
spb.pack()
phi = tk.PhotoImage(file="AccuWeather.jpg").subsample(5)


def showp():
    if os.path.exists("BigAccuWeather.png"):
        ap = tk.Toplevel(a)
        ap.title("photo")
        ap.geometry('512x512')
        pig = tk.PhotoImage(file="BigAccuWeather.png")
        tpi = tk.Label(ap, image=pig)
        tpi.photo = pig
        tpi.pack()
    else:
        msg.showerror(title="Error", message="File not found !")


pbhi = tk.Button(a, text="Show", image=phi, compound="top", command=showp)
pbhi.pack()


def showfee():
    if os.path.exists("feelings.exe"):
        thread = threading.Thread(target=lambda: subprocess.call(["feelings.exe"], shell=True))
        thread.start()
    else:
        msg.showerror(title="Error", message="not found !")

bfee = tk.Button(a, text="feel ?", command=showfee)
bfee.pack()
# code
a.mainloop()
