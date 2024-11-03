from tkinter import *
from PIL import Image, ImageTk

# Áron galéria ablak megnyitása
def arongaleria():
    GalériaÁRON = Toplevel()  # Toplevel ablak
    GalériaÁRON.geometry("680x760")
    GalériaÁRON.title("Áron képei")
    GalériaÁRON.configure(bg="black")

    #A Képek elérési útvonala
    kepek = [
        r"negyedik.png",
        r"otodik.jpeg",
        r"hatodik.jpg"
    ]
    
    global index, img  
    index = 0

    #Képek betöltése és megjelenítése
    def load_image():
        global index, img  
        img = Image.open(kepek[index])
        img = img.resize((500, 500), Image.LANCZOS)
        img = ImageTk.PhotoImage(img)
        img_label.config(image=img)
        img_label.image = img

    #Lépés a következő képre
    def next_image():
        global index
        index = (index + 1) % len(kepek)
        load_image()
    #Lépés az előző képre
    def prev_image():
        global index
        index = (index - 1) % len(kepek)
        load_image()

    # Kép megjelenítése
    img_label = Label(GalériaÁRON, bg="black")
    img_label.grid(row=1, column=0, columnspan=3, padx=50, pady=10)
    
    #Első kép betöltése
    load_image()  
    emoji = Label(GalériaÁRON, text="Áron képei", bg="black", fg="#28e8fa", font=('Comic Sans', 30, 'bold'))
    emoji.grid(row=0, column=1, pady=5, padx=90)

    # Navigációs gombok létrehozása és elhelyezése a grid segítségével

    #Lépés az előző képre
    prev_button = Button(GalériaÁRON, text="<==", bg="#28e8fa", font="Times 20 bold", borderwidth=10, command=prev_image)
    prev_button.grid(row=2, column=0, padx=20, pady=10)
    
    #Lépés a következő képre
    next_button = Button(GalériaÁRON, text="==>", bg="#28e8fa", font="Times 20 bold", borderwidth=10, command=next_image)
    next_button.grid(row=2, column=2, padx=20, pady=10)
    
    #bezáró gomb
    bezaro_gomb = Button(GalériaÁRON, text="Bezárás", bg="#ed735a", font="sans 23 bold", command=GalériaÁRON.destroy).grid(row=3, column=1,pady=5,padx=20)
