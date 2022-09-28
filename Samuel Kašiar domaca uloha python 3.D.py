import tkinter # importovanie kniznice pre platno ( tkinter ) 
canvas = tkinter.Canvas(width=450, height=200, bg='white') # rozmery a farba platna
canvas.pack()

def vykresli():
    for i in range(len(farby)):
        canvas.create_rectangle(x+i*vel, y, x+i*vel+vel-2, y+vel-2,
                                fill=farby[i], outline='')



canvas.create_text(210, 40, text='VÝBER JEDLA', font='Arial 20', fill='red') #vykreslenie textu
subor = open('vyber_jedla.txt', 'w') # otvorenie suboru
subor.close() # zavrerie suboru
farby = ['green', 'red', 'blue', 'orange'] # zafarbenie štvorcov
skratky = 'zcmo' 
x, y, vel = 23, 65, 105 # velkost a kompozicia štvorcov
vykresli() # funkcia na vykreslenie

canvas.bind('<Button-1>')
label1 = tkinter.Label(text='kód študenta:')
label1.pack()
entry1 = tkinter.Entry()
entry1.pack()

