import tkinter as tk
from tkinter import messagebox
import string

def check_password():
    password = password_entry.get()

    # Maximum char count
    if len(password) > 128:
        messagebox.showwarning("Weak Password", "Password should not exceed 128 characters.")
        return
     
    # Minimum char count
    if len(password) <= 10:
        messagebox.showwarning("Weak Password", " Weak Password, Increase character count.")
        return
    
    # Minimum numeric count
    if not any(char.isdigit() for char in password):
        messagebox.showwarning("Weak Password", "Weak Password, No numeric characters.")
        return
    
    #Minimum uppercase count
    if not any(char.isupper() for char in password):
        messagebox.showwarning("Weak Password", "Weak Password, No uppercase characters.")
        return
  
    #Minimum lowercase count
    if not any(char.islower() for char in password):
        messagebox.showwarning("Weak Password", "Weak Password, No lowercase characters.")
        return
    
    #Special char count
    special_characters = set(string.punctuation)
    if sum(1 for char in password if char in special_characters) < 1:
        messagebox.showwarning("Weak Password", "Weak Password, Include at least one special character.")
        return
    
    #Check for not more than 2 identical characters in a row
    for i in range(len(password) - 2):
        if password[i] == password[i+1] == password[i+2]:
            messagebox.showwarning("Weak Password", "Weak Password, More than 2 identical characters in a row.")
            return
    
    # All password criteria is met
    messagebox.showinfo("Strong Password", "Password is strong and meets all criteria!")

# Create main window
root = tk.Tk()
root.title("OWASP Password Checker")

# Create password label and entry
password_label = tk.Label(root, text="Please Enter Password:")
password_label.pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()

# Create check button
check_button = tk.Button(root, text="Check Password", command=check_password)
check_button.pack()

# Run the main event loop
root.mainloop()