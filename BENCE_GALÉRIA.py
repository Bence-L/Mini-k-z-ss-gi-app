from tkinter import *
from tkinter import ttk

# A galéria ablak megnyitása
def bencegaleria():
    GalériaB = Toplevel()  # Toplevel ablak
    GalériaB.geometry("680x760")
    GalériaB.title("Bence képei")
    GalériaB.configure(bg="black")

    # A képek elérési útvonala
    kepek = [
        r"elsokep.png",
        r"masodikkep.png",
        r"harmadikkep.png",
        r"hetedik.png",
        r"nyolcadik.png"
    ]
    
    global index, img_list, img_label, textOfStatusbar
    index = 0

    # Képek betöltése
    img_list = [PhotoImage(file=kep) for kep in kepek]

    
    

    
    # Kép megjelenítésére szolgáló címke létrehozása
    img_label = Label(GalériaB, bg="black")
    img_label.grid(row=1, column=0, columnspan=3, padx=50, pady=10)
    
    # Kép betöltése és megjelenítése
    def load_image():
        img_label.config(image=img_list[index])

    # Lépés a következő képre
    def next_image():
        global index
        index = (index + 1) % len(img_list)
        load_image()
        

    # Lépés az előző képre
    def prev_image():
        global index
        index = (index - 1) % len(img_list)
        load_image()
        

    # Első kép betöltése
    load_image()

    emoji = Label(GalériaB, text="Bence képei", bg="black", fg="#28e8fa", font=('Comic Sans', 30, 'bold'))
    emoji.grid(row=0, column=1, pady=5, padx=90)

    # Navigációs gombok létrehozása és elhelyezése a grid segítségével
    prev_button = Button(GalériaB, text="<==", bg="#28e8fa", font="Times 20 bold", borderwidth=10, command=prev_image)
    prev_button.grid(row=2, column=0, padx=20, pady=10)
    
    next_button = Button(GalériaB, text="==>", bg="#28e8fa", font="Times 20 bold", borderwidth=10, command=next_image)
    next_button.grid(row=2, column=2, padx=20, pady=10)

    # Bezáró gomb
    bezaro_gomb = Button(GalériaB, text="Bezárás", bg="#ed735a", font="sans 23 bold", command=GalériaB.destroy)
    bezaro_gomb.grid(row=3, column=1, pady=5, padx=20)