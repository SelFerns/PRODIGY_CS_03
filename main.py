import tkinter as tk
from tkinter import messagebox
import string

def check_pass(pswd, common_passwords):
    password_length = len(pswd)

    if pswd in common_passwords:
        return "Password is too common, choose a different one.", False
    elif password_length < 8:
        return "Password is too short, should be at least 8 characters long.", False
    elif not any(c.isupper() for c in pswd):
        return "Password should include at least one uppercase letter.", False
    elif not any(c.islower() for c in pswd):
        return "Password should include at least one lowercase letter.", False
    elif not any(c in string.punctuation for c in pswd):
        return "Password should include at least one special character.", False
    elif not any(c.isdigit() for c in pswd):
        return "Password should include at least one number.", False
    else:
        return "Strong Password!", True

def on_submit():
    password = entry.get()
    message, is_strong = check_pass(password, common_passwords)
    result_label.config(text=message, fg="green" if is_strong else "red")

def load_common_passwords(filename):
    try:
        with open(filename, "r") as file:
            return set(file.read().splitlines())
    except FileNotFoundError:
        messagebox.showerror("Error", f"File {filename} not found!")
        return set()

def main():
    global entry, result_label, common_passwords

    common_passwords = load_common_passwords("passwords.txt")

    root = tk.Tk()
    root.title("Password Complexity Checker")

    root.configure(padx=50, pady=50)

    tk.Label(root, text="Enter your password:").pack(pady=10)
    
    entry = tk.Entry(root, show="*", width=30)
    entry.pack(pady=5)

    tk.Button(root, text="Check Password", command=on_submit).pack(pady=10)

    result_label = tk.Label(root, text="")
    result_label.pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()
