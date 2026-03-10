class BankAccount:

    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

        if self.owner == "Diana":
            print(f"{self.owner} поповнила рахунок на {amount}")
        else:
            print(f"{self.owner} поповнив рахунок на {amount}")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Недостатньо грошей")
        else:
            self.__balance -= amount

            if self.owner == "Diana":
                print(f"{self.owner} зняла {amount}")
            else:
                print(f"{self.owner} зняв {amount}")

    def get_balance(self):
        return self.__balance


acc1 = BankAccount("Edgar", 10000000)
acc2 = BankAccount("Ivan", 5000)
acc3 = BankAccount("Diana", 2000)


acc1.deposit(300)
acc1.withdraw(200)
print(acc1.get_balance())

acc2.withdraw(600)
acc2.deposit(100)
print(acc2.get_balance())

acc3.deposit(50)
acc3.withdraw(100)
print(acc3.get_balance())