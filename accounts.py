class Account:
    def __init__(self, username, password, balance):
        self.username = username
        self.password = password
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        writeAccounts()
        return self.balance

    def withdraw(self, amount):
        self.balance -= amount
        writeAccounts()
        return self.balance


accounts = []


def loadAccounts():
    with open('accountStorage.txt', 'r') as f:
        file = f.readlines()

    for i, line in enumerate(file):
        elements = line.strip().split(",")
        accounts.append(Account(elements[0], int(elements[1]), round(float(elements[2]), 2)))


def writeAccounts():
    with open('accountStorage.txt', 'w') as f:
        for account in accounts:
            f.write(str(account.username) + "," + str(account.password) + "," + str(format(account.balance, '.2f')) + "\n")
