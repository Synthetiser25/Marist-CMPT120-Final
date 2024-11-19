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


user1 = Account("user1", "password", 123)
user2 = Account("user2", "password", 345)

accounts = [user1, user2]
