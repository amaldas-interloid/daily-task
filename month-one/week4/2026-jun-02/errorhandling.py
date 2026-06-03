import logging

logging.basicConfig(
    filename="bank.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            logging.info(
                f"{self.owner} deposited {amount}. New balance: {self.balance}"
            )
            return self.balance
        else:
            logging.warning(
                f"{self.owner} attempted to deposit a non-positive amount: {amount}"
            )
            return "Deposit amount must be positive"

    def withdraw(self, amount):
        if amount > self.balance:
            logging.error(
                f"{self.owner} attempted to withdraw {amount}, but only has {self.balance} available."
            )
            raise ValueError("Insufficient funds")
        elif amount <= 0:
            logging.warning(
                f"{self.owner} attempted to withdraw a non-positive amount: {amount}"
            )
            raise ValueError("Withdrawal amount must be positive")
        else:
            self.balance -= amount
            logging.info(f"{self.owner} withdrew {amount}. New balance: {self.balance}")
            return self.balance


account = BankAccount("Amaldas", 1000)
print(account.deposit(500))
print(account.withdraw(200))


