# Adding functionalities to the Tkinter
import tkinter as tk
from tkinter import messagebox


class MyGUI:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Message Popup")
        self.root.geometry("500x300")

        # Creating menu bar in the Tkinter
        self.menubar = tk.Menu(self.root)

        self.file_menu = tk.Menu(self.menubar, tearoff=0)  # tearoff to avoid dash line or space above menu
        # Adding menu items
        self.file_menu.add_command(label="Close", command=self.on_closing)
        self.file_menu.add_separator()  # To add a seperator line between items
        self.file_menu.add_command(label="Direct Exit", command=exit)

        self.action_menu = tk.Menu(self.menubar, tearoff=0)
        self.action_menu.add_command(label="Show message", command=self.show_message)

        # Adding menu item's heading
        self.menubar.add_cascade(menu=self.file_menu, label="File")
        self.menubar.add_cascade(menu=self.action_menu, label="Action")
        self.root.config(menu=self.menubar)

        self.label = tk.Label(self.root, text="Write your message", font=("Arial", 18))
        self.label.pack(padx=10, pady=10)

        self.textbox = tk.Text(self.root, height=3, font=("Arial", 18))
        # Binding a KeyPress and pass it ti a new function | It automatically passes a event to that function
        self.textbox.bind("<KeyPress>", self.shortcut)
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

        self.clear_button = tk.Button(self.root, text="Clear", font=("Arial", 10), command=self.clear)
        self.clear_button.pack(padx=10, pady=10)

        # "WM_DELETE_WINDOW":  tell that user is clicking on close "X" symbol
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()

    def show_message(self):
        state_of_checkbox = self.check_state.get()  # Get the state of the checkbox
        text_from_textbox = self.textbox.get(
            '1.0',  # To get the text from 1st index (from beginning)
            tk.END  # To get the text till the end
        )  # Get the text from textbox

        if state_of_checkbox:
            if len(text_from_textbox) != 1:
                messagebox.showinfo(title="Message", message=text_from_textbox)

        else:
            print(f"No message box should be displayed. Here is your message {text_from_textbox}")

    def shortcut(self, event):  # Event will have details about the key pressed
        if event.state in (4, 6) and event.keysym == 'Return':
            self.show_message()

    def on_closing(self):
        # Confirmation dialog box
        if messagebox.askyesno(title="Close windows?", message="Do you really want to close this windows?"):
            self.root.destroy()  # To destroy the Tkinter

    def clear(self):
        self.textbox.delete('1.0', tk.END)


MyGUI()
