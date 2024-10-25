from tkinter import *
import Aron_Bejelentkezve

def aronfuggveny():
    master = Tk()
    master.geometry("700x500")
    master.title("Áron profilja")
    master.configure(bg="black")
    
    def ujabblaknyitas_aronnak():
        Aron_Bejelentkezve.aron_ablak()

    ÁRON_ábra= Label(master, text="📞", fg="#28e8fa", bg="black",font=('Times', 70, 'bold'))
    ÁRON_ábra.grid(row= 0, columnspan=3,pady=(10,0), padx=320)
    
    cím_áron = Label(master, text="Bejelentkezés", bg="black", fg="#28e8fa", font=('Comic Sans', 60, 'bold'))
    cím_áron.grid(row=1, columnspan=3, pady=(6, 0), padx=120)

    neve_áron = Label(master, text="Áron profiljába", bg="black", fg="#28e8fa", font=('Comic Sans', 30, 'bold'))
    neve_áron.grid(row=2, columnspan=3, pady=(15, 20), padx=110)

    jelszo_aron = Label(master, text="Írja be a jelszóját: ", fg="#28e8fa", bg="black", font=('Comic Sans', 10, 'bold'))
    jelszo_aron.grid(row=4, columnspan=3, pady=4, padx=5)

    aron_erteke = Entry(master, width=20, fg="#black", bg="#28e8fa",  borderwidth=2)
    aron_erteke.grid(row=5, columnspan=3, pady=3, padx=5)
    
    def ellenoriz_aronnak():
        bekert_ertek_aron = aron_erteke.get()
        if bekert_ertek_aron == "asd":
            master.destroy()
            ujabblaknyitas_aronnak()
        else:
            rossz_aron = Label(master, text="Rossz jelszó, próbáld újra", bg="black", fg="#28e8fa", font=('Comic Sans', 16, 'bold'))
            rossz_aron.grid(row=6, column=1, pady=10, padx=20)

    ellenorzo_aronnak = Button(master, text="Ellenőrzés!", fg="#28e8fa", bg="black", font="sans 13 bold", command=ellenoriz_aronnak)
    ellenorzo_aronnak.grid(row=8, column=1, pady=10, padx=20)

