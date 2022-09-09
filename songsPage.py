from tkinter import *
from tkmacosx import Button
import glob
import os

import learnCantonese as lc
from utils import *

# ------------------------------------------------------------------
#  Create menu bar
#   ** Mian/Select Songs, Main/New Words **
# ------------------------------------------------------------------



# ------------------------------------------------------------------
#  Select Song Page
#  -- Create a listbox to show all songs
#  -- Create buttons for next step
# ------------------------------------------------------------------

def get_song(lb):
    value = lb.get(lb.curselection())
    SONG.set(value)
        
def songPage(ws):

    # Song Page
    ws1 = Toplevel(ws)
    ws1.title('Select Songs')
    center_window(ws1)

    # Create a listbox
    all_f = glob.glob('data/songs/*.txt')
    SONG_LIST = [x[11:-4] for x in all_f]

    lb = Listbox(ws1, listvariable=SONG_LIST, width=50, height=20, borderwidth=0, bg='#3D3D3D', selectbackground='#2B57B7', activestyle='none', selectmode=SINGLE)
    for s in SONG_LIST:
        lb.insert('end', s)
    
    # Create buttons
    def enter_lyricsPage(ws, lb):
        lyricsPage(ws, lb)
        ws1.destroy()


    b1 = Button(ws1, text='Play Cantonese', command=lambda: gamePage(ws2), width=200, bg='#616161', fg='white')
    b2 = Button(ws1, text='Show Lyrics', command=lambda: enter_lyricsPage(ws, lb), width=200, bg='#616161', fg='white')

    lb.grid(column=0, row=0, columnspan=2, padx=75, pady=20)
    b1.grid(column=0, row=1, padx=10, pady=10)
    b2.grid(column=1, row=1, padx=10, pady=10)


    ws1.mainloop()

# -----------------------------------------------20-------------------
#  Lyrics Page
#  -- Create a Label to display lyrics
# ------------------------------------------------------------------


def lyricsPage(ws, lb):

    # Lyrics Page
    ws3 = Toplevel(ws)
    ws3.title('Show Lyrics')
    center_window(ws3)
    
    get_song(lb)

    # Create a text
    lyric_dir = f'data/songs/{SONG.get()}.txt'

    t = Text(ws3, bg='#3D3D3D', width=82, height=28)
    t.insert('1.0', lc.show_lyrics(lyric_dir))
    t.configure(state='disabled')

    # Return button
    def back_songPage(ws):
        ws3.destroy()
        songPage(ws)
    
    b = Button(ws3, text='Back', command=lambda: back_songPage(ws), width=200, bg='#616161', fg='white')

    t.grid(column=0, row=0, padx=10, pady=20)
    b.grid(column=0, row=1, pady=10)

    ws3.mainloop()

# ------------------------------------------------------------------
#  Game Page
#  ** Listbox, 2 Buttons **
# ------------------------------------------------------------------

def gamePage(ws):
    ws1.destroy()
    import playPage

def newBooksPage(ws):
    import newBooksPage



if __name__ == '__main__':

    ws = Tk()
    ws.title('Learning Cantonese')
    center_window(ws)

    SONG_LIST = StringVar()
    SONG = StringVar()
    
    # Create components
    menubar(ws, gamePage, newBooksPage)

    b1 = Button(ws, text='Select Songs', command=lambda: songPage(ws), width=200, bg='#616161', fg='white')
    b2 = Button(ws, text='Learn New Words', command=lambda: newBooksPage(ws), width=200, bg='#616161', fg='white')
    b1.pack()

    ws.mainloop()
