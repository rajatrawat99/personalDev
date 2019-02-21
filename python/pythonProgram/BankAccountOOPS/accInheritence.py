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

class Checking(Account):   #Account here is the base class
    """ this is a checking account info""" # this gives us info of the class

    type = 'checking' # its a class variable

    def __init__(self, filepath, fee): # fee is instance variable of Checking class
        Account.__init__(self,filepath) # Creates the default method of Account class
        self.fee=fee

    def transfer(self, amount):
        self.balance=self.balance - amount - self.fee # balance will be taken out from base class


checking = Checking("balance.txt", 1)
print('\n')
#checking.deposit(10)
checking.transfer(10)
print(checking.balance) # Accessing the function of the base class
print(checking.type)
print(checking.__doc__) # prints the doc string
checking.commit()
