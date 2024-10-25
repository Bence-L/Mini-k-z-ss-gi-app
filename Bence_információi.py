from tkinter import *


def benceinfo():
    informacioB = Tk()
    informacioB.geometry("480x700")
    informacioB.title("Bence-Információ")
    informacioB.configure(bg="black")
    
    emoji = Label(informacioB, text="📜", bg="black", fg="#28e8fa", font=('Comic Sans', 50, 'bold'))
    emoji.grid(row=0, column=0, pady=5, padx=30)

    kie = Label(informacioB, text="Léber Bence", bg="black", fg="#28e8fa", font=('Comic Sans', 50, 'bold'))
    kie.grid(row=1, column=0, pady=5, padx=30)

    info = Label(informacioB, text="Információi", bg="black", fg="#28e8fa", font=('Comic Sans', 30, 'bold'))
    info.grid(row=2, column=0, pady=5, padx=30)
    
    adatok = Label(informacioB, text="Adatok", bg="black", fg="#28e8fa", font=('Comic Sans', 20, 'bold'))
    adatok.grid(row=3,column=0,pady=(50,10), padx=(0,200))

    nev_adatok = Label(informacioB, text="Neve: Léber Bence Bendegúz", bg="black", fg="#28e8fa", font=('Comic Sans', 12, 'bold'))
    nev_adatok.grid(row=4,column=0,pady=2, padx=20)

    szuletesi_adatok = Label(informacioB, text="Született: 2008.01.18.", bg="black", fg="#28e8fa", font=('Comic Sans', 12, 'bold'))
    szuletesi_adatok.grid(row=5,column=0,pady=2, padx=20)

    sport = Label(informacioB, text="Sport: Foci⚽", bg="black", fg="#28e8fa", font=('Comic Sans', 12, 'bold'))
    sport.grid(row=6,column=0,pady=2, padx=20)

    szin = Label(informacioB, text="Szín: Narancs🏀", bg="black", fg="orange", font=('Comic Sans', 12, 'bold'))
    szin.grid(row=7,column=0,pady=2, padx=20)

    # Bezáró gomb
    bezaro_gomb = Button(informacioB, text="Bezárás", bg="#ed735a", font="sans 13 bold", command=informacioB.destroy)
    bezaro_gomb.grid(row=8, column=0, pady=10, padx=30)

#egyik szín #285cfa
#masik szín #28e8fa
#gomb szín #ed735a