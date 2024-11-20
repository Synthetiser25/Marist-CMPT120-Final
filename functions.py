from tkinter import messagebox, simpledialog

from accounts import accounts

def load_user(acc):
    input_password = age = simpledialog.askinteger("Password", "What is your password?", minvalue=1000, maxvalue=9999)


def show_balance(acc):
    balance = acc.balance
    username = acc.username
    messagebox.showinfo("Account Balance", f"Balance for {username}: ${balance:.2f}")

def get_account_by_username(username):
    for account in accounts:
        if account.username == username:
            return account
