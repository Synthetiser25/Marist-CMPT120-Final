"""
ATM Project - Main module
"""

import tkinter as tk
from accounts import *  # The accounts associated with our service
from functions import *


def create_new_window(acc, selected_account, account_menu, card_frame):
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
    balance_label = tk.Label(card_frame, text=f"Balance: ${acc.balance:.2f}", bg="lightblue", fg="black",
                             font=("Arial", 18))
    balance_label.pack(pady=10)

    # Create a button frame for Deposit and Withdraw buttons
    button_frame = tk.Frame(account_window, bg="white")
    button_frame.pack(pady=20)

    # Deposit Button
    deposit_button = tk.Button(button_frame, text="Deposit", bg="#4CAF50", fg="black", font=("Arial", 14), width=15,
                               command=lambda: [deposit(acc), balance_label.config(text=f"Balance: ${acc.balance:.2f}")])
    deposit_button.grid(row=0, column=0, padx=10)

    # Withdraw Button
    withdrawal_button = tk.Button(button_frame, text="Withdraw", bg="#F44336", fg="black", font=("Arial", 14), width=15,
                                  command=lambda: [withdraw(acc),
                                                   balance_label.config(text=f"Balance: ${acc.balance:.2f}")])
    withdrawal_button.grid(row=0, column=1, padx=10)

    # Close Account
    close_button = tk.Button(button_frame, text="Close Account", bg="#007BFF", fg="black", font=("Arial", 14), width=15,
                             command=lambda: [close_account(acc.username),
                                              update_dropdown(selected_account, account_menu, card_frame),
                                              account_window.destroy()])
    close_button.grid(row=0, column=2, padx=10)

    # Run the Tkinter main loop
    account_window.mainloop()


def update_dropdown(menu_var, menu_widget, parent_frame):
    """
    Update the dropdown menu with the latest list of usernames.
    """

    loadAccounts()  # Reload accounts from the source
    usernames = [account.username for account in accounts]

    # Clear the old menu
    menu_widget['menu'].delete(0, 'end')

    # Add new menu items
    for username in usernames:
        menu_widget['menu'].add_command(label=username,
                                        command=lambda value=username: menu_var.set(value))

    # Reset the selected value
    menu_var.set("Pick an Account!")


# Main function adjusted
def main():
    # Create the main window
    window = tk.Tk()
    window.title("Account Balance Viewer")
    window.geometry("600x400")
    window.configure(bg="white")

    # Header label
    header_label = tk.Label(window, text="Welcome to Account Viewer", bg="white", fg="black",
                            font=("Arial", 20, "bold"))
    header_label.pack(pady=20)

    # Card frame
    card_frame = tk.Frame(window, bg="lightblue", width=400, height=250, relief="ridge", bd=3)
    card_frame.pack_propagate(False)
    card_frame.pack(pady=20)

    # Label inside the card
    label = tk.Label(card_frame, text="Select an Account", bg="lightblue", fg="black", font=("Arial", 16, "italic"))
    label.pack(pady=10)

    # Dropdown menu to select account
    selected_account = tk.StringVar(window)
    selected_account.set("Pick an Account!")

    account_menu = tk.OptionMenu(card_frame, selected_account, ())
    account_menu.config(font=("Arial", 12), bg="white", fg="black", relief="groove")
    account_menu.pack(pady=10)

    # Initial dropdown population
    update_dropdown(selected_account, account_menu, card_frame)

    # Button to view account details
    view_button = tk.Button(card_frame, text="View Account", bg="#007BFF", fg="black", font=("Arial", 14), width=15,
                            command=lambda: load_user(get_account_by_username(selected_account.get()), selected_account, account_menu, card_frame))
    view_button.pack(pady=15)

    # Button to Create Account
    account_button = tk.Button(card_frame, text="Create Account", bg="#007BFF", fg="black", font=("Arial", 14),
                               width=15, command=lambda: (create_account(), update_dropdown(selected_account, account_menu, card_frame)))
    account_button.pack(pady=15)

    # Footer
    footer_label = tk.Label(window, text="Manage your accounts securely and easily", bg="white", fg="gray",
                            font=("Arial", 10))
    footer_label.pack(side="bottom", pady=10)

    # Run the application
    window.mainloop()


if __name__ == "__main__":
    main()