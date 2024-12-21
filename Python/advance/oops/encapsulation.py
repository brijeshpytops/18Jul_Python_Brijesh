"""
What is encapsulation in python?

Encapsulation is a way of bundling data and the methods that operate on that data into a single unit. It is achieved by using private variables and public methods.
"""

class ATM:
    def __init__(self, holder_name, pin):
        self.holder_name = holder_name # public
        self.__account_balance = 0 # private
        self.__pin = pin # private

    def get_account_balance(self):
        return self.__account_balance
    
    def set_account_balance(self, amount):
        if amount < 0:
            print("Error: Negative balance not allowed.")
            return
        self.__account_balance = amount

brijesh = ATM("brijesh gondaliya", 1123)

# brijesh.set_account_balance(5000)

# print("Current balance: ", brijesh.get_account_balance())

# brijesh.set_account_balance(-1000)

# print("Current balance: ", brijesh.get_account_balance())

# brijesh.__account_balance = 2000

# print("Current balance: ", brijesh.get_account_balance())

# print(brijesh.__pin)

# print(brijesh._ATM__pin) # Name mangling syntax: _className__varname

