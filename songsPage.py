from distutils.command.clean import clean
from tkinter import *
from tkmacosx import Button
import glob
import os

import learnCantonese as lc
from utils import *

# ------------------------------------------------------------------
#  Main Page
#   ** Mian/Select Songs, Main/New Words **
# ------------------------------------------------------------------

def mainPage(ws, method='not delete'):

    # Create components
    menubar(ws, gamePage, newWordsPage)
    buttonframe = Frame(ws)

    b1 = Button(buttonframe, text='Select Songs', command=lambda: songPage(ws), width=200, bg='#616161', fg='white')
    b2 = Button(buttonframe, text='Learn New Words', command=lambda: newWordsPage(ws), width=200, bg='#616161', fg='white')
    
    buttonframe.pack(expand=1)
    b1.pack(side=LEFT, padx=10, pady=5)
    b2.pack(side=RIGHT, padx=10, pady=5)

    if method == 'delete':
        buttonframe.destroy()

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

    # Create components
    returnframe = Frame(ws1)
    listframe = Frame(ws1)
    buttonframe = Frame(ws1)

    def songPage_2_mainPage(ws):
        ws1.destroy()
        mainPage(ws, 'delete')
    
    b = Button(returnframe, text='Back', command=lambda: songPage_2_mainPage(ws), width=100, bg='#616161', fg='white')

    all_f = glob.glob('data/songs/*.txt')
    SONG_LIST = [x[11:-4] for x in all_f]

    lb = Listbox(listframe, listvariable=SONG_LIST, borderwidth=0, bg='#3D3D3D', selectbackground='#2B57B7', activestyle='none', selectmode=SINGLE)
    for s in SONG_LIST:
        lb.insert('end', s)

    b1 = Button(buttonframe, text='Play Cantonese', command=lambda: gamePage(ws, ws1, lb), width=200, bg='#616161', fg='white')
    b2 = Button(buttonframe, text='Show Lyrics', command=lambda: lyricsPage(ws, ws1, lb), width=200, bg='#616161', fg='white')

    returnframe.pack(side=TOP, anchor=NW)
    b.pack(padx=10)

    listframe.pack(fill='both', expand=1)
    lb.pack(fill='both', expand=1, padx=10, pady=20)
    
    buttonframe.pack()
    b1.pack(side=LEFT, padx=10, pady=5)
    b2.pack(side=RIGHT, padx=10, pady=5)

    ws1.mainloop()

# ------------------------------------------------------------------
#  Lyrics Page
#  -- Create a Label to display lyrics
# ------------------------------------------------------------------


def lyricsPage(ws, ws1, lb):
    global SONG

    # Lyrics Page
    ws3 = Toplevel(ws1)
    ws3.title('Show Lyrics')
    center_window(ws3)

    get_song(lb)
    ws1.destroy()

    # Create components
    returnframe = Frame(ws3)
    frame = Frame(ws3)

    lyric_dir = f'data/songs/{SONG.get()}.txt'

    def lyricsPage_2_songPage(ws):
        ws3.destroy()
        songPage(ws)
    
    b = Button(returnframe, text='Back', command=lambda: lyricsPage_2_songPage(ws), width=100, bg='#616161', fg='white')

    t = Text(frame, bg='#3D3D3D', font=("arial", 14))
    t.insert('1.0', lc.show_lyrics(lyric_dir))
    t.configure(state='disabled')

    # Show components on screen
    returnframe.pack(side=TOP, anchor=NW)
    frame.pack(fill='both', expand=1, padx=10)

    b.pack(side=TOP, anchor=NW)
    t.pack(expand=1, padx=10, pady=5)

    ws3.mainloop()

# ------------------------------------------------------------------
#  Game Page
#  -- A label to display a line of Cantonese lyric
#  -- An Entry to input Cantoese
#  -- A Label to display comparison
# ------------------------------------------------------------------

def next_lyrics(display_c_l, cn_l, t, e):
    global N

    N += 1
    value = cn_l[N]
    display_c_l.set(value)

    t.delete("1.0", END)
    e.delete(0, END)
    e.focus_set()

def check_lyrics(input_l, cn_l, en_l, w_dir, t, t2):
    global N

    cn_w = list(cn_l.replace(' ', ''))
    en_l = en_l.split(' ')
    check_words = input_l.split(' ')
    new_w = lc.read_new_words(w_dir)

    for w in range(len(check_words)):
        if (check_words[w] != en_l[w]) and ('/' not in en_l[w] or check_words[w] not in en_l[w].split('/')):
            t.insert(END, en_l[w], 'warning')
            t.insert(END, '  ')

            # add to word book
            lc.add_new_words(new_w, cn_w[w], en_l[w])
            lc.output_new_words(w_dir, new_w)

            t2.insert(END, f'{cn_w[w]}: ')
            t2.insert(END, f'{en_l[w]}\t', 'warning')

        else:
            t.insert(END, f'{en_l[w]}  ')

