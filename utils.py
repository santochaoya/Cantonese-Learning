from tkinter import *
from tkmacosx import Button


def center_window(window):
    """Initial window size and postion
    """

    # Window size
    ws_width = 600
    ws_height = 450

    # Set Window to center
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    center_x = int(screen_width/2 - ws_width/2)
    center_y = int(screen_height/2 - ws_height/2)

    # set window to the center of the screen
    window.geometry(f'{ws_width}x{ws_height}+{center_x}+{center_y}')

    # prohibit resizing
    window.resizable(False, False)

    # Add window icon
    window.iconbitmap('assets/windowIcon.icns')
