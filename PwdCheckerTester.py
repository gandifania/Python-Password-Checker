import tkinter as tk
from tkinter import messagebox

def check_password():
    pwd = password_entry.get()

    # Minimum length check
    if len(pwd) <= 9:
        messagebox.showwarning("Weak Password", "Are you tryna get hacked my boy?")
        return

    # Additional checks can be added here

    messagebox.showinfo("Strong Password", "Password is strong!")

# Create main window
root = tk.Tk()
root.title("Password Checker")

# Create password label and entry
password_label = tk.Label(root, text="Enter Password:")
password_label.pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()

# Create check button
check_button = tk.Button(root, text="Check Password", command=check_password)
check_button.pack()

# Run the main event loop
root.mainloop()
