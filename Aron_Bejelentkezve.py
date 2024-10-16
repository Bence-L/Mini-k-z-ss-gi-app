from tkinter import *

def ablakja():
    ARON_ablak = Tk()
    ARON_ablak.geometry("700x500")
    ARON_ablak.configure(bg="black")
    ARON_ablak.title("ÁRON VAGYOK")
    ARON_cím = Label(ARON_ablak, text="ÁRON profilja🎁", fg="black", bg="#00FF9C", font=('Times', 50, 'bold'))
    ARON_cím.grid(row=0, columnspan=1, pady=10, padx=120)

    # abelepes_sikeres = Label(siker_ablak, text="A belépés sikeres volt", bg="black", fg="red", font=('Helvetica', 10, 'bold'))
    # abelepes_sikeres.grid(row=2, columnspan=1,pady=20, padx=(220,360))
    # ertettem_gomb = Button(siker_ablak, text="Értettem!", fg="red",bg="black", font="sans 10 bold", command=abelepes_sikeres.destroy)
    # ertettem_gomb.grid(row=2, columnspan=2, pady=3, padx=5)
    
    #írás
    ARON_chatfal = Label(ARON_ablak, text="Írja ide az üzenetét", bg="black", fg="red", font=('Helvetica', 15, 'bold'))
    ARON_chatfal.grid(row=3, pady=10, padx=(0,550))
    ARON_ide_irjon = Entry(ARON_ablak, width=20, bg="#00FF9C")
    ARON_ide_irjon.grid(row=4, pady=0, padx=(0,560))

    def megnyomva():
        ARON_üzenetek = ARON_ide_irjon.get()
        ARON_elküldve = Label(ARON_ablak, text="Elküldve", bg="black", fg="red", font=('Times', 10, 'bold'))
        ARON_elküldve.grid(row=5, pady=10, padx=(0,550))
        def eltavolit():
            ARON_elküldve.destroy()
        ARON_ablak.after(2000, eltavolit)
        try:
            with open("üzenetek.txt", 'a', encoding="utf-8") as fajl:
                    üzenetek = ARON_ide_irjon.get()
                    print(üzenetek+"; ÁRON", sep='\n', file=fajl)
        except:
            print('Nem találjuk az adatokat')
        
    ARON_bekuldesgomb = Button(ARON_ablak, text ="=>", bg="#00FF9C", font="Times 8",  borderwidth=3, command=megnyomva).grid(row=4, pady=0, padx=(0,400))
    
    def beszelgetni():
        kiüzent = []
        with open("üzenetek.txt", 'r', encoding="utf-8") as fajl: #encodinggal fur betűk lettek!!!!!!!!!!!
                    for sor in fajl:
                        adat = sor.strip().split(';')
                        kiüzent.append({
                        'Üzenet' : adat[0],
                        'Kiküldte' : adat[1]
                })
        print(kiüzent)
                
    beszelgetni()
            
                          
    
    #kilépés
    vissza_fooldalra = Button(ARON_ablak, text="Vissza a főoldalra", bg="red", font="sans 10 bold", command=ARON_ablak.destroy)
    vissza_fooldalra.grid(row=8, columnspan=1,pady=15,padx=20)
    