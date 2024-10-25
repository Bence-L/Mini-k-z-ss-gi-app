from tkinter import *
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
ábra= Label(master, text="📞", fg="#285cfa", bg="black",font=('Times', 80, 'bold'))
ábra.grid(row= 0, columnspan=3,pady=(10,0), padx=320)
cím = Label(master, text="Messenger+", fg="#285cfa",bg="black",font=('Times', 60,'bold'))
cím.grid(row= 1, columnspan=3,pady=(1,0), padx=320)
label = Label(master, text ="Válasszon egy profilt!",bg="black", fg="#28e8fa" ,font="sans 16 bold").grid(row= 2, columnspan=3, pady=(10,40), padx=5)

#GOMBSTÍLUS


# a button widget which will open a 
# new window on button click
aron_valaszt = Button(master, text ="Áron", bg="#28e8fa", font="Times 30 bold",  borderwidth=20,command = openNewWindow).grid(row= 4, column=0, pady=10,padx=(25, 25))
bence_valaszt = Button(master, text ="Bence", bg="#28e8fa", font="Times 30 bold",  borderwidth=20, command = openNewWindow2).grid(row= 4, column=2, pady=10,padx=(25, 25))
bence_emoji = Label(master, text="🏆", bg="black",fg="#285cfa",font=('Times', 35))
bence_emoji.grid(row= 3, column=2, pady=5,padx=(25, 25))
aron_emoji = Label(master, text="⚽", bg="black",fg="#285cfa",font=('Times', 35))
aron_emoji.grid(row= 3, pady=5,padx=(25, 25))
#quit button
bezaro_gomb = Button(master, text="Bezárás", bg="#ed735a", font="sans 23 bold", command=master.destroy).grid(row=6, column=1,pady=75,padx=20)

mainloop()

#egyik szín #285cfa
#masik szín #28e8fa
#gomb szín #ed735a