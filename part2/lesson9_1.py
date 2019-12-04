from tkinter import Tk, Button, Entry, Frame, Label, LabelFrame

root = Tk()
root.geometry('600x400+500+200')

f_top = Frame(root)
f_top.pack()
f_bottom = Frame(root)
f_bottom.pack()


l1 = Label(f_top, text='1', font=15, fg='#fff', bg='#3498db', width=8, height=4)
l1.pack(side='left')
l2 = Label(f_top, text='2', font=15, fg='#fff', bg='#2ecc71', width=8, height=4)
l2.pack(side='left')
l3 = Label(f_bottom, text='3', font=15, fg='#fff', bg='#f1c40f', width=8, height=4)
l3.pack(side='left')
l4 = Label(f_bottom, text='4', font=15, fg='#fff', bg='#34495e', width=8, height=4)
l4.pack(side='left')


root.mainloop()
