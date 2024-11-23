import types
from tkinter import messagebox, simpledialog
from accounts import accounts


def load_user(acc):
    login_attempt = login(acc)  # Will receive true or false by user
    if login_attempt:
        import main
        main.create_new_window(acc)


def deposit(acc):
    amount = round(float(simpledialog.askstring("Amount", "Enter amount to deposit")), 2)
    acc.deposit(amount)


def withdraw(acc):
    amount = round(float(simpledialog.askstring("Amount", "Enter amount to withdraw")), 2)
    acc.withdraw(amount)


def login(acc):
    count = 0
    input_password = simpledialog.askinteger("Password", "What is your password?", minvalue=1000, maxvalue=9999)
    # Password checker
    while count <= 2:
        # Check if cancel
        if type(input_password) == types.NoneType:
            return False
        # Check password
        if input_password == acc.password:
            return True
        # Set up next iter.
        else:
            count += 1
            if count <= 2:
                messagebox.showwarning("Incorrect","Incorrect password! You have " +str(3-count)+" attempts remaining")
        if count <= 2:
            input_password = simpledialog.askinteger("Password", "What is your password?", minvalue=1000, maxvalue=9999)
    messagebox.showwarning("Incorrect", "Too many incorrect attempts! Please try again later.")
    return False


def show_balance(acc):
    balance = acc.balance
    username = acc.username
    messagebox.showinfo("Account Balance", f"Balance for {username}: ${balance:.2f}")


def get_account_by_username(username):
    for account in accounts:
        if account.username == username:
            return account
