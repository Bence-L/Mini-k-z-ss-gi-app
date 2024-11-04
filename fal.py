from tkinter import Tk, Label, Entry, Button, Canvas, Scrollbar, Frame, VERTICAL, Text, END, DISABLED

def falresz():
    fal_ablak = Tk()
    fal_ablak.geometry("1800x750")
    fal_ablak.configure(bg="black")
    fal_ablak.title("Fal")
    fal_cim = Label(fal_ablak, text="Fal🍔", fg="#fed766", bg="black", font=('Times', 70, 'bold'))
    fal_cim.grid(row=0, column=0, pady=10, padx=40)
    

    def fal_zolden():
        uzenet = fal_irjon.get()  # Az Entry mezőből vett üzenet szövege
        # Üzenet mentése a fájlba
        try:
            with open("faluzenetei.txt", 'a', encoding="utf-8") as fajl:
                fajl.write(uzenet + "; ZÖLD\n")
        except Exception as e:
            print('Nem találjuk az adatokat', e)
        
        fal_irjon.delete(0, 'end')  # Az Entry mező ürítése
        beszelgetni()  # Üzenetek frissítése
        iras()  # Üzenetek megjelenítése
    
    def fal_narancson():
        uzenet = fal_irjon.get()  # Az Entry mezőből vett üzenet szövege
        # Üzenet mentése a fájlba
        try:
            with open("faluzenetei.txt", 'a', encoding="utf-8") as fajl:
                fajl.write(uzenet + "; NARANCS\n")
        except Exception as e:
            print('Nem találjuk az adatokat', e)
        
        fal_irjon.delete(0, 'end')  # Az Entry mező ürítése
        beszelgetni()  # Üzenetek frissítése
        iras() 
    
    def fal_piroson():
        uzenet = fal_irjon.get()  # Az Entry mezőből vett üzenet szövege
        # Üzenet mentése a fájlba
        try:
            with open("faluzenetei.txt", 'a', encoding="utf-8") as fajl:
                fajl.write(uzenet + "; PIROS\n")
        except Exception as e:
            print('Nem találjuk az adatokat', e)
        
        fal_irjon.delete(0, 'end')  # Az Entry mező ürítése
        beszelgetni()  # Üzenetek frissítése
        iras() 
    # Üzenetek beolvasása a fájlból
    def beszelgetni():
        global kiuzent
        kiuzent = []
        
        try:
            with open("faluzenetei.txt", 'r', encoding="utf-8") as fajl:
                for sor in fajl:
                    adat = sor.strip().split(';')
                    if len(adat) == 2:
                        kiuzent.append({
                            'Üzenet': adat[0],
                            'Szin': adat[1]
                        })
        except FileNotFoundError:
            print("Az uzenetek.txt fájl nem található.")

    # Üzenetek megjelenítése a szövegmezőben
    def iras():
        for widget in message_frame.winfo_children():
            widget.destroy()  # Meglévő widgetek eltávolítása a message_frame-ből
        
        sorkoz = 0  
        for i in kiuzent:
            if i['Szin'].strip() == "ZÖLD":  # Bence üzenete
                uzenetlabel = Text(message_frame, wrap='word', font="Times 20", fg="black", bg="green", height=2, width=20)
                uzenetlabel.insert(END, i['Üzenet'])
                uzenetlabel.grid(row=sorkoz, pady=5, padx=(1300,10))
                uzenetlabel.config(state=DISABLED)
            if i['Szin'].strip() == "NARANCS":  # Bence üzenete
                uzenetlabel = Text(message_frame, wrap='word', font="Times 20", fg="black", bg="orange", height=2, width=20)
                uzenetlabel.insert(END, i['Üzenet'])
                uzenetlabel.grid(row=sorkoz, pady=5, padx=(10,1300))
                uzenetlabel.config(state=DISABLED)
            if i['Szin'].strip() == "PIROS": # Áron üzenete
                uzenetlabel = Text(message_frame, wrap='word', font="Times 20", fg="black", bg="red", height=2, width=20)
                uzenetlabel.insert(END, i['Üzenet'])
                uzenetlabel.grid(row=sorkoz, pady=5, padx=(10,10))
                uzenetlabel.config(state=DISABLED)
            sorkoz += 1
        
        # Görgetés beállítása az utolsó üzenetre
        canvas.update_idletasks()
        canvas.yview_moveto(1.0)



    # Canvas a görgethető tartalomhoz
    canvas = Canvas(fal_ablak, bg="#272727")
    canvas.grid(row=1, column=0, columnspan=2, sticky='nsew')

    # Függőleges görgetősáv hozzáadása a canvas-hoz
    scrollbar = Scrollbar(fal_ablak, orient=VERTICAL, command=canvas.yview)
    scrollbar.grid(row=1, column=2, sticky='ns')
    canvas.configure(yscrollcommand=scrollbar.set)
    
    # Frame a canvas tartalmához
    message_frame = Frame(canvas, bg="#272727")
    canvas.create_window((0, 0), window=message_frame, anchor='nw')
    
    # Dinamikus görgetési tartomány beállítása
    message_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    # Chat beviteli mező és címke
    chatfal = Label(fal_ablak, text="Írja ide az üzenetét:", bg="black", fg="#fed766", font=('Helvetica', 12, 'bold'))
    chatfal.grid(row=2, columnspan=2, pady=5, padx=40)
    fal_irjon = Entry(fal_ablak, width=20, bg="#fed766")
    fal_irjon.grid(row=3, columnspan=2, pady=(0,5), padx=40)
    fal_ablak.grid_rowconfigure(1, weight=1)
    fal_ablak.grid_columnconfigure(0, weight=1)
    
    fal_cim = Label(fal_ablak, text="Válassza ki milyen színű legyen az üzenet!\n🎨", fg="#FED766", bg="black", font=('Times', 20, 'bold'),width=3500)
    fal_cim.grid(row=4, column=0, pady=10, padx=40)

    zold_gomb = Button(fal_ablak, text="Zöld", bg="green", font="Times 25", borderwidth=8, command=fal_zolden)
    zold_gomb.grid(row=5, pady=10, padx=(245,10))
    narancs_gomb = Button(fal_ablak, text="Narancs", bg="orange", font="Times 25", borderwidth=8, command=fal_narancson)
    narancs_gomb.grid(row=5,  pady=10, padx=(10,300))
    piros_gomb = Button(fal_ablak, text="Piros", bg="red", font="Times 25", borderwidth=8, command=fal_piroson)
    piros_gomb.grid(row=5, pady=10, padx=(10,10))
    bezaro_gomb = Button(fal_ablak, text="Bezárás", bg="#ed735a", font="sans 23 bold", command=fal_ablak.destroy).grid(row=6,pady=10,padx=(10,10))
    fal_ablak.mainloop()
    

#falresz()