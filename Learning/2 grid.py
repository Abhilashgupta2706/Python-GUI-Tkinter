import tkinter as tk

root = tk.Tk()

root.title("Tkinter Title")
root.geometry("500x500")

# Creating Label for displaying text
label = tk.Label(root, text="Hello World!", font=('Arial', 18))
label.pack(padx=20, pady=20)

text_box = tk.Text(root, height=3, font=('Arial', 16))
text_box.pack(padx=5, pady=5)

# Adding frame layout
button_frame = tk.Frame(root)
# For x number of columns x number of columnconfigure
button_frame.columnconfigure(0, weight=1)  # Weight is to fill the all empty space
button_frame.columnconfigure(1, weight=1)
button_frame.columnconfigure(2, weight=1)

# Creating Buttons but passing to button_frame rather than root as master
btn1 = tk.Button(button_frame, text="Button 1", font=("Arial", "10"))
# To stick the button from West2East (Left2Right) | Rows & Columns define buttons position in grid
btn1.grid(row=0, column=0, sticky=tk.W + tk.E)

btn2 = tk.Button(button_frame, text="Button 2", font=("Arial", "10"))
btn2.grid(row=0, column=1, sticky=tk.W + tk.E)

btn3 = tk.Button(button_frame, text="Button 3", font=("Arial", "10"))
btn3.grid(row=0, column=2, sticky=tk.W + tk.E)

btn4 = tk.Button(button_frame, text="Button 4", font=("Arial", "10"))
btn4.grid(row=1, column=0, sticky=tk.W + tk.E)

btn5 = tk.Button(button_frame, text="Button 5", font=("Arial", "10"))
btn5.grid(row=1, column=1, sticky=tk.W + tk.E)

btn6 = tk.Button(button_frame, text="Button 6", font=("Arial", "10"))
btn6.grid(row=1, column=2, sticky=tk.W + tk.E)

button_frame.pack(padx=5, pady=5, fill='x')  # Fill will stretch/fill the button in x-axis

root.mainloop()
