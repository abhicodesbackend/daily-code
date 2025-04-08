from tkinter import *
from tkinter import ttk

def againsomething():
	someshit = Tk()
	#Checkbutton(someshit,text='Check here!',command=someshit.quit).pack(side=BOTTOM)
	Button(someshit,text='Check here!',command=someshit.quit).pack()
	someshit.geometry('300x300')
	#someshit.mainloop()
#againsomething()

def something():
	shit = Tk()
	#Checkbutton(shit,text='Bang here!',command=shit.quit).pack(side=BOTTOM)
	Button(shit,text='Bang here!',command=againsomething()).pack()
	shit.geometry('600x600')
	shit.mainloop()
something()

def againsomething():
	someshit = Tk()
	#Checkbutton(someshit,text='Check here!',command=someshit.quit).pack(side=BOTTOM)
	Button(someshit,text='Check here!',command=someshit.quit).pack()
	#someshit.mainloop()
#againsomething()