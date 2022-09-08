from tkinter import *
from tkmacosx import Button

from learnCantonese import *
from utils import *

ws = Tk()
ws.title('Learn Cantonese')
center_window(ws)

# Create menu
def songPage():
    ws.destroy()
    import songsPage

def newBooksPage():
    ws.destroy()
    import newBooksPage

menubar = Menu(ws)
filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Main', menu=filemenu)

filemenu.add_command(label='Select Songs', command=songPage)
filemenu.add_command(label='New Words', command=newBooksPage)
filemenu.add_separator()
filemenu.add_command(label='Exit', command=ws.quit)

# Show menubar on window
ws.config(menu=menubar)

# text to show chinese lyrics
cn_l = StringVar()
tl = ['123', '253234', '5234']

cn_l.set(tl)

l = Label(ws, textvariable=cn_l)
l.pack()

# entry to input cantonese
e = Entry(ws)
e.pack()

ws.mainloop()
