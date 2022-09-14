import tkinter
canvas = tkinter.Canvas(width=800, height=200, background='white')
canvas.pack()
entry1 = tkinter.Entry()
entry1.pack()

#vykreslenie platna

def x():
#funkcia vykresli
    subor = open('zastavba_na_ulici.txt')

#otvorenie suboru




button1 = tkinter.Button(text='ulica', command=x)
button1.pack()

#vykreslenie buttonu

canvas.mainloop()
