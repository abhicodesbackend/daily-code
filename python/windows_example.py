from tkinter import *
from tkinter import messagebox
win = Tk()
one=messagebox.askokcancel('title1 ','really?')
if one:
	print(one)
two=messagebox.askokcancel('title2 ','really?')
print(two)
three=messagebox.askokcancel('title3 ','really?')
print(three)
messagebox.showinfo('title','a tk messagebox, \n would you like \t to open this command?')
messagebox.showwarning('warning','a tk warning')
messagebox.showerror('error','a tk error')
win.mainloop()