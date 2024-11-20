"""
ATM Project - Main module
"""

import tkinter as tk
from accounts import *  # The accounts associated with our service
from functions import *

# Create the main window
window = tk.Tk()
window.title("Account Balance Viewer")
window.geometry("600x400")

# Create a frame for the card
card_frame = tk.Frame(window, bg="lightblue", width=400, height=200)
card_frame.pack_propagate(False)  # Prevent resizing to content
card_frame.pack(pady=20)

# Label inside the card
label = tk.Label(card_frame, text="Click to Select Account", bg="lightblue", font=("Arial", 14))
label.pack(expand=True)

# Dropdown menu to select account
selected_account = tk.StringVar(window)
selected_account.set("Pick an Account!")  # Default value

loadAccounts()  # Load Accounts

usernames = [account.username for account in accounts]
account_menu = tk.OptionMenu(card_frame, selected_account, *usernames)
account_menu.pack()

# Button to view balance
view_button = tk.Button(card_frame, text="View Balance", command=lambda: show_balance(get_account_by_username(selected_account.get())))
view_button.pack(pady=10)

# Run the application
window.mainloop()
