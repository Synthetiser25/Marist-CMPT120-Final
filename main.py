"""
ATM Project - Main module
"""

import tkinter as tk
from tkinter import messagebox
from accounts import accounts  # The accounts associated with our service

def show_balance(account_name):
    balance = accounts.get(account_name, 0)
    messagebox.showinfo("Account Balance", f"Balance for {account_name}: ${balance:.2f}")

# Create the main window
window = tk.Tk()
window.title("Account Balance Viewer")
window.geometry("300x200")

# Create a frame for the card
card_frame = tk.Frame(window, bg="lightblue", width=250, height=150)
card_frame.pack_propagate(False)  # Prevent resizing to content
card_frame.pack(pady=20)

# Label inside the card
label = tk.Label(card_frame, text="Click to Select Account", bg="lightblue", font=("Arial", 14))
label.pack(expand=True)

# Dropdown menu to select account
selected_account = tk.StringVar(window)
selected_account.set("Account 1")  # Default value

account_menu = tk.OptionMenu(card_frame, selected_account, *accounts.keys())
account_menu.pack()

# Button to view balance
view_button = tk.Button(card_frame, text="View Balance", command=lambda: show_balance(selected_account.get()))
view_button.pack(pady=10)

# Run the application
window.mainloop()
