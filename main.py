"""
ATM Project - Main module
"""

import tkinter as tk
from accounts import *  # The accounts associated with our service
from functions import *


def create_new_window(acc):
    # Create the main account window
    account_window = tk.Tk()
    account_window.title(f"{acc.username}'s Account")
    account_window.geometry("600x400")
    account_window.configure(bg="white")

    # Create a header for the account window
    header_label = tk.Label(account_window, text=f"{acc.username}'s Account", bg="white", fg="black",
                            font=("Arial", 24, "bold"))
    header_label.pack(pady=20)

    # Create a frame for account details
    card_frame = tk.Frame(account_window, bg="lightblue", width=400, height=200, relief="groove", bd=2)
    card_frame.pack_propagate(False)
    card_frame.pack(pady=20)

    # Display account balance within the card frame
    balance_label = tk.Label(card_frame, text=f"Balance: ${acc.balance}", bg="lightblue", fg="black",
                             font=("Arial", 18))
    balance_label.pack(pady=10)

    # Create a button frame for Deposit and Withdraw buttons
    button_frame = tk.Frame(account_window, bg="white")
    button_frame.pack(pady=20)

    # Deposit Button
    deposit_button = tk.Button(button_frame, text="Deposit", bg="#4CAF50", fg="black", font=("Arial", 14), width=15,
                               command=lambda: [deposit(acc), balance_label.config(text=f"Balance: ${acc.balance}")])
    deposit_button.grid(row=0, column=0, padx=10)

    # Withdraw Button
    withdrawal_button = tk.Button(button_frame, text="Withdraw", bg="#F44336", fg="black", font=("Arial", 14), width=15,
                                  command=lambda: [withdraw(acc),
                                                   balance_label.config(text=f"Balance: ${acc.balance}")])
    withdrawal_button.grid(row=0, column=1, padx=10)

    # Run the Tkinter main loop
    account_window.mainloop()


def main():
    # Create the main window
    window = tk.Tk()
    window.title("Account Balance Viewer")
    window.geometry("600x400")
    window.configure(bg="white")  # Set background color for the window

    # Create a header label for the window
    header_label = tk.Label(window, text="Welcome to Account Viewer", bg="white", fg="black",
                            font=("Arial", 20, "bold"))
    header_label.pack(pady=20)

    # Create a frame for the card with styled appearance
    card_frame = tk.Frame(window, bg="lightblue", width=400, height=250, relief="ridge", bd=3)
    card_frame.pack_propagate(False)  # Prevent resizing to content
    card_frame.pack(pady=20)

    # Label inside the card
    label = tk.Label(card_frame, text="Select an Account", bg="lightblue", fg="black", font=("Arial", 16, "italic"))
    label.pack(pady=10)

    # Dropdown menu to select account
    selected_account = tk.StringVar(window)
    selected_account.set("Pick an Account!")  # Default value

    loadAccounts()  # Load accounts (assuming this function is defined)

    usernames = [account.username for account in accounts]
    account_menu = tk.OptionMenu(card_frame, selected_account, *usernames)
    account_menu.config(font=("Arial", 12), bg="white", fg="black", relief="groove")
    account_menu.pack(pady=10)

    # Button to view account details
    view_button = tk.Button(card_frame, text="View Account", bg="#007BFF", fg="black", font=("Arial", 14), width=15,
                            command=lambda: load_user(get_account_by_username(selected_account.get())))
    view_button.pack(pady=15)

    # Footer for additional information
    footer_label = tk.Label(window, text="Manage your accounts securely and easily", bg="white", fg="gray",
                            font=("Arial", 10))
    footer_label.pack(side="bottom", pady=10)

    # Run the application
    window.mainloop()


if __name__ == "__main__":
    main()
