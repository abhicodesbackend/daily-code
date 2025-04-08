'''
from tkinter import *
win = Tk()
Button(win,text='quit',command=win.quit).pack()

def shit():
	print('abhi')
	win.mainloop()
	print(i)

for i in range(5):
	shit()
'''
from tkinter import *
master = Tk()
from PIL import Image, ImageTk
load=Image.open('1.JPG')
render=ImageTk.PhotoImage(load)
img=Label(image=render)
img.image=render
img.place(x=10,y=100)
master.mainloop()


