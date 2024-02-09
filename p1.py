import tkinter as tk


def take():
    
    value=entry.get() 
    label.config(text=value)

window = tk.Tk()
window.title("My first window")
window.geometry("500x300")  

label = tk.Label(window, text="¡Hello!", font=("Arial", 27))
label.place(x=200, y=100)

button = tk.Button(window, text="Click", command=take)
button.config(width=15, height=2, font=("Arial", 12),bg="black",fg="white")
button.place(x=190, y=200)

entry = tk.Entry(window, textvariable=tk.StringVar(), width=30)
entry.place(x=170, y=160)


window.mainloop()