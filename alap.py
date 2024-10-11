from tkinter import *
# Root -> a fő widget (a fő ablak)
root = Tk()

# Létrehozzuk a labelt
myLabel = Label(root, text="Közösségi app", font=('Comic Sans', 60, 'bold'))

# Betesszük a labelt az ablakba, és pont akkor lesz így az ablak, amekkora a szöveg
myLabel.pack()

# Event loop létrehozása
root.mainloop()