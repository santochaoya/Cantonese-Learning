from tkinter import *
from tkmacosx import Button

from learnCantonese import *
from utils import *

ws = Tk()
ws.title('Learning Cantonese')
center_window(ws)

# Create menu
def songPage():
    ws.destroy()
    import songsPage

def newBooksPage():
    ws.destroy()
    import newBooksPage

# --------------- main menu ------------------

menubar = Menu(ws)
mainmenu = Menu(menubar, tearoff=0)

menubar.add_cascade(label='Main', menu=mainmenu)
mainmenu.add_command(label='Select Songs', command=songPage)
mainmenu.add_command(label='New Words', command=newBooksPage)
mainmenu.add_separator()
mainmenu.add_command(label='Exit', command=ws.quit)

submenu = Menu(mainmenu, tearoff=0)
mainmenu.add_cascade(label='')

# Show menubar on window
ws.config(menu=menubar)

ws.mainloop()