def gamePage(ws, ws1, lb):
    global N, SONG

    # Lyrics Page
    ws2 = Toplevel(ws1)
    ws2.title('Check Cantonese')
    center_window(ws2)

    get_song(lb)
    ws1.destroy()

    # Get lyrics
    lyric_dir = f'data/songs/{SONG.get()}.txt'
    clean_l = lc.read_lyrics(lyric_dir)
    cn_l, en_l = clean_l[::2], lc.split_words_tones(clean_l[1::2])
    N = 0

    display_c_l = StringVar()
    display_c_l.set(cn_l[N])

    # components to input cantonese
    returnframe = Frame(ws2)
    frame = Frame(ws2)

    l = Label(frame, textvariable=display_c_l, bg='#323232', font=("arial", 14), height=2)

    e = Entry(frame, bg='black')
    e.focus_set()

    t = Text(frame, height=2, font=("arial", 14))
    t.tag_config('warning', foreground='#A6FF2E')
    
    # Return button
    def gamePage_2_songPage(ws):
        ws2.destroy()
        songPage(ws)

    back_b = Button(returnframe, text='Back', command=lambda: gamePage_2_songPage(ws), width=100, bg='#616161', fg='white')
 
    returnframe.pack(side=TOP, anchor=NW)
    back_b.pack(padx=10)

    buttonframe = Frame(ws2)
    b1 = Button(buttonframe, text='Check', command=lambda: check_lyrics(e.get(), cn_l[N], en_l[N], W_DIR, t, t2), bg='#616161', fg='white', width=200)
    b2 = Button(buttonframe, text='Next', command=lambda: next_lyrics(display_c_l, cn_l, t, e), bg='#616161', fg='white', width=200)

    frame2 = Frame(ws2)
    t2 = Text(frame2, font=("Helvetica", 14))
    t2.tag_config('warning', foreground='#A6FF2E')


    # show components on screen
    frame.pack()

    l.pack(fill='x', padx=10, pady=5)
    e.pack(fill='x', padx=10, pady=5)
    t.pack(fill='x', padx=10, pady=5)

    buttonframe.pack()
    b1.pack(side=LEFT, padx=10, pady=5)
    b2.pack(side=RIGHT, padx=10, pady=5)

    frame2.pack()
    t2.pack(fill='x', padx=10, pady=5)

# ------------------------------------------------------------------
#  New Words Page
#  -- A label to display a line of Cantonese lyric
#  -- An Entry to input Cantoese
#  -- A Label to display comparison
# ------------------------------------------------------------------

def delete_item(lb):
    selection = lb.curselection()
    lb.delete(selection[0])

def clear_items(lb):
    lb.delete(0, END)

def newWordsPage(ws):
 
    # Lyrics Page
    ws4 = Toplevel(ws)
    ws4.title('New Words')
    center_window(ws4)

    # Frames
    returnframe = Frame(ws4)
    listframe = Frame(ws4)
    buttonframe = Frame(ws4)

    # Create components
    new_w = dict(sorted(lc.read_new_words(W_DIR).items(), key=lambda item: item[1][1], reverse=True))

    # Return button
    def wordPage_2_songPage(ws):
        ws4.destroy()
        mainPage(ws, 'delete')
    
    b = Button(returnframe, text='Back', command=lambda: wordPage_2_songPage(ws4), width=100, bg='#616161', fg='white')

    # listbox
    lb = Listbox(listframe, listvariable=SONG_LIST, borderwidth=0, bg='#3D3D3D', selectbackground='#2B57B7', activestyle='none', selectmode=SINGLE)
    for i in new_w.items():
        lb.insert('end', f'{i[0]}: {i[1][0]}')

    # buttons
    delete_button = Button(buttonframe, text='Delete', command=lambda: delete_item(lb), width=200, bg='#616161', fg='white')
    clear_button = Button(buttonframe, text='Clear', command=lambda: clear_items(lb), width=200, bg='#616161', fg='white')

    returnframe.pack(side=TOP, anchor=NW)
    b.pack(padx=10)

    listframe.pack(fill='both', expand=1)
    lb.pack(fill='both', expand=1, padx=10, pady=20)

    buttonframe.pack()
    delete_button.pack(side=LEFT, padx=10, pady=5)
    clear_button.pack(side=RIGHT, padx=10, pady=5)

    ws4.mainloop()

# ------------------------------------------------------------------
#  Excution 
#
# ------------------------------------------------------------------

if __name__ == '__main__':

    ws = Tk()
    ws.title('Learning Cantonese')
    center_window(ws)

    SONG_LIST = StringVar()
    SONG = StringVar()
    NUM_L = 0
    W_DIR = 'data/new words.json'

    mainPage(ws)

    ws.mainloop()
