import tkinter as tk

def check(check1,check2,option, label_result):
    
    label_result.config(text=f'Radiobuttons: {option.get()} - Checks: {check1.get()}, {check2.get()}')

window = tk.Tk()
window.title("My first window")
window.geometry("500x700")  # Tamaño de la ventana





check1=tk.IntVar()
check2=tk.IntVar()
checkbutton = tk.Checkbutton(window, text="Check 1",variable=check1)
checkbutton.place(x=200, y=300)
checkbutton2 = tk.Checkbutton(window, text="Check 2",variable=check2)
checkbutton2.place(x=200, y=350)
option=tk.StringVar()
radiobutton = tk.Radiobutton(window, text="option 1", variable=option, value ='option 1')
radiobutton.place(x=200, y=400)
radiobutton = tk.Radiobutton(window, text="option 2", variable=option, value ='option 2')
radiobutton.place(x=200, y=450)

button = tk.Button(window, text="Click", command=lambda: check(check1,check2,option, label_result))
button.config(width=15, height=2, font=("Arial", 12),bg="black",fg="white")
button.place(x=330, y=400)
label_result = tk.Label(window, text="",font=("bold"))
label_result.place(x=100, y=100)




window.mainloop()