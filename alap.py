from tkinter import *
import Áron_Profilja
import Bence_Profilja
import Bence_információi
import Áron_információi

master = Tk()
master.geometry("1000x800")
master.title("Főoldal")
master.configure(bg="black")

#Gombok funkciói
#Áron bejelentkező ablakát nyitja meg
def openNewWindow():
    Áron_Profilja.aronfuggveny()
#Bence bejelentkező ablakát nyitja meg 
def openNewWindow2():
    Bence_Profilja.bencefuggveny()
#Bence információs ablakát nyitja meg
def info1():
    Bence_információi.benceinfo()
#Áron információs ablakát nyitja meg
def info2():
    Áron_információi.aroninfo()

#Emoji + ismertető szövegek
ábra= Label(master, text="📞", fg="#28e8fa", bg="black",font=('Times', 80, 'bold'))
ábra.grid(row= 0, columnspan=3,pady=(10,0), padx=320)

cím = Label(master, text="ChatRing™", fg="#28e8fa",bg="black",font=('Times', 60,'bold'))
cím.grid(row= 1, columnspan=3,pady=(1,0), padx=320)

label = Label(master, text ="Válasszon egy profilt!",bg="black", fg="#28e8fa" ,font="sans 16 bold").grid(row= 2, columnspan=3, pady=(10,40), padx=5)
#Gombok, profil választás, és információk
aron_valaszt = Button(master, text ="Áron", bg="#28e8fa", font="Times 30 bold",  borderwidth=20,command = openNewWindow).grid(row= 4, column=0, pady=10,padx=(25, 25))
bence_valaszt = Button(master, text ="Bence", bg="#28e8fa", font="Times 30 bold",  borderwidth=20, command = openNewWindow2).grid(row= 4, column=2, pady=10,padx=(25, 25))
info_aron = Button(master, text ="Info-Áron", bg="#28e8fa", font="Times 20 bold",  borderwidth=10,command = info2).grid(row= 5, column=0, pady=10,padx=(25, 25))
info_bence = Button(master, text ="Info-Bence", bg="#28e8fa", font="Times 20 bold",  borderwidth=10,command = info1).grid(row= 5, column=2, pady=10,padx=(25, 25))
bence_emoji = Label(master, text="🏆", bg="black",fg="#28e8fa",font=('Times', 35))
bence_emoji.grid(row= 3, column=2, pady=5,padx=(25, 25))
aron_emoji = Label(master, text="⚽", bg="black",fg="#28e8fa",font=('Times', 35))
aron_emoji.grid(row= 3, pady=5,padx=(25, 25))
#Bezáró button
bezaro_gomb = Button(master, text="Bezárás", bg="#ed735a", font="sans 23 bold", command=master.destroy).grid(row=6, column=1,pady=75,padx=20)

mainloop()
