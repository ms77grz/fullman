from tkinter import Tk, Button, Entry, Frame, Label, LabelFrame

root = Tk()
root.geometry('600x400+500+200')


l1 = Label(root, text='1', font=15, fg='#fff', bg='#3498db', width=8, height=4)
l1.pack(side='top')
l2 = Label(root, text='2', font=15, fg='#fff', bg='#2ecc71', width=8, height=4)
l2.pack(side='left')
l3 = Label(root, text='3', font=15, fg='#fff', bg='#f1c40f', width=8, height=4)
l3.pack(side='right')
l4 = Label(root, text='4', font=15, fg='#fff', bg='#34495e', width=8, height=4)
l4.pack(side='bottom')


root.mainloop()
