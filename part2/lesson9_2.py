from tkinter import Tk, Button, Entry, Frame, Label, LabelFrame

root = Tk()
root.geometry('600x400+500+200')


lf_top = LabelFrame(root, text='Top Label Frame', padx=10, pady=10)
lf_top.pack(pady=10)

lf_bottom = LabelFrame(root, text='Bottom Label Frame')
lf_bottom.pack()

l5 = Label(lf_top, text='1', font=15, fg='#fff', bg='#3498db', width=8, height=4)
l5.pack(side='left')
l6 = Label(lf_top, text='2', font=15, fg='#fff', bg='#2ecc71', width=8, height=4)
l6.pack(side='left')
l7 = Label(lf_bottom, text='3', font=15, fg='#fff', bg='#f1c40f', width=8, height=4)
l7.pack(side='left')
l8 = Label(lf_bottom, text='4', font=15, fg='#fff', bg='#34495e', width=8, height=4)
l8.pack(side='left')

root.mainloop()
