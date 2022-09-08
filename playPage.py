from tkinter import *
from tkmacosx import Button

from learnCantonese import *
from utils import *

ws = Tk()
ws.title('All Songs')
center_window(ws)

# ------------------------------------------------------------------
#  Create menu bar
#   ** Mian/Select Songs, Main/New Words **
# ------------------------------------------------------------------

def songPage():
    ws.destroy()
    import songsPage

def newBooksPage():
    ws.destroy()
    import newBooksPage

menubar = Menu(ws)
mainmenu = Menu(menubar, tearoff=0)

menubar.add_cascade(label='Main', menu=mainmenu)
mainmenu.add_command(label='Select Songs', command=songPage)
mainmenu.add_command(label='New Words', command=newBooksPage)
mainmenu.add_separator()
mainmenu.add_command(label='Exit', command=ws.quit)

ws.config(menu=menubar)

# ------------------------------------------------------------------
#  Create a text to show a line of Chinese lyric
#  -- iteral to get each line of Chinese lyric
# ------------------------------------------------------------------

cn_l = StringVar()
tl = ['123', '253234', '5234']

cn_l.set(tl)

l = Label(ws, textvariable=cn_l)
l.pack()

# entry to input cantonese
e = Entry(ws)
e.pack()

ws.mainloop()
