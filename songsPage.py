from tkinter import *
from turtle import width
from tkmacosx import Button
import glob

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
#  Create a listbox to show all songs
#  -- order of songs is based on sort method in folder
# ------------------------------------------------------------------

song_list = StringVar()

all_f = glob.glob('data/songs/*.txt')
song_list = [x[11:-4] for x in all_f]

lb = Listbox(ws, listvariable=song_list, width=50, height=20, borderwidth=0, bg='#3D3D3D', selectbackground='#2B57B7', activestyle='none')
for s in song_list:
    lb.insert('end', s)

# ------------------------------------------------------------------
#  Create buttons for next step
#  ** Play Cantonese, Show Lyrics **
# ------------------------------------------------------------------

def mainPage():
    ws.destroy()
    import playPage

def lyricsPage():
    ws.destroy()
    import lyricsPage

b1 = Button(ws, text='Play Cantonese', command=mainPage, width=200, bg='#616161', fg='white')
b2 = Button(ws, text='Show Lyrics', command=mainPage, width=200, bg='#616161', fg='white')

# ------------------------------------------------------------------
#  Display all components on window
#  ** Listbox, 2 Buttons **
# ------------------------------------------------------------------

lb.grid(column=0, row=0, columnspan=2, padx=75, pady=20)
b1.grid(column=0, row=1, padx=10, pady=10)
b2.grid(column=1, row=1, padx=10, pady=10)

ws.mainloop()