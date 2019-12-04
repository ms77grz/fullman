from tkinter import Tk, Button, Entry, Frame, Label, LabelFrame

root = Tk()
root.geometry('600x400+500+200')


lf_top = LabelFrame(root, text='Top Label Frame', padx=10, pady=10)
lf_top.pack(pady=10)

lf_bottom = LabelFrame(root, text='Bottom Label Frame', padx=10, pady=10)
lf_bottom.pack()

l1 = Label(lf_top, text='1', font=15, fg='#fff',
           bg='#3498db', width=8, height=4)
l1.pack(side='left')
l2 = Label(lf_top, text='2', font=15, fg='#fff',
           bg='#2ecc71', width=8, height=4)
l2.pack(side='left')
l3 = Label(lf_bottom, text='3', font=15, fg='#fff',
           bg='#f1c40f', width=8, height=4)
l3.pack(side='left')
l4 = Label(lf_bottom, text='4', font=15, fg='#fff',
           bg='#34495e', width=8, height=4)
l4.pack(side='left')

root.mainloop()
