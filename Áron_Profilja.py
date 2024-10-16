from tkinter import *
import Aron_Bejelentkezve

def aronfuggveny():
    master = Tk()
    master.geometry("1000x800")
    master.title("Áron profilja")
    master.configure(bg="black")
    
    def ujabblaknyitas_aronnak():
        Aron_Bejelentkezve.ablakja()
    
    cím_áron = Label(master, text="Bejelentkezés", bg="#00FF9C", font=('Comic Sans', 60, 'bold'))
    cím_áron.grid(row=0, columnspan=3, pady=10, padx=5)

    neve_áron = Label(master, text="Áron profiljába", bg="#00FF9C", font=('Comic Sans', 30, 'bold'))
    neve_áron.grid(row=1, columnspan=3, pady=10, padx=5)

    jelszo_aron = Label(master, text="Írja be a jelszóját: ", fg="red", bg="black", font=('Comic Sans', 10, 'bold'))
    jelszo_aron.grid(row=2, columnspan=3, pady=10, padx=5)

    aron_erteke = Entry(master, width=20, bg="#00FF9C", borderwidth=2)
    aron_erteke.grid(row=3, columnspan=3, pady=10, padx=5)
    
    def ellenoriz_aronnak():
        bekert_ertek_aron = aron_erteke.get()
        if bekert_ertek_aron == "asd":
            master.destroy()
            ujabblaknyitas_aronnak()
        else:
            rossz_aron = Label(master, text="Rossz jelszó, próbáld újra", bg="black", fg="red", font=('Comic Sans', 16, 'bold'))
            rossz_aron.grid(row=7, column=1, pady=10, padx=20)

    ellenorzo_aronnak = Button(master, text="Ellenőrzés!", fg="red", bg="black", font="sans 13 bold", command=ellenoriz_aronnak)
    ellenorzo_aronnak.grid(row=8, column=1, pady=10, padx=20)
    
    

# Event loop létrehozása