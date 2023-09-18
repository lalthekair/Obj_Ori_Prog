"""
- Exit button.
- 320 * 250 = w * l
- Displayed in the middle.
"""

from tkinter import *


window = Tk()
width = 320
height = 250
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
window.geometry(f'{width}x{height}+{int(x)}+{int(y)}')


def on_click():
    entry.delete(0, END)
    entry.insert(0, 'A')
def on_click2():
    entry.delete(0, END)
    entry.insert(0, 'B')
def on_click3():
    entry.delete(0, END)
    entry.insert(0, 'C')
# we cannot disable the entry widget because these functions are writing on the widget


entry = Entry(window, width=25)
entry.pack()
# Add Buttons in the window
b1 = Button(window, text="A", command=on_click)
b1.pack()
b2 = Button(window, text="B", command=on_click2)
b2.pack()
b3 = Button(window, text="C", command=on_click3)
b3.pack()


exitButton = Button(window, text="Exit", command=window.destroy)
exitButton.pack()  # adds it to the window

window.mainloop()
