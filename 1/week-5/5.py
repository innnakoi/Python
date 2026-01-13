class BankAccount:
    def __init__(self, owner, balance=0):
        self.__owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit must be positive")
        else:
            self.__balance += amount

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient balance")
        elif amount <= 0:
            print("Withdrawal must be positive")
        else:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance


account = BankAccount("Zarina", 2500)
account.deposit(400)
account.withdraw(800)
print(account.get_balance())
