import customtkinter as ctk
import keyboard as ky

app = ctk.CTk()
app.title("Telefona nummuru grāmatiņa")
app.geometry("420x520")
app.grid_columnconfigure(0, weight=1)
app.resizable(width=False, height=False)

tagad = "name"

def pievienot():
    global tagad
    tagad = "name"
    txt.configure(text="Ievadiet lototāju!")
    inp.bind("<Return>", queue)

def queue(event):
    global tagad, name
    if tagad == "name":
        name = inp.get().strip()
        print(name)
        inp.delete(0, "end")
        txt.configure(text="Ievadiet telefona numuru!")
        tagad = "number"
    elif tagad == "number":
        number = inp.get().strip()
        inp.delete(0, "end")
        try:
            with open(f"{name}.txt", "x") as f:
                f.write(number)
            txt.configure(text="Jūs pievienojāt jaunu litotāja nummuru")
        except FileExistsError:
            txt.configure(text="Tāds vārds jau eksistē!")
        tagad = "name"

def atrast():
    txt.configure(text="Ievadiet vārdu!")
    inp.bind("<Return>", mekle)

def mekle(event):
    try:
        nameA = inp.get().strip()
        print(nameA)
        inp.delete(0, "end")
        with open(f"{nameA}.txt") as f:
            txt.configure(text=f.read())
    except FileNotFoundError:
        txt.configure(text="Tāda nav vēl kontakta!")
        


txt = ctk.CTkLabel(app, text="", font=("Arial", 20))
txt.grid(row=1, pady=20)

inp = ctk.CTkEntry(app, justify="center", placeholder_text="", width=200, height=35)
inp.grid(row=2, pady=20)

btnPie = ctk.CTkButton(app, text="Pievienot nummuru", command=pievienot, height=35, width=200)
btnPie.grid(row=3, padx=5, pady=5)

btnAtr = ctk.CTkButton(app, text="Atrast nummuru pēc vārda", command=atrast, height=35, width=200)
btnAtr.grid(row=4, padx=5, pady=5)

app.mainloop()