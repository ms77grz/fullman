from tkinter import Tk, Button, Entry, Frame, Label, LabelFrame

root = Tk()
root.geometry('600x400+500+200')

l1 = Label(root, text='HELLO', font=15, fg='#fff', bg='#f1c40f', width=8, height=4)
l1.pack(expand=1, anchor='nw')
l2 = Label(root, text='HELLO', font=15, fg='#fff', bg='#f1c40f', width=8, height=4)
l2.pack(expand=1, anchor='ne')
l3 = Label(root, text='HELLO', font=15, fg='#fff', bg='#f1c40f', width=8, height=4)
l3.pack(expand=1, anchor='sw')
l4 = Label(root, text='HELLO', font=15, fg='#fff', bg='#f1c40f', width=8, height=4)
l4.pack(expand=1, anchor='se')

root.mainloop()
