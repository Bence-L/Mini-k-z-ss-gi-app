from tkinter import *

def alkalmazás():
    siker_ablak = Tk()
    siker_ablak.geometry("700x500")
    siker_ablak.configure(bg="black")
    siker_ablak.title("Siker")
    siker_cím = Label(siker_ablak, text="SIKERÜLT", bg="black", fg="#00FF9C", font=('Comic Sans', 70, 'bold'))
    siker_cím.grid(row=0, columnspan=1, pady=10, padx=100)
    chatfal = Label(siker_ablak, text="Írjon ide valamit:", bg="black", fg="red", font=('Comic Sans', 15, 'bold'))
    chatfal.grid(row=1, pady=10, padx=(10,350))
    ide_irjon = Entry(siker_ablak, width=20, bg="#00FF9C")
    ide_irjon.grid(row=1, columnspan=1, pady=3, padx=5)
    vissza_fooldalra = Button(siker_ablak, text="Vissza a főoldalra", bg="red", font="sans 23 bold", command=siker_ablak.destroy)
    vissza_fooldalra.grid(row=2, columnspan=1,pady=15,padx=20)
    


    siker_ablak.mainloop()