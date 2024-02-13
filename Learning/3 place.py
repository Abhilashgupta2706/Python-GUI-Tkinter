import tkinter as tk

root = tk.Tk()

root.title("Tkinter Title")
root.geometry("500x500")

label = tk.Label(root, text="Hello World!", font=('Arial', 18))
label.pack(padx=20, pady=20)

text_box = tk.Text(root, height=3, font=('Arial', 16))
text_box.pack(padx=5, pady=5)

# Adding frame layout
button_frame = tk.Frame(root)
button_frame.columnconfigure(0, weight=1)  # Weight is to fill the all empty space
button_frame.columnconfigure(1, weight=1)

btn1 = tk.Button(button_frame, text="Submit", font=("Arial", "10"))
btn1.grid(row=0, column=0, sticky=tk.W + tk.E)

btn2 = tk.Button(button_frame, text="Cancel", font=("Arial", "10"))
btn2.grid(row=0, column=1, sticky=tk.W + tk.E)

button_frame.pack(padx=5, pady=5, fill='x')

# To place the button using x-axis & y-axis instant of placing after previous pack
anotherBtn = tk.Button(root, text="Place button")
anotherBtn.place(x=150, y=300, height=50, width=200)

root.mainloop()
