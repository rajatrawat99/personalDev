class Account:

    def __init__(self, filepath):
        self.path = filepath
        with open(filepath, 'r') as file:
            self.balance=int(file.read())

    def withdraw(self, amount):
        self.balance=self.balance - amount
        return self.balance

    def deposit(self, amount):
        self.balance=self.balance + amount
        return self.balance

    def commit(self):
        with open(self.path, 'w') as file:
            file.write(str(self.balance))
            file.close()


account = Account("balance.txt")
print(account)
print(account.balance)
print(account.withdraw(0))
print(account.deposit(10))
print(account.balance)
account.commit()
