from tkinter import Tk, Label, Entry, Button

def ablakja():
    ARON_ablak = Tk()
    ARON_ablak.geometry("700x900")
    ARON_ablak.configure(bg="black")
    ARON_ablak.title("ÁRON VAGYOK")
    ARON_cím = Label(ARON_ablak, text="ÁRON profilja🎁", fg="black", bg="#00FF9C", font=('Times', 50, 'bold'))
    ARON_cím.grid(row=0, columnspan=1, pady=10, padx=120)

    ARON_chatfal = Label(ARON_ablak, text="Írja ide az üzenetét", bg="black", fg="red", font=('Helvetica', 15, 'bold'))
    ARON_chatfal.grid(row=3, pady=10, padx=(0,550))
    ARON_ide_irjon = Entry(ARON_ablak, width=20, bg="#00FF9C")
    ARON_ide_irjon.grid(row=4, pady=0, padx=(0,560))

    def megnyomva():
        üzenet = ARON_ide_irjon.get()
        elküldve = Label(ARON_ablak, text="Elküldve", bg="black", fg="red", font=('Times', 10, 'bold'))
        elküldve.grid(row=5, pady=10, padx=(0,550))
        
        def eltavolit():
            elküldve.destroy()
        
        ARON_ablak.after(2000, eltavolit)
        
        try:
            with open("üzenetek.txt", 'a', encoding="utf-8") as fajl:
                fajl.write(üzenet + "; ÁRON\n")
        except Exception as e:
            print('Nem találjuk az adatokat', e)
        
        ARON_ide_irjon.delete(0, 'end')
        beszelgetni()
        iras()
    
    def beszelgetni():
        global kiüzent
        kiüzent = []
        
        try:
            with open("üzenetek.txt", 'r', encoding="utf-8") as fajl:
                for sor in fajl:
                    adat = sor.strip().split(';')
                    if len(adat) == 2:
                        kiüzent.append({
                            'Üzenet': adat[0],
                            'Kiküldte': adat[1]
                        })
        except FileNotFoundError:
            print("Az üzenetek.txt fájl nem található.")

    def iras():
        sorkoz = 6  
        for widget in ARON_ablak.grid_slaves():
            if int(widget.grid_info()["row"]) >= 6:
                widget.grid_forget()
        
        for i in kiüzent:
            if i['Kiküldte'] == "ÁRON":
                uzenetlabel = Label(ARON_ablak, text=i['Üzenet'], font="Times 20", fg="white", bg="#00FF9C")
                uzenetlabel.grid(row=sorkoz, column=0, pady=5, padx=(10, 0))
            else:
                uzenetlabel = Label(ARON_ablak, text=i['Üzenet'], font="Times 20", fg="red", bg="#656966")
                uzenetlabel.grid(row=sorkoz, column=1, pady=5, padx=(450, 0))
            sorkoz += 1

    bekuldesgomb = Button(ARON_ablak, text="=>", bg="#00FF9C", font="Times 8", borderwidth=3, command=megnyomva)
    bekuldesgomb.grid(row=4, pady=0, padx=(0,440))

    beszelgetni()
    iras()
    
    ARON_ablak.mainloop()

ablakja()
    