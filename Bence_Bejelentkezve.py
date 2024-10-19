from tkinter import Tk, Label, Entry, Button

def alkalmazás():
    siker_ablak = Tk()
    siker_ablak.geometry("700x900")
    siker_ablak.configure(bg="black")
    siker_ablak.title("Siker")
    siker_cím = Label(siker_ablak, text="Bence profilja🕸", fg="red", bg="black", font=('Times', 50, 'bold'))
    siker_cím.grid(row=0, columnspan=1, pady=10, padx=60)

    chatfal = Label(siker_ablak, text="Írja ide az üzenetét:", bg="black", fg="red", font=('Helvetica', 15, 'bold'))
    chatfal.grid(row=3, pady=10, padx=(0,550))
    ide_irjon = Entry(siker_ablak, width=20, bg="#00FF9C")
    ide_irjon.grid(row=4, pady=0, padx=(0,560))

    def megnyomva():
        üzenet = ide_irjon.get()
        elküldve = Label(siker_ablak, text="Elküldve", bg="black", fg="red", font=('Times', 10, 'bold'))
        elküldve.grid(row=5, pady=10, padx=(0,550))
        
        def eltavolit():
            elküldve.destroy()
        
        siker_ablak.after(2000, eltavolit)
        
        try:
            with open("üzenetek.txt", 'a', encoding="utf-8") as fajl:
                fajl.write(üzenet + "; BENCE\n")
        except Exception as e:
            print('Nem találjuk az adatokat', e)
        
        ide_irjon.delete(0, 'end')
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
        for widget in siker_ablak.grid_slaves():
            if int(widget.grid_info()["row"]) >= 6:
                widget.grid_forget()
        
        for i in kiüzent:
            if i['Kiküldte'] == "BENCE":
                uzenetlabel = Label(siker_ablak, text=i['Üzenet'], font="Times 20", fg="black", bg="#00FF9C")
                uzenetlabel.grid(row=sorkoz, column=1, pady=5, padx=(450, 0))
            else:
                uzenetlabel = Label(siker_ablak, text=i['Üzenet'], font="Times 20", fg="red", bg="#656966")
                uzenetlabel.grid(row=sorkoz, column=0, pady=5, padx=(10, 0))
            sorkoz += 1

    bekuldesgomb = Button(siker_ablak, text="=>", bg="#00FF9C", font="Times 8", borderwidth=3, command=megnyomva)
    bekuldesgomb.grid(row=4, pady=0, padx=(0,440))

    beszelgetni()
    iras()
    
    siker_ablak.mainloop()

alkalmazás()