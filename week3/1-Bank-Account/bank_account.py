class BankAccount:

    def __init__(self, name, balance, currency):
        if balance < 0:
            raise ValueError

        self.history = []
        self.name = name
        self.balance = balance
        self.currency = currency
        self.history.append("Account was created")

    def deposit(self, amount):
        if amount < 0:
            raise ValueError
        self.balance += amount
        self.history.append("Deposited " + str(amount) + str(self.currency))

    def withdraw(self, amount):
        if amount < 0:
            raise ValueError
        if amount > self.balance:
            self.history.append("withdraw for {}{} failed."
                                .format(str(amount), self.currency))
            return False
        else:
            self.balance -= amount
            self.history.append(str(amount) +
                                self.currency + " was withdrawed")
            return True

    def __str__(self):
        message = "Bank account for {} with balance of {}{}"
        return message.format(self.name, self.balance, self.currency)

    def get_balance(self):
        self.history.append("Balance check -> " + str(self.balance))
        return self.balance

    def __int__(self):
        self.history.append("__int__ check -> " + str(self.balance))
        return self.balance

    def transfer_to(self, account, amount):
        if self.currency != account.currency:
            raise ValueError
        if self.balance < amount:
            self.history.append("Transfer to " + account.name + " for " +
                                str(amount) + account.currency + " failed.")

            account.history.append("Transfer from " + self.name + " for " +
                                   str(amount) + self.currency + " failed.")
            return False

        self.balance -= amount
        account.balance += amount
        self.history.append("Transfer to " + account.name +
                            " for " + str(amount) + account.currency)

        account.history.append("Transfer from " + self.name +
                               " for " + str(amount) + self.currency)
        return True

    def account_history(self):
        return self.history
