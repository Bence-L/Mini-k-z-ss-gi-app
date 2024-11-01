from tkinter import Tk, Label, Entry, Button, Canvas, Scrollbar, Frame, VERTICAL

def aron_ablak():
    def megnyomva():
        uzenet = ide_irjon.get()
        elkuldve = Label(aron_ablak, text="Elküldve", bg="black", fg="#ed735a", font=('Times', 10, 'bold'))
        elkuldve.grid(row=4, column=1, pady=10, padx=(0, 300))
        
        def eltavolit():
            elkuldve.destroy()
        
        aron_ablak.after(2000, eltavolit)
        
        try:
            with open("uzenetek.txt", 'a', encoding="utf-8") as fajl:
                fajl.write(uzenet + "; ÁRON\n")
        except Exception as e:
            print('Nem találjuk az adatokat', e)
        
        ide_irjon.delete(0, 'end')
        beszelgetni()
        iras()
    
    def beszelgetni():
        global kiuzent
        kiuzent = []
        
        try:
            with open("uzenetek.txt", 'r', encoding="utf-8") as fajl:
                for sor in fajl:
                    adat = sor.strip().split(';')
                    if len(adat) == 2:
                        kiuzent.append({
                            'Üzenet': adat[0],
                            'Kiküldte': adat[1]
                        })
        except FileNotFoundError:
            print("Az uzenetek.txt fájl nem található.")

    def iras():
        for widget in message_frame.winfo_children():
            widget.destroy()
        
        sorkoz = 0  
        for i in kiuzent:
            if i['Kiküldte'].strip() == "ÁRON":  # Áron üzenete
                uzenetlabel = Label(message_frame, text=f"Én: {i['Üzenet']}", font="Times 20", fg="black", bg="#28e8fa")
                uzenetlabel.grid(row=sorkoz, column=1, pady=5, padx=(150,0), sticky='e')
            else:  # Bence üzenete
                uzenetlabel = Label(message_frame, text=f"Bence: {i['Üzenet']}", font="Times 20", fg="black", bg="#285cfa")
                uzenetlabel.grid(row=sorkoz, column=0, pady=5, padx=(10,100), sticky='w')
            sorkoz += 1
        canvas.update_idletasks()
        canvas.yview_moveto(1.0)

    aron_ablak = Tk()
    aron_ablak.geometry("900x700")
    aron_ablak.configure(bg="black")
    aron_ablak.title("Áron profilja")
    aron_cim = Label(aron_ablak, text="Áron profilja🎁", fg="#28e8fa", bg="black", font=('Times', 30, 'bold'))
    aron_cim.grid(row=0, columnspan=2, pady=10, padx=40)

    canvas = Canvas(aron_ablak, bg="black")
    canvas.grid(row=1, column=0, columnspan=2, sticky='nsew')

    scrollbar = Scrollbar(aron_ablak, orient=VERTICAL, command=canvas.yview)
    scrollbar.grid(row=1, column=2, sticky='ns')

    canvas.configure(yscrollcommand=scrollbar.set)

    message_frame = Frame(canvas, bg="black")
    canvas.create_window((0, 0), window=message_frame, anchor='nw')

    message_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    chatfal = Label(aron_ablak, text="Írja ide az üzenetét:", bg="black", fg="#28e8fa", font=('Helvetica', 12, 'bold'))
    chatfal.grid(row=2, columnspan=2, pady=10, padx=40)
    ide_irjon = Entry(aron_ablak, width=20, bg="#285cfa")
    ide_irjon.grid(row=3, columnspan=2, pady=10, padx=40)

    bekuldesgomb = Button(aron_ablak, text="=>", bg="#285cfa", font="Times 8", borderwidth=3, command=megnyomva)
    bekuldesgomb.grid(row=3, columnspan=2, pady=10, padx=(170,10))

    aron_ablak.grid_rowconfigure(1, weight=1)
    aron_ablak.grid_columnconfigure(0, weight=1)

    beszelgetni()
    iras()
    
    aron_ablak.mainloop()

