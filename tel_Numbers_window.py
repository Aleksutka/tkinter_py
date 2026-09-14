import customtkinter as ctk
import keyboard as ky

app = ctk.CTk()
app.title("Telefona nummuru grāmatiņa")
app.geometry("420x520")
app.grid_columnconfigure(0, weight=1)
app.grid_columnconfigure(1, weight=1)
app.resizable(width=False, height=False)

def pievienot():
    txt.configure(text="Ievadiet lototāju!")
    inp.bind("<Return>", ievadiet_vardu)

def ievadiet_vardu(event):
    global name
    name = inp.get().strip()
    print(name)
    inp.delete(0, "end")
    txt.configure(text="Ievadiet telefona numuru!")
    inp.bind("<Return>", ievadiet_numuru)

def ievadiet_numuru(event):
    global number
    number = inp.get().strip()
    inp.delete(0, "end")
    try:
        with open(f"{name}.txt", "x") as f:
            f.write(number)
        txt.configure(text="Jūs pievienojāt jaunu litotāja nummuru")
    except FileExistsError:
        txt.configure(text="Tāds vārds jau eksistē!")


txt = ctk.CTkLabel(app, text="", font=("Arial", 20))
txt.grid(row=1, pady=20)

inp = ctk.CTkEntry(app, justify="center", placeholder_text="", width=200, height=35)
inp.grid(row=2, pady=20)

btnPie = ctk.CTkButton(app, text="Pievienot nummuru", command=pievienot, height=35, width=200)
btnPie.grid(row=3, column=0, padx=5, pady=5)

btnAtr = ctk.CTkButton(app, text="Atrast nummuru pēc vārda", height=35, width=200)
btnAtr.grid(row=3, column=1, padx=5, pady=5)

app.mainloop()