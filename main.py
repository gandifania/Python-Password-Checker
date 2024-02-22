import string
import getpass
import tkinter as tk
from tkinter import messagebox

def check_pwd():
    password = getpass.getpass("Enter Password: ")
    strength = 0
    remarks = ''
    lower_count = upper_count = num_count =wspace_count = special_count = word_count = 0

    for char in list(password):
        if char in string.ascii_lowercase:
            lower_count += 1
        elif char in string.ascii_uppercase:
            upper_count += 1
        elif char in string.digits:
            num_count += 1
        elif char == '':
            wspace_count += 1
        else:
            special_count += 1
    
    if lower_count >= 1:
        strength += 1
    if upper_count >= 1:
        strength += 1
    if num_count >= 1:
        strength += 1
    if wspace_count >= 1:
        strength += 1
    if special_count >= 1:
        strength += 1

 # Minimum length check
    if len(password) <= 9:
        messagebox.showwarning("Weak Password", "Password should be at least 10 characters long.")
        return

    if strength == 1:
        remarks = "VERY BAD: Are you tryna get hacked my boy?"
    elif strength == 2:
        remarks = "BAD: What is this weak sauce!"
    elif strength == 3:
        remarks = "WEAK: Trash but passable"
    elif strength == 4:
        remarks = "HARD: Mid but we could be better"
    elif strength == 5:
        remarks = "VERY STRONG: Solid, you aight"
    
    print('Your password has: ')
    print(f"{lower_count} lowercase characters")
    print(f"{upper_count} uppercase characters")
    print(f"{num_count} numeric characters")
    print(f"{wspace_count} whitespace characters")
    print(f"{special_count} special characters")

    print(f"Password Strength: {strength}")
    print(f"Hint: {remarks}")
    
    def ask_pwd(another_pwd=False):
        valid = False
        if another_pwd:
            choice = input('Do you want to enter another password (y/n): ')
        else:
            choice=input('Do you want to check password strength (y/n): ')
        while not valid:
            if choice.lower() == 'y':
                return True
            elif choice.lower() == 'n':
                return False
            else:
                print('Invalid, Try Again')

    #Place GUI Here
     
   # Create the main window
root = tk.Tk()
root.title("Password Strength Checker")

# Create a label and entry for the password
password_label = tk.Label(root, text="Enter Password:")
password_label.pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()

# Create a button to check the password
check_button = tk.Button(root, text="Check Password", command=check_pwd())
check_button.pack()

# Run the Tkinter event loop
root.mainloop()



