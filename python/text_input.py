from tkinter import *
def btn_pressed():
	btn['text']=var.get()
root = Tk()
root.title('something')
root.geometry('500x500')
root.configure(background='pink')
var=StringVar()
entry=Entry(root,width=10,bd=4,textvariable=var)
entry.pack()
btn=Button(root,text='ok',command=btn_pressed)
btn.pack()
root.mainloop()
print(btn)