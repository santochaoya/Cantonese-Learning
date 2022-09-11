from dis import dis
from tkinter import *
import learnCantonese as lc
from songsPage import next_lyrics
from utils import *


ws = Tk()
ws.title('Check Cantonese')
center_window(ws)

lyric_dir = 'data/songs/寻找独角兽.txt'
W_DIR = 'data/new words.json'

clean_l = lc.read_lyrics(lyric_dir)
cn_l, en_l = clean_l[::2], lc.split_words_tones(clean_l[1::2])
N = 0

display_c_l = StringVar()
display_c_l.set(cn_l[N])

# components to input cantonese
l = Label(ws, textvariable=display_c_l, bg='#252525', font=("Helvetica", 14), height=2)

e = Entry(ws, bg='black')
e.focus_set()

t = Text(ws, height=2, font=("Helvetica", 14))
t.tag_config('warning', foreground='green')

t2 = Text(ws, font=("Helvetica", 14))

b1 = Button(ws, text='Check', command=lambda: check_lyrics(e.get(), cn_l[N], en_l[N], W_DIR, t), bg='#616161', fg='white')
b2 = Button(ws, text='Next', command=lambda: next_lyrics(display_c_l, cn_l, t, e), bg='#616161', fg='white')

# Show components on screen
l.grid(column=0, row=0, columnspan=2, sticky='nsew', padx=10, pady=10)
e.grid(column=0, row=1, columnspan=2, sticky='nsew', padx=10, pady=10)

t.grid(column=0, row=2, columnspan=2, sticky='nsew', padx=10, pady=10)

b1.grid(column=0, row=3, sticky='w', padx=10, pady=10)
b2.grid(column=1, row=3, sticky='e', padx=10, pady=10)

t2.grid(column=0, row=4, columnspan=2, sticky='nsew', padx=10, pady=10)

def next_lyrics(display_c_l, cn_l, t, e):
    global N

    N += 1
    value = cn_l[N]
    display_c_l.set(value)

    t.delete("1.0", "end")
    e.delete(0, 'end')
    e.focus_set()

def check_lyrics(input_l, cn_l, en_l, w_dir, t):
    global N

    cn_w = list(cn_l.replace(' ', ''))
    en_l = en_l.split(' ')
    check_words = input_l.split(' ')
    new_w = lc.read_new_words(w_dir)

    for w in range(len(check_words)):
        if (check_words[w] != en_l[w]) and ('/' not in en_l[w] or check_words[w] not in en_l[w].split('/')):
            t.insert('insert', en_l[w], 'warning')
            t.insert('insert', '  ')

            # add to word book
            lc.add_new_words(new_w, cn_w[w], en_l[w])
            lc.output_new_words(w_dir, new_w)

            t2.insert('end', f'{cn_w[w]}: {en_l[w]}\n')

        else:
            t.insert('insert', f'{en_l[w]}  ')

ws.mainloop()
