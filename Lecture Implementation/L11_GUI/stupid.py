from tkinter import *
import time

win = Tk("Test")
win.geometry('400x200')


def yes_func():
    frame1.pack_forget()
    frame2.pack()
    # time.sleep(2)
    # win.quit()


def back_func():
    frame2.pack_forget()
    frame1.pack()


frame1 = Frame(win, width=400, height=200)
title = Label(frame1, text='Are you stupid?', font='Calibri')
title.pack(pady=40)
but1 = Button(frame1, text='Yes', command=yes_func)
but1.pack()
but2 = Button(frame1, text='No')
but2.pack()
frame1.pack()

frame2 = Frame(win, width=400, height=200)
label2 = Label(frame2, text='I knew it!', font='Calibri')
label2.pack()
but3 = Button(frame2, text='Back', command=back_func)
but3.pack()


win.mainloop()