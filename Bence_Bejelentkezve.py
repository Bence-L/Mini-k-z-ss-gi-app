from tkinter import *

def alkalmazás():
    siker_ablak = Tk()
    siker_ablak.geometry("700x500")
    siker_ablak.configure(bg="black")
    siker_ablak.title("Siker")
    siker_cím = Label(siker_ablak, text="Bence profilja🕸", bg="black", fg="#00FF9C", font=('Times', 50, 'bold'))
    siker_cím.grid(row=0, columnspan=1, pady=10, padx=150)

    # abelepes_sikeres = Label(siker_ablak, text="A belépés sikeres volt", bg="black", fg="red", font=('Helvetica', 10, 'bold'))
    # abelepes_sikeres.grid(row=2, columnspan=1,pady=20, padx=(220,360))
    # ertettem_gomb = Button(siker_ablak, text="Értettem!", fg="red",bg="black", font="sans 10 bold", command=abelepes_sikeres.destroy)
    # ertettem_gomb.grid(row=2, columnspan=2, pady=3, padx=5)
    
    #írás
    chatfal = Label(siker_ablak, text="Írjon ide valamit:", bg="black", fg="red", font=('Helvetica', 15, 'bold'))
    chatfal.grid(row=3, pady=10, padx=50)
    ide_irjon = Entry(siker_ablak, width=20, bg="#00FF9C")
    ide_irjon.grid(row=3, columnspan=1, pady=10, padx=2)
    #kilépés
    vissza_fooldalra = Button(siker_ablak, text="Vissza a főoldalra", bg="red", font="sans 23 bold", command=siker_ablak.destroy)
    vissza_fooldalra.grid(row=4, columnspan=1,pady=15,padx=20)
    


    siker_ablak.mainloop()