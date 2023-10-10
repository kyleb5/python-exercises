# 1. RUN this code to see the error
# --------------
# 2. After running, comment out line 16 AND comment in lines 17-22
# Now, if an incorrect type of value is passed, a human-friendly message is output to the console and the exception is re-raised up to the calling code.


class BankAccount():

    def __init__(self):
        self.balance = 0

    def add_money(self, amount):
        """Add money to a bank account

        Arguments:
          amount - A numerical value by which the bank account's balance will increase
        """
        self.balance += amount
        try:
            self.balance += amount
            return self.balance
        except TypeError:
            print('(Error): The add_money method requies a numeric value')
            raise

    def withdraw_money(self, amount):
        """Withdraw money to a bank account

        Arguments:
          amount - A numerical value by which the bank account's balance will decrease
        """
        self.balance -= amount


my_account = BankAccount()
my_account.add_money('Gazillion dollars')
