from tkinter import *
# Root -> a fő widget (a fő ablak)


# Létrehozzuk a labelt


# This will import all the widgets and modules which are available in
# tkinter and ttk module
import Áron_Profilja
import Bence_Profilja


master = Tk()


# sets the geometry and the title of the main root window
master.geometry("1000x800")
master.title("Főoldal")
master.configure(bg="black")

# function to open a new window 
# on a button click
def openNewWindow():
    Áron_Profilja.aronfuggveny()
    
    
def openNewWindow2():
    Bence_Profilja.bencefuggveny()
cím = Label(master, text="Közösségi app", bg="#00FF9C",font=('Times', 50))
cím.grid(row= 0, columnspan=3,pady=(35,0), padx=280)
label = Label(master, text ="Válaszd ki, hogy melyik profilba szeretnél belépni",bg="#00FF9C" ,font="sans 16 bold").grid(row= 1, columnspan=3, pady=(35,40), padx=5)


# a button widget which will open a 
# new window on button click
btn = Button(master, text ="Áronéba", bg="#00FF9C", font="sans 30 bold", command = openNewWindow).grid(row= 2, column=0, pady=40,padx=(25, 25))
btn2 = Button(master, text ="Bencéébe", bg="#00FF9C", font="sans 30 bold", command = openNewWindow2).grid(row= 2, column=2, pady=40,padx=(25, 25))


#quit button
bezaro_gomb = Button(master, text="Bezárás", bg="#733C3C", font="sans 23 bold", command=master.destroy).grid(row=6, column=1,pady=75,padx=20)


# mainloop, runs infinitely
mainloop()

# Betesszük a labelt az ablakba, és pont akkor lesz így az ablak, amekkora a szöveg


# Event loop létrehozása