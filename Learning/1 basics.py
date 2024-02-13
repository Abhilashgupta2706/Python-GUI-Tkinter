import tkinter as tk

root = tk.Tk()

root.title("Tkinter Title")
root.geometry("500x500")  # X & Y

# Creating Label for displaying text
label = tk.Label(root, text="Hello World!", font=('Arial', 18))
label.pack(padx=20, pady=20)  # Passing Label to Root with padding (optional)

# Creating Label an input filed with multi lines
text_box = tk.Text(root, height=3, font=('Arial', 16))  # Height is optional
text_box.pack(padx=5, pady=5)  # Passing Text to Root with padding (optional)

# Creating Label an input filed with one line input
my_entry = tk.Entry(root, bg='lightgrey', width=50)  # bg: BackgroundColor | fg: TextColor | Use show="*" for passwords
# my_entry.insert(0, "Username")  # Default Text
my_entry.pack(padx=5, pady=5)  # Passing Text to Root with padding (optional)

# Button
button = tk.Button(root, text="Click Me!", font=('Arial', 10))
button.pack(padx=5, pady=5)

# To run the Tkinter
root.mainloop()
