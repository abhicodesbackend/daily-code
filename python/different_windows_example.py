from tkinter import *
from tkinter import messagebox
#win = Tk()
run=Tk()
one=messagebox.askyesno('title1 ','I love you!')
print(one)
two=messagebox.askokcancel('title2 ','really?')
print(two)
three=messagebox.askokcancel('title3 ','really?')
print(three)
messagebox.showinfo('info','a tk messagebox')
messagebox.showwarning('warning','a tk warning')
messagebox.showerror('error','a tk error')
#win.mainloop()