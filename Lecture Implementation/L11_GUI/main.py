from tkinter import *


root = Tk()  # creating the root window where all widgets go
width = 500  # in pixels
height = 300  # put the dimensions in variables to refer to them again

# no need to memorize how to manipulate the position of the window
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry(f'{width}x{height}+{int(x)}+{int(y)}')  # the coordinate of the upper left corner
# f stands for format; variable inside string. paired with curly braces
# the curly braces tell the interpreter that this is a variable inside the string
# window.geometry(f'{width_variable}x{height_variable}
# +{int(center coordinate on x-axis)}+int(center coordinate on y-axis)}')
# must put both int(x) and int(y) for the positioning to work

text1 = Label(root, text="This is my first GUI window!")  # inheritance example; child class of Tk
text1.pack()  # display it on the window

def exitClick():
    # event handler; mouse clicks/scrolls/etc. are events; anything done by the user
    # functions that deal with events
    root.quit()  # main.destroy()
exitButton = Button(root, text="Exit", command=exitClick)  # command function WITHOUT parentheses
exitButton.pack()  # adds it to the window

root.mainloop()


"""
create interface
add widgets
connect to the window
"""