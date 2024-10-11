from tkinter import *



def bencefuggveny():
    master = Tk()
    master.geometry("1000x800")
    master.title("Bence profilja")
    master.configure(bg="black")
    cím_bence = Label(master,text="Bejelentkezés",bg="#00FF9C", font=('Comic Sans', 60, 'bold'))
    cím_bence.grid(row= 0, columnspan=3, pady=10, padx=5)
    neve_bence = Label(master,text="Bence profiljába",bg="#00FF9C", font=('Comic Sans', 30, 'bold'))
    neve_bence.grid(row= 1, columnspan=3, pady=10, padx=5)

# Event loop létrehozása