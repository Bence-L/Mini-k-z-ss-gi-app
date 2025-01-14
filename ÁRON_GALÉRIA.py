from tkinter import *

# Áron galéria ablak megnyitása
def arongaleria():
    GalériaÁRON = Toplevel()  # Toplevel ablak
    GalériaÁRON.geometry("680x760")
    GalériaÁRON.title("Áron képei")
    GalériaÁRON.configure(bg="black")

    # A képek elérési útvonala
    kepek = [
        r"negyedik.png",
        r"otodik.png",
        r"hatodik.png"
    ]
    
    global index, img_list, img_label
    index = 0

    # Képek betöltése
    img_list = [PhotoImage(file=kep) for kep in kepek]

    # Kép megjelenítésére szolgáló címke létrehozása
    img_label = Label(GalériaÁRON, bg="black", width=500, height=500)  # Kép keret méretezése
    img_label.grid(row=1, column=0, columnspan=3, padx=50, pady=10)

    # Kép betöltése és megjelenítése
    def load_image():
        img = img_list[index]
        # Kép beállítása
        img_label.config(image=img)
        img_label.image = img  # Referencia megőrzése

        # Kép méretének beállítása
        img_label.config(width=500, height=500)  # Egységes méret

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

    emoji = Label(GalériaÁRON, text="Áron képei", bg="black", fg="#28e8fa", font=('Comic Sans', 30, 'bold'))
    emoji.grid(row=0, column=1, pady=5, padx=90)

    # Navigációs gombok létrehozása és elhelyezése a grid segítségével
    prev_button = Button(GalériaÁRON, text="<==", bg="#28e8fa", font="Times 20 bold", borderwidth=10, command=prev_image)
    prev_button.grid(row=2, column=0, padx=20, pady=10)
    
    next_button = Button(GalériaÁRON, text="==>", bg="#28e8fa", font="Times 20 bold", borderwidth=10, command=next_image)
    next_button.grid(row=2, column=2, padx=20, pady=10)

    # Bezáró gomb
    bezaro_gomb = Button(GalériaÁRON, text="Bezárás", bg="#ed735a", font="sans 23 bold", command=GalériaÁRON.destroy)
    bezaro_gomb.grid(row=3, column=1, pady=5, padx=20)