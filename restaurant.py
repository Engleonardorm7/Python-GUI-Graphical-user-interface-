import tkinter as tk

def check():
    value=option.get()
    if value == '1':
        
        vegetarian=tk.Toplevel()
        vegetarian.title('Vegetarian')
        vegetarian.geometry("800x500")
        
        label3 = tk.Label(vegetarian, text="Welcome to the Vegetarian menu!", font=("Arial", 27))
        label3.place(x=200, y=70)
        label4 = tk.Label(vegetarian, text="Select your order", font=("Arial", 18))
        label4.place(x=250, y=150)

        mediterranean_var = tk.IntVar()
        lentils_var = tk.IntVar()

        Mediterranean = tk.Checkbutton(vegetarian, text="Mediterranean salad          $25000", variable=mediterranean_var)
        Mediterranean.place(x=250, y=250)

        Lentils = tk.Checkbutton(vegetarian, text="Lentils Bolognese              $35000", variable=lentils_var)
        Lentils.place(x=250, y=270)
        
        label4 = tk.Label(vegetarian, text="Quantity",font=("bold"))
        label4.place(x=250, y=300)

        quantity_var = tk.IntVar()

        entry2=tk.Entry(vegetarian,textvariable=quantity_var, width=30)
        entry2.place(x=350, y=305)
    
        

        label_result = tk.Label(vegetarian, text="",font=("bold"))
        label_result.place(x=400, y=350)

        
        button2 = tk.Button(vegetarian, text="Prepare my order", command=lambda: price(mediterranean_var, lentils_var, quantity_var, label_result))
        button2.config(width=15, height=2, font=("Arial", 12),bg="black",fg="white")
        button2.place(x=330, y=400)



    if value=='3':
        vegetarian=tk.Toplevel()
        vegetarian.title('Non vegetarian')
        vegetarian.geometry("800x500")

def price(mediterranean_var, lentils_var, quantity_var, label_result):
    mediterranean_price = 25000
    lentils_price = 35000
    quantity = int(quantity_var.get())
    mediterranean_var=mediterranean_var.get()
    lentils_var=lentils_var.get()
    
    total_price = (mediterranean_var * mediterranean_price + lentils_var * lentils_price) * quantity

    label_result.config(text=f"Total Price $ {total_price}")

window = tk.Tk()
window.title("My Restaurant")
window.geometry("800x500")  # Tamaño de la ventana
window.configure(bg="lightblue")

label = tk.Label(window, text="Welcome to my restaurant!", font=("Arial", 27),bg="lightblue")
label.place(x=200, y=70)
label2 = tk.Label(window, text="Which menu do you prefer?", font=("Arial", 18),bg="lightblue")
label2.place(x=250, y=150)

option=tk.StringVar()
radiobutton = tk.Radiobutton(window, text="Vegetarian", variable=option, value=1,bg="lightblue")
radiobutton.place(x=250, y=250)

radiobutton2 = tk.Radiobutton(window, text="Non vegetarian", variable=option, value =3, bg="lightblue")
radiobutton2.place(x=450, y=250)

button = tk.Button(window, text="Click", command=check)
button.config(width=15, height=2, font=("Arial", 12),bg="black",fg="white")
button.place(x=330, y=350)










window.mainloop()