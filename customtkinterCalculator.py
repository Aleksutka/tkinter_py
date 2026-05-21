import customtkinter as ctk

app = ctk.CTk()
app.title("Calculator")
app.geometry("320x520")
app.grid_columnconfigure(0, weight=1)
app.grid_columnconfigure(1, weight=1)
app.grid_columnconfigure(2, weight=1)
app.grid_columnconfigure(3, weight=1)

expression = ""

def add_to_expression(value):
    global expression
    expression += str(value)
    textInWindow.configure(text=expression)

def calculate():
    global expression
    try:
        result = eval(expression)
        textInWindow.configure(text=result)
    except:
        textInWindow.configure(text="Error")

def clear():
    global expression
    expression = ""
    textInWindow.configure(text="0")

textInWindow = ctk.CTkLabel(app, text="0", font=ctk.CTkFont(size=20, weight="bold"))
textInWindow.grid(row=0, column=3, columnspan=4, pady=(100, 10), sticky="nsew", padx=5)

btnC = ctk.CTkButton(app, text="C", command=clear)
btnC.grid(row=1, column=3, padx=5, pady=5, sticky="nsew")

btn7 = ctk.CTkButton(app, text="7", command=lambda: add_to_expression("7"))
btn7.grid(row=2, column=0, padx=5, pady=5, sticky="nsew")

btn8 = ctk.CTkButton(app, text="8", command=lambda: add_to_expression("8"))
btn8.grid(row=2, column=1, padx=5, pady=5, sticky="nsew")

btn9 = ctk.CTkButton(app, text="9", command=lambda: add_to_expression("9"))
btn9.grid(row=2, column=2, padx=5, pady=5, sticky="nsew")

btnDel = ctk.CTkButton(app, text="/", command=lambda: add_to_expression("/"))
btnDel.grid(row=2, column=3, padx=5, pady=5, sticky="nsew")

btn4 = ctk.CTkButton(app, text="4", command=lambda: add_to_expression("4"))
btn4.grid(row=3, column=0, padx=5, pady=5, sticky="nsew")

btn5 = ctk.CTkButton(app, text="5", command=lambda: add_to_expression("5"))
btn5.grid(row=3, column=1, padx=5, pady=5, sticky="nsew")

btn6 = ctk.CTkButton(app, text="6", command=lambda: add_to_expression("6"))
btn6.grid(row=3, column=2, padx=5, pady=5, sticky="nsew")

btnTime = ctk.CTkButton(app, text="*", command=lambda: add_to_expression("*"))
btnTime.grid(row=3, column=3, padx=5, pady=5, sticky="nsew")

btn1 = ctk.CTkButton(app, text="1", command=lambda: add_to_expression("1"))
btn1.grid(row=4, column=0, padx=5, pady=5, sticky="nsew")

btn2 = ctk.CTkButton(app, text="2", command=lambda: add_to_expression("2"))
btn2.grid(row=4, column=1, padx=5, pady=5, sticky="nsew")

btn3 = ctk.CTkButton(app, text="3", command=lambda: add_to_expression("3"))
btn3.grid(row=4, column=2, padx=5, pady=5, sticky="nsew")

btnMinus = ctk.CTkButton(app, text="-", command=lambda: add_to_expression("-"))
btnMinus.grid(row=4, column=3, padx=5, pady=5, sticky="nsew")

btn0 = ctk.CTkButton(app, text="0", command=lambda: add_to_expression("0"))
btn0.grid(row=5, column=0, padx=5, pady=5, sticky="nsew")

btnKom = ctk.CTkButton(app, text=".", command=lambda: add_to_expression("."))
btnKom.grid(row=5, column=1, padx=5, pady=5, sticky="nsew")

btn = ctk.CTkButton(app, text="=", command=calculate)
btn.grid(row=5, column=2, padx=5, pady=5, sticky="nsew")

btnPlus = ctk.CTkButton(app, text="+", command=lambda: add_to_expression("+"))
btnPlus.grid(row=5, column=3, padx=5, pady=5, sticky="nsew")

app.mainloop()