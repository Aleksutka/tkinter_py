import customtkinter as ctk
import os

app = ctk.CTk()
app.title("Telefona nummuru grāmatiņa")
app.geometry("370x420")
app.grid_columnconfigure(0, weight=1)
app.grid_columnconfigure(1, weight=1)
app.resizable(width=False, height=False)

folder_path = "Kontakti"

os.makedirs(folder_path, exist_ok=True)

def pievienot():
    global tagad
    tagad = "name"
    txt.configure(text="Ievadiet lototāju!")
    buttApst.grid(row=2, column=1)
    
def atrast():
    global tagad
    tagad = "atrast"
    txt.configure(text="Ievadiet vārdu!")
    buttApst.grid(row=2, column=1)
    
def izdzest():
    global tagad
    tagad = "izdzest"
    txt.configure(text="Ievadiet vārdu kuru izdzēst!")
    buttApst.grid(row=2, column=1)

def visi():
    for file in os.listdir(folder_path):
            name, ext = os.path.splitext(file)
            print("-", name)
    print()
        
def turp():
    global tagad, name, number, file_path
    if tagad == "name":
        name = inp.get().strip().lower()
        inp.delete(0, "end")
        txt.configure(text="Ievadiet telefona numuru!")
        tagad = "number"
    elif tagad == "number":
        number = inp.get().strip().lower()
        inp.delete(0, "end")
        try:
            file_path = os.path.join(folder_path, f"{name}.txt")
            with open(file_path, "x") as f:
                f.write(number)
            txt.configure(text="Jūs pievienojāt jaunu litotāja nummuru")
        except FileExistsError:
            txt.configure(text="Tāds vārds jau eksistē!")
        tagad = "name"
        buttApst.grid_remove()
    elif tagad == "atrast":
        try:
            name = inp.get().strip().lower()
            inp.delete(0, "end")
            file_path = os.path.join(folder_path, f"{name}.txt")
            with open(file_path) as f:
                txt.configure(text=f.read())
            buttApst.grid_remove()
        except:
            txt.configure(text="Notika kaut kāda kļūda!")
    elif tagad == "izdzest":
        try:
            name = inp.get().strip().lower()
            inp.delete(0, "end")
            file_path = os.path.join(folder_path, f"{name}.txt")
            if os.path.exists(file_path):
                txt.configure(text=f"Tiešām izdēst kontaktu: {name}?")
                tagad = "yes"
            else:
                txt.configure(text="Fails neeksistē!")
                buttApst.grid_remove()
        except:
            txt.configure(text="Kaut kas sagāja greizi!")
            buttApst.grid_remove()
    elif tagad == "yes":
        os.remove(file_path)
        txt.configure(text="Kontakts tika izdzēsts!")

txt = ctk.CTkLabel(app, text="", font=("Arial", 20))
txt.grid(row=1, pady=20)

buttApst = ctk.CTkButton(app, text="Apstiprināt", command=turp, width=80, height=35)
buttApst.grid_remove()

inp = ctk.CTkEntry(app, justify="center", placeholder_text="", width=200, height=35)
inp.grid(row=2, pady=20, column=0)

btnPie = ctk.CTkButton(app, text="Pievienot nummuru", command=pievienot, height=35, width=200)
btnPie.grid(row=3, padx=5, pady=5)

btnAtr = ctk.CTkButton(app, text="Atrast nummuru pēc vārda", command=atrast, height=35, width=200)
btnAtr.grid(row=4, padx=5, pady=5)

btnIzdz = ctk.CTkButton(app, text="Izdzēst kontaktu", command=izdzest, height=35, width=200)
btnIzdz.grid(row=5, column=0, pady=5)

btnVisi = ctk.CTkButton(app, text="Visi kontakti", command=visi, height=35, width=200)
btnVisi.grid(row=6, column=0, pady=5)

app.mainloop()