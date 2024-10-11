from tkinter import *
# Root -> a fő widget (a fő ablak)



# sets the geometry and the title of the main root window

def aronfuggveny():
    master = Tk()
    master.geometry("1000x800")
    master.title("Áron profilja")
    master.configure(bg="black")
    cím_áron = Label(master,text="Bejelentkezés",bg="#00FF9C", font=('Comic Sans', 60, 'bold'))
    cím_áron.grid(row= 0, columnspan=3, pady=10, padx=5)
    neve_áron = Label(master,text="Áron profiljába",bg="#00FF9C", font=('Comic Sans', 30, 'bold'))
    neve_áron.grid(row= 1, columnspan=3, pady=10, padx=5)
    jelszo_aron=Label(master,text="Írja be a jelszóját: ",fg="red",bg="black", font=('Comic Sans', 10, 'bold'))
    jelszo_aron.grid(row= 2, columnspan=3, pady=10, padx=5)
    e = Entry(master, width=20, bg="#00FF9C", borderwidth=2)
    e.grid(row= 3, columnspan=3, pady=10, padx=5)
    

# Event loop létrehozása