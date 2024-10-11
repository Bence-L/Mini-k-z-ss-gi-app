from tkinter import *

def bencefuggveny():
    master = Tk()
    master.geometry("700x500")
    master.title("Bence profilja")
    master.configure(bg="black")

    cim_bence = Label(master, text="Bejelentkezés", bg="#00FF9C", font=('Comic Sans', 50, 'bold'))
    cim_bence.grid(row=0, columnspan=3, pady=(35, 0), padx=120)

    neve_bence = Label(master, text="Bence profiljába", bg="#00FF9C", font=('Comic Sans', 20, 'bold'))
    neve_bence.grid(row=1, columnspan=3, pady=(15, 20), padx=110)

    jelszo_bence = Label(master, text="Írja be a jelszóját: ", fg="red", bg="black", font=('Comic Sans', 10, 'bold'))
    jelszo_bence.grid(row=3, columnspan=3, pady=4, padx=5)

    bence_erteke = Entry(master, width=20, bg="#00FF9C")
    bence_erteke.grid(row=4, columnspan=3, pady=3, padx=5)

    def ellenoriz():
        bekert_ertek = bence_erteke.get()
        if bekert_ertek == "Reggel":
            # Fő ablak bezárása sikeres bejelentkezés esetén
            master.destroy()

            # Új ablak nyitása ha sikeres a bejelentkezés
            siker_ablak = Tk()
            siker_ablak.geometry("700x500")
            siker_ablak.configure(bg="black")
            siker_ablak.title("Siker")
            siker_cím = Label(siker_ablak, text="SIKERÜLT", bg="black", fg="#00FF9C", font=('Comic Sans', 70, 'bold'))
            siker_cím.grid(row=0, columnspan=1, pady=10, padx=100)
            vissza_fooldalra = Button(siker_ablak, text="Vissza a főoldalra", bg="red", font="sans 23 bold", command=siker_ablak.destroy)
            vissza_fooldalra.grid(row=1, column=1,pady=75,padx=20)
        else:
            rossz = Label(master, text="Rossz jelszó, próbáld újra", bg="black",fg="red", font=('Comic Sans', 16, 'bold'))
            rossz.grid(row=6, column=1, pady=10, padx=20)

    # Ellenőrző gomb, amely hívja az ellenőrző függvényt
    ellenorzo = Button(master, text="Ellenőrzés!", fg="red", bg="black", font="sans 13 bold", command=ellenoriz)
    ellenorzo.grid(row=5, column=1, pady=10, padx=20)

    # Bezáró gomb
    bezaro_gomb = Button(master, text="Bezárás", bg="red", font="sans 13 bold", command=master.destroy)
    bezaro_gomb.grid(row=7, column=1, pady=10, padx=20)

    master.mainloop()