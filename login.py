import tkinter as tk



def second():
    window2 = tk.Toplevel()
    window2.title("Welcome")
    window2.geometry("500x300")  
    label_bienvenida = tk.Label(window2, text="Welcome!", font=("Arial", 18))
    label_bienvenida.pack(pady=50)

def take():
    
    user=entry_user.get() 
    password=entry_pass.get() 
    if user=='admin' and password == '12345':
        answer.config(text='Welcome!!!')
        # second()
    else:
        answer.config(text='Try again')

window = tk.Tk()
window.title("My first window")
window.geometry("500x300")  


user = tk.Label(window, text="Username", font=("Arial", 12))
user.place(x=200, y=50)

entry_user = tk.Entry(window, textvariable=tk.StringVar(), width=30)
entry_user.place(x=150, y=90)

password = tk.Label(window, text="Password", font=("Arial", 12))
password.place(x=200, y=120)

entry_pass = tk.Entry(window, textvariable=tk.StringVar(), width=30)
entry_pass.place(x=150, y=160)

button = tk.Button(window, text="Login", command=take)
button.config(width=15, height=2, font=("Arial", 12),bg="black",fg="white")
button.place(x=170, y=200)

answer = tk.Label(window, text="", font=("Arial", 12))
answer.place(x=210, y=260)



window.mainloop()