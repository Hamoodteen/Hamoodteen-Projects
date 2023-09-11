import tkinter as tk
from tkinter import ttk
calc = tk.Tk()
calc.title("آلة حاسبة بسيطة")
calc.resizable(False, False)
calc.geometry("460x180")
lab = tk.Label(calc, text="أدخل الأرقام و اختر العملية", foreground="blue", font=("Segoe UI", 20))
lab.pack()
ent1 = tk.Entry(calc, font=10, width=20, justify="center")
ent1.insert(0, "0")
ent1.place(x=265, y=70)
ent2 = tk.Entry(calc, font=10, width=20, justify="center")
ent2.insert(0, "0")
ent2.place(x=10, y=70)
res = tk.Label(calc, fg="blue", font=("Segoe UI", 20), text="0")
res.place(x=20, y=112)
combob = ttk.Combobox(calc, width=2, font=50, values=("+", "-", "x", "÷", "^", "√", "%", "//", "~", "m."))
combob.current(0)
combob.place(x=209, y=70)
def calculate():
	try:
		x = float(ent1.get())
		y = float(ent2.get())
	except ValueError:
		res.config(text="تأكد من المدخلات")
		return
	match combob.get():
		case '+':
			result = round((x + y), 14)
		case '-':
			result = round((x - y), 14)
		case 'x':
			result = x * y
		case '÷':
			try:
				result = x / y
			except ZeroDivisionError:
				result = "لا يمكن القسمة على صفر"
		case '^':
			result = round((x ** y), 14)
		case '√':
			try:
				result = round((x ** (1 / y)), 14)
			except ZeroDivisionError:
				result = "لا يمكن القسمة على صفر"
		case '%':
			try:
				result = round((x % y), 14)
			except ZeroDivisionError:
				result = "لا يمكن القسمة على صفر"
		case '//':
			try:
				result = x // y
			except ZeroDivisionError:
				result = "لا يمكن القسمة على صفر"
		case '~':
			result = round(x, int(y))
		case "m.":
			result = ((x + y) / 2)
		case _:
			result = "تأكد من المدخلات"
	res.config(text=result)
eq = tk.Button(calc, text="=", font=50, command=calculate)
eq.place(x=415, y=120)
calc.mainloop()