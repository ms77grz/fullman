from tkinter import Tk, Button, Entry, Frame, Label, LabelFrame

root = Tk()
root.geometry('600x400+500+200')

l = Label(root, text='HELLO', font=15, fg='#fff', bg='#f1c40f', width=8, height=4)
l.pack(fill='both', expand=1)

root.mainloop()
