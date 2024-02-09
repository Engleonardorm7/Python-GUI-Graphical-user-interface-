import tkinter as tk


# def take():
#     label.config(text="¡Clic en el botón!")
#     value=entry.get()
#     # value =int(value)+10    
#     label.config(text=value)
# # Crear una ventana
window = tk.Tk()
window.title("My first window")
window.geometry("500x700")  # Tamaño de la ventana

# label = tk.Label(window, text='Hello')
label = tk.Label(window, text="¡Hello!", font=("Arial", 27))
label.place(x=200, y=100)
# label.pack()



button = tk.Button(window, text="Click")
button.config(width=15, height=2, font=("Arial", 12),bg="black",fg="white")
button.place(x=190, y=200)

checkbutton = tk.Checkbutton(window, text="Check me")
checkbutton.place(x=200, y=300)

radiobutton = tk.Radiobutton(window, text="Option 1")
radiobutton.place(x=200, y=400)
scale = tk.Scale(window, from_=0, to=100, orient=tk.HORIZONTAL)
scale.place(x=200, y=400)

# text = tk.Text(window)
# text.place(x=200, y=450)
scrollbar = tk.Scrollbar(window)

scrollbar.place(x=200, y=450)


# button = tk.Button(window, text="send", command=take)
# button.pack()

# # Mostrar la ventana

# # Crear una variable de control para almacenar el texto


# # Crear un Entry para que el usuario ingrese texto
entry = tk.Entry(window, textvariable=tk.StringVar(), width=30)
entry.place(x=170, y=160)


window.mainloop()