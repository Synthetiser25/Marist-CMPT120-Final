from tkinter import messagebox, simpledialog
from accounts import accounts


def load_user(acc):
    login_attempt = login(acc)  # Will receive true or false by user
    if login_attempt:
        import main
        main.create_new_window(acc)


def deposit(acc):
    amount = float(simpledialog.askstring("Amount", "Enter amount to deposit"))
    acc.deposit(amount)


def withdraw(acc):
    amount = float(simpledialog.askstring("Amount", "Enter amount to withdraw"))
    acc.withdraw(amount)


def login(acc):
    count = 0
    input_password = simpledialog.askinteger("Password", "What is your password?", minvalue=1000, maxvalue=9999)
    # Password checker
    while count < 2:
        if input_password == acc.password:
            return True
        else:
            count += 1
            messagebox.showwarning("Incorrect","Incorrect password! You have " +str(3-count)+" attempts remaining")
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
