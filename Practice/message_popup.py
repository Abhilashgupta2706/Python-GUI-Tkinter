# Adding functionalities to the Tkinter
import tkinter as tk
from tkinter import messagebox


class MyGUI:

    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("500x300")

        self.label = tk.Label(self.root, text="Your Message", font=("Arial", 18))
        self.label.pack(padx=10, pady=10)

        self.textbox = tk.Text(self.root, height=3, font=("Arial", 18))
        self.textbox.pack(padx=10, pady=10)

        self.check_state = tk.IntVar()  # To store the checkbox value

        self.checkbox = tk.Checkbutton(self.root,
                                       text="Show Message Box?",
                                       font=("Arial", 15),
                                       variable=self.check_state)  # To store the checkbox value to variable
        self.checkbox.pack(padx=10, pady=10)

        self.button = tk.Button(self.root,
                                text="Submit",
                                font=("Arial", 10),
                                command=self.show_message)
        # Pass function (Don't call ex: self.show_message()) to execute on btn click

        self.button.pack(padx=10, pady=10)

        self.root.mainloop()

    def show_message(self):
        state_of_checkbox = self.check_state.get()  # Get the state of the checkbox
        text_from_textbox = self.textbox.get(
            '1.0',  # To get the text from 1st index (from beginning)
            tk.END  # To get the text till the end
        )  # Get the text from textbox

        if state_of_checkbox:
            messagebox.showinfo(title="Message", message=text_from_textbox)
        else:
            print(f"No message box should be displayed. Here is your message {text_from_textbox}")


MyGUI()
