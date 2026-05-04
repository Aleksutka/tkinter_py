import customtkinter as ctk

def terminal_output():
    written = inp.get()
    textInWindow.configure(text=f"You wrote: {written}")

app = ctk.CTk()
app.title("cudtomTkinter App")
app.geometry("320x520")


textInWindow = ctk.CTkLabel(app, text="Result will be here")
textInWindow.grid(row=0, pady=(10, 20), padx=20)

title = ctk.CTkLabel(app, text="Write something down:")
title.grid(row=1, pady=(10, 10), padx=20)

inp = ctk.CTkEntry(app, placeholder_text="Write here", width=200)
inp.grid(row=2, pady=(10, 10), padx=20)

btn = ctk.CTkButton(app, text="Click here to appear your writtentext", command=terminal_output)
btn.grid(row=3, padx=20)

app.mainloop()