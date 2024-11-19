from tkinter import messagebox

from accounts import accounts

def show_balance(acc):
    balance = acc.balance
    username = acc.username
    messagebox.showinfo("Account Balance", f"Balance for {username}: ${balance:.2f}")

def get_account_by_username(username):
    for account in accounts:
        if account.username == username:
            return account
