import types
from tkinter import messagebox, simpledialog
from accounts import accounts, writeAccounts, Account


def create_account(username, password, start_bal):  # Jonas use this to create account with the inputs (Make sure to double check with user the info before sending to function)
    accounts.append(Account(str(username), int(password), round(float(start_bal), 2)))
    writeAccounts()


def close_account(username, password):  # Jonas use this to close account, will return True if it closed or False if the information was wrong
    for user in accounts:
        if user.username == username and user.password == password:
            accounts.remove(user)
        else:
            return False
    writeAccounts()
    return True


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


def get_account_by_username(username):
    for account in accounts:
        if account.username == username:
            return account
