from tkinter import Tk, Button, Entry, Frame, Label, LabelFrame

root = Tk()
root.geometry('600x400+500+200')

l1 = Label(root, text='HELLO', font=15, fg='#fff', bg='#ff0000', width=8, height=4)
l1.pack(expand=1, anchor='se')

root.mainloop()
