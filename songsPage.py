from distutils.command.clean import clean
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
    global SONG

    value = lb.get(lb.curselection())
    SONG.set(value)
        
def songPage(ws):
    global SONG_LIST

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

    b1 = Button(ws1, text='Play Cantonese', command=lambda: gamePage(ws, ws1, lb), width=200, bg='#616161', fg='white')
    b2 = Button(ws1, text='Show Lyrics', command=lambda: lyricsPage(ws, ws1, lb), width=200, bg='#616161', fg='white')

    lb.grid(column=0, row=0, columnspan=2, padx=75, pady=20)
    b1.grid(column=0, row=1, padx=10, pady=10)
    b2.grid(column=1, row=1, padx=10, pady=10)

    ws1.mainloop()

# ------------------------------------------------------------------
#  Lyrics Page
#  -- Create a Label to display lyrics
# ------------------------------------------------------------------


def lyricsPage(ws, ws1, lb):
    global SONG

    # Lyrics Page
    ws3 = Toplevel(ws)
    ws3.title('Show Lyrics')
    center_window(ws3)

    get_song(lb)
    ws1.destroy()

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
#  -- A label to display a line of Cantonese lyric
#  -- An Entry to input Cantoese
#  -- A Label to display comparison
# ------------------------------------------------------------------

def next_lyrics(display_c_l, cn_l):
    global NUM_L

    NUM_L += 1
    value = cn_l[NUM_L]
    display_c_l.set(value)

def check_lyrics(input_l, cn_l, en_l):
    global NUM_L

    cn_w = list(cn_l.replace(' ', ''))
    en_l = en_l.split(' ')
    colored_en_l = en_l.copy()
    check_words = input_l.split(' ')

    for w in range(len(check_words)):
        if (check_words[w] != en_l[w]) and ('/' not in en_l[w] or check_words[w] not in en_l[w].split('/')):
            check_words[w] = RED + check_words[w] + RESET
            colored_en_l[w] = GREEN + en_l[w] + RESET

    output_ls = ' '.join(check_words)    
    correct_ls = ' '.join(colored_en_l)  

    return output_ls, correct_ls


def gamePage(ws, ws1, lb):
    global NUM_L, SONG

    # Lyrics Page
    ws2 = Toplevel(ws)
    ws2.title('Check Cantonese')
    center_window(ws2)

    get_song(lb)
    ws1.destroy()

    # Get lyrics
    lyric_dir = f'data/songs/{SONG.get()}.txt'
    clean_l = lc.read_lyrics(lyric_dir)
    cn_l, en_l = clean_l[::2], lc.split_words_tones(clean_l[1::2])

    NUM_L = 0
    display_c_l = StringVar()
    display_c_l.set(cn_l[NUM_L])
 
    # components to input cantonese
    l = Label(ws2, textvariable=display_c_l, width=64, bg='#3D3D3D')
    e = Entry(ws2, bg='black', width=64)
    t = Text(ws2, height=2, width=54)

    b1 = Button(ws1, text='Check', command=lambda: check_lyrics(e.get(), ws1, lb), width=200, bg='#616161', fg='white')
    b2 = Button(ws2, text='Next', command=lambda: next_lyrics(display_c_l, cn_l), width=200, bg='#616161', fg='white')
    
    l.grid(column=0, row=0, padx=10, pady=20)
    e.grid(column=0, row=1, pady=10)
    t.grid(column=0, row=2, pady=10)
    b1.grid(column=0, row=3, padx=10, pady=10)
    b2.grid(column=1, row=3, padx=10, pady=10)

# ------------------------------------------------------------------
#  New Words Page
#  -- A label to display a line of Cantonese lyric
#  -- An Entry to input Cantoese
#  -- A Label to display comparison
# ------------------------------------------------------------------

def newWordsPage(ws):
    import newBooksPage

if __name__ == '__main__':

    ws = Tk()
    ws.title('Learning Cantonese')
    center_window(ws)

    SONG_LIST = StringVar()
    SONG = StringVar()
    NUM_L = 0
    
    RED = "\033[31m"
    GREEN = "\033[32m"
    RESET = "\033[39m"
    
    # Create components
    menubar(ws, gamePage, newWordsPage)

    b1 = Button(ws, text='Select Songs', command=lambda: songPage(ws), width=200, bg='#616161', fg='white')
    b2 = Button(ws, text='Learn New Words', command=lambda: newWordsPage(ws), width=200, bg='#616161', fg='white')
    b1.pack()

    ws.mainloop()
