class Account:
    def __init__(self, username, password, balance):
        self.username = username
        self.password = password
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance


accounts = []


def loadAccounts ():
    with open('accountStorage.txt', 'r') as f:
        file = f.readlines()

    for i, line in enumerate(file):
        elements = line.split(",")
        accounts.append(Account(elements[0], int(elements[1]), int(elements[2])))
