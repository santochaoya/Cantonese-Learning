from dis import dis
from tkinter import *
import learnCantonese as lc
from songsPage import next_lyrics
from utils import *


ws = Tk()
ws.title('Check Cantonese')
center_window(ws)

RED = "\033[31m"
GREEN = "\033[32m"
RESET = "\033[39m"

lyric_dir = 'data/songs/寻找独角兽.txt'
clean_l = lc.read_lyrics(lyric_dir)
cn_l, en_l = clean_l[::2], lc.split_words_tones(clean_l[1::2])
N = 0

print(cn_l)

display_c_l = StringVar()
display_c_l.set(cn_l[N])

# components to input cantonese
l = Label(ws, textvariable=display_c_l, width=64, bg='#3D3D3D')
e = Entry(ws, bg='black', width=64)
t = Text(ws, height=4, width=54, font=("Helvetica", 16))

b1 = Button(ws, text='Check', command=lambda: check_lyrics(e.get(), cn_l[N], en_l[N], t), width=200, bg='#616161', fg='white')
b2 = Button(ws, text='Next', command=lambda: next_lyrics(display_c_l, cn_l, t, e), width=200, bg='#616161', fg='white')

l.grid(column=0, row=0, columnspan=2, padx=10, pady=20)
e.grid(column=0, row=1, columnspan=2, pady=10)
e.focus_set()
t.grid(column=0, row=2, columnspan=2, pady=10)
b1.grid(column=0, row=3, padx=10, pady=10)
b2.grid(column=1, row=3, padx=10, pady=10)

def next_lyrics(display_c_l, cn_l, t, e):
    global N

    N += 1
    print(N)
    value = cn_l[N]
    display_c_l.set(value)

    t.delete("1.0", "end")
    e.delete(0, 'end')

def check_lyrics(input_l, cn_l, en_l, t):
    global N

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

    t.delete("1.0", "end")
    t.insert('insert', correct_ls)

ws.mainloop()
