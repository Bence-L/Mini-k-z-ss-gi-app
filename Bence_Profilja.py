from tkinter import *
import Bence_Bejelentkezve

def bencefuggveny():
    master = Tk()
    master.geometry("700x500")
    master.title("Bence profilja")
    master.configure(bg="black")
    def ujabblaknyitas():
                Bence_Bejelentkezve.bence_ablak()
    
    ábra= Label(master, text="📞", fg="#28e8fa", bg="black",font=('Times', 70, 'bold'))
    ábra.grid(row= 0, columnspan=3,pady=(10,0), padx=320)

    cim_bence = Label(master, text="Bejelentkezés", bg="black", fg="#28e8fa", font=('Comic Sans', 50, 'bold'))
    cim_bence.grid(row=1, columnspan=3, pady=(6, 0), padx=120)

    neve_bence = Label(master, text="Bence profiljába", bg="black", fg="#28e8fa", font=('Comic Sans', 20, 'bold'))
    neve_bence.grid(row=2, columnspan=3, pady=(15, 20), padx=110)

    jelszo_bence = Label(master, text="Írja be a jelszóját: ", fg="#28e8fa", bg="black", font=('Comic Sans', 10, 'bold'))
    jelszo_bence.grid(row=4, columnspan=3, pady=4, padx=5)

    # A jelszó bevitelének elrejtése
    bence_erteke = Entry(master, width=20, bg="#28e8fa", show="*")
    bence_erteke.grid(row=5, columnspan=3, pady=3, padx=5)

    def ellenoriz():
        bekert_ertek = bence_erteke.get()
        if bekert_ertek == "Bence":
            # Fő ablak bezárása sikeres bejelentkezés esetén
            master.destroy()
            ujabblaknyitas()
        else:
            rossz = Label(master, text="Rossz jelszó, próbáld újra", bg="black",fg="#28e8fa", font=('Comic Sans', 16, 'bold'))
            rossz.grid(row=7, column=1, pady=10, padx=20) 

    # Ellenőrző gomb, amely hívja az ellenőrző függvényt
    ellenorzo = Button(master, text="Ellenőrzés!", fg="#28e8fa", bg="black", font="sans 13 bold", command=ellenoriz)
    ellenorzo.grid(row=6, column=1, pady=10, padx=20)

    # Bezáró gomb
    bezaro_gomb = Button(master, text="Bezárás", bg="#ed735a", font="sans 13 bold", command=master.destroy)
    bezaro_gomb.grid(row=8, column=1, pady=10, padx=20)



#egyik szín #285cfa
#masik szín #28e8fa
#gomb szín #ed735a