import tkinter as tk #import window libarary

root = tk.Tk() #make window
root.title("First window test") #window title
root.geometry("320x520") #window size

def on_button_click():
    textInWindow.config(text="button pressed!") #function that completes when button pressed

textInWindow = tk.Label(root, text="This is my app", pady=20)
textInWindow.pack() #put widget into the window

button = tk.Button(root, text="Click me", command=on_button_click) #make button with text "Click me", when you click completes caommand
button.pack()

root.mainloop() #start the app

# Entry - type text(input)
# Lable - for displaying text
# Button - for trigerring functions
# Frame - for organising other widgets into groups ???

# .pack() - stacks items on top of each other
# .grid() - place items in rows and columns