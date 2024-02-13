import tkinter as tk


def open_tkinter():
    new_root = tk.Toplevel(root)
    new_root.title("Child Tkinter")
    new_root.geometry("300x100")

    username = tk.Entry(new_root, bg='lightgrey', width=50)
    username.pack(padx=5, pady=5)

    submit_btn = tk.Button(new_root, text="Submit", font=("Arial", 10),
                           command=lambda: close_child(new_root, username.get()))
    submit_btn.pack(padx=5, pady=5)


def close_child(tkinter, text):
    tkinter.destroy()
    label = tk.Label(root, text=f"Hey {text}", font=("Arial", 18))
    label.pack(padx=10, pady=10)


root = tk.Tk()
root.title("Parent Tkinter")
root.geometry("500x400")

button = tk.Button(root, text="Enter you name", font=("Arial", 13), command=open_tkinter)
button.pack(padx=10, pady=10)
root.mainloop()
