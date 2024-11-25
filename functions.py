import types
from tkinter import messagebox, simpledialog

from accounts import accounts, writeAccounts, Account


def create_account():
    username = simpledialog.askstring("New User", "Enter your username: ")
    password = simpledialog.askstring("New User", "Enter your PIN: ")
    if len(password) != 4:
        password = simpledialog.askstring("New User", "Enter a 4 DIGIT PIN: ")
    start_bal = simpledialog.askfloat("New User", "Enter your starting balance: ")
    if type(username) == types.NoneType or type(password) == types.NoneType or type(start_bal) == types.NoneType:
        messagebox.showwarning("Failed", "Account creation failed! Please try again later.")
        return False
    accounts.append(Account(str(username), int(password), round(float(start_bal), 2)))
    writeAccounts()
    return True


def close_account(username):
    password = simpledialog.askinteger("Close Account", "Enter your PIN to close account: ")
    prevLength = len(accounts)
    for user in accounts:
        if user.username == username and user.password == password and type(password) != types.NoneType:
            messagebox.showwarning(f"{username}'s Account","Account Deleted")
            accounts.remove(user)
    if len(accounts) == prevLength:
        return False
    writeAccounts()
    return True


def load_user(acc, selected_account, account_menu, card_frame):
    login_attempt = login(acc)  # Will receive true or false by user
    if login_attempt:
        import main
        main.create_new_window(acc, selected_account, account_menu, card_frame)


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


def get_account_by_username(username):
    for account in accounts:
        if account.username == username:
            return account
