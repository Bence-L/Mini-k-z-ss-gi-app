from tkinter import *
# Root -> a fő widget (a fő ablak)
root = Tk()

# Létrehozzuk a labelt
cím = Label(root, text="Közösségi app", font=('Comic Sans', 60, 'bold'))

# This will import all the widgets and modules which are available in
# tkinter and ttk module
import Áron_Profilja
import Bence_Profilja


master = Tk()


# sets the geometry and the title of the main root window
master.geometry("500x400")
master.title("Főoldal")


# function to open a new window 
# on a button click
def openNewWindow():
    Áron_Profilja.mainFunction()
    
    
def openNewWindow2():
    Bence_Profilja.foFuggveny()


label = Label(master, text ="Válaszd ki, hogy melyik \n profilba szeretnél belépni", font="sans 22 bold").grid(row= 1, columnspan=3, pady=10, padx=5)


# a button widget which will open a 
# new window on button click
btn = Button(master, text ="Áronéba", fg="white", bg="lightblue", font="sans 20 bold", command = openNewWindow).grid(row= 2, column=0, padx=(5, 5))
btn2 = Button(master, text ="Bencéébe", fg="white", bg="lightblue", font="sans 20 bold", command = openNewWindow2).grid(row= 2, column=2, padx=(5, 5))


#quit button
bezaro_gomb = Button(master, text="Bezárás", bg="red", font="sans 20 bold", command=master.destroy).grid(row=6, column=1)


# mainloop, runs infinitely
mainloop()

# Betesszük a labelt az ablakba, és pont akkor lesz így az ablak, amekkora a szöveg
cím.grid(row= 0, columnspan=3, pady=10, padx=5)

# Event loop létrehozása
root.mainloop()
