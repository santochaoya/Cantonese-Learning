from tkinter import *


root = Tk()
root.title('Frames')
root.geometry('500x250+300+300')

# Position frame
frame = LabelFrame(root, text='Such a dilemma', padx=25, pady=25)
frame.pack(padx=10, pady=50)

# What do the buttons do
def bad():
    frame.grid_forget()
    b.grid_forget()
    b2.grid_forget()
    slechtekeuze = Label(frame, text='Bad choice')
    slechtekeuze.grid(row=0, column=0, columnspan=2)

    # Option to got back
    homepage = Button(frame, text='Go back', command=back)
    homepage.grid(row=1, column=0, columnspan=2, pady=10)

def good():
    frame.grid_forget()
    b.grid_forget()
    b2.grid_forget()
    slechtekeuze = Label(frame, text='Good choice')
    slechtekeuze.grid(row=0, column=0, columnspan=2)

    # Option to go back
    homepage = Button(frame, text='Terug', command=back)
    homepage.grid(row=1, column=0, columnspan=2, pady=10)


def back():
    frame.grid_forget()
    frame1 = LabelFrame(root, text='Such a dilemma', padx=25, pady=25)
    frame1.pack(padx=10, pady=50)

    b = Button(frame1, text="Don't click!!!", fg='red', command=bad)
    b2 = Button(frame1, text='Click!!!', fg='green', command=good)

    b.grid(row=0, column=0, padx=3)
    b2.grid(row=0, column=1, padx=3)

# Create the buttons and put them in the frame
b = Button(frame, text="Don't click!!!", fg='red', command=bad)
b2 = Button(frame, text='Click!!!', fg='green', command=good)

b.grid(row=0, column=0, padx=3)
b2.grid(row=0, column=1, padx=3)

root.mainloop()
