from tkinter import *


def benceinfo():
    informacioB = Tk()
    informacioB.geometry("700x500")
    informacioB.title("Bence-Infor")
    informacioB.configure(bg="black")
    
    kie = Label(informacioB, text="Bence", bg="black", fg="#28e8fa", font=('Comic Sans', 50, 'bold'))
    kie.grid(row=1, columnspan=3, pady=(6, 0), padx=120)

    info = Label(informacioB, text="információi", bg="black", fg="#28e8fa", font=('Comic Sans', 20, 'bold'))
    info.grid(row=2, columnspan=3, pady=(15, 20), padx=110)
    
    # Bezáró gomb
    bezaro_gomb = Button(informacioB, text="Bezárás", bg="#ed735a", font="sans 13 bold", command=informacioB.destroy)
    bezaro_gomb.grid(row=8, column=1, pady=10, padx=20)

#egyik szín #285cfa
#masik szín #28e8fa
#gomb szín #ed735a