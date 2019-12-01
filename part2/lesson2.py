from tkinter import Tk, Button
from tkinter import ttk
import sys

root = Tk()

root.geometry('600x400+500+200')

def clicker():
    print('Mission Initiation')

btn = Button(root, text='Start', command=clicker, font='Arial 20')
btn.pack()

btn2 = ttk.Button(root, text='Stop', command=sys.exit)
btn2.pack()

btn3 = Button(root, text='Login', width=20, height=2)
btn3.pack()

btn4 = Button(root, text='Logout', font=('Comic Sans MS', 20, 'italic'))
btn4.pack()

btn5 = Button(root, text='Edit')
btn5.configure(width=8, height=2)
btn5['font'] = 'Arial 20'
btn5.pack()

btn6 = Button(root, text='Mission Completed\nThe Game Is Over', justify='right')
btn6.pack()

root.mainloop()