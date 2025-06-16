from tkinter import *
from datetime import datetime

def what_time():
    dnow = datetime.now()
    btn.config(text = dnow)

win = Tk()
win.geometry("600x100")
win.title("Chobo_Coding")

ent = Entry(win)
ent.pack()
def ent_p():
    a=ent.get()
    print(a)

btn = Button(win, text = "Time")
btn.pack()
btn.config(width=30,height=3)
btn.config(command = what_time)

win.mainloop