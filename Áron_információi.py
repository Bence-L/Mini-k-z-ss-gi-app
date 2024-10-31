from tkinter import *
import ÁRON_GALÉRIA

def aroninfo():
    informacioA = Tk()
    informacioA.geometry("480x700")
    informacioA.title("Áron-Információ")
    informacioA.configure(bg="black")
    
    def nyisdmegaronet():
        ÁRON_GALÉRIA.arongaleria()

    emoji = Label(informacioA, text="📜", bg="black", fg="#28e8fa", font=('Comic Sans', 50, 'bold'))
    emoji.grid(row=0, column=0, pady=5, padx=30)

    kie = Label(informacioA, text="Varga Áron", bg="black", fg="#28e8fa", font=('Comic Sans', 50, 'bold'))
    kie.grid(row=1, column=0, pady=5, padx=30)

    info = Label(informacioA, text="Információi", bg="black", fg="#28e8fa", font=('Comic Sans', 30, 'bold'))
    info.grid(row=2, column=0, pady=5, padx=30)
    
    adatok = Label(informacioA, text="Adatok", bg="black", fg="#28e8fa", font=('Comic Sans', 20, 'bold'))
    adatok.grid(row=3,column=0,pady=(50,10), padx=(0,200))

    nev_adatok = Label(informacioA, text="Neve: Varga Áron", bg="black", fg="#28e8fa", font=('Comic Sans', 12, 'bold'))
    nev_adatok.grid(row=4,column=0,pady=2, padx=20)

    szuletesi_adatok = Label(informacioA, text="Született: ....", bg="black", fg="#28e8fa", font=('Comic Sans', 12, 'bold'))
    szuletesi_adatok.grid(row=5,column=0,pady=2, padx=20)

    sport = Label(informacioA, text="Sport: ....", bg="black", fg="#28e8fa", font=('Comic Sans', 12, 'bold'))
    sport.grid(row=6,column=0,pady=2, padx=20)

    szin = Label(informacioA, text="Szín: ....", bg="black", fg="orange", font=('Comic Sans', 12, 'bold'))
    szin.grid(row=7,column=0,pady=2, padx=20)

    galeria_gombA = Button(informacioA, text="Galéria", bg="#285cfa", fg="white", font="sans 13 bold",  command=nyisdmegaronet)
    galeria_gombA.grid(row=8, column=0, pady=10, padx=30)
    
    # Bezáró gomb
    bezaro_gomb = Button(informacioA, text="Bezárás", bg="#ed735a", font="sans 20 bold", command=informacioA.destroy)
    bezaro_gomb.grid(row=9, column=0, pady=10, padx=30)
#egyik szín #285cfa
#masik szín #28e8fa
#gomb szín #ed735a