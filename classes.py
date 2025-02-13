class Bankacc:
    def __init__(self, account_holder, balance = 0):
        self.__account_holder = account_holder
        self.__balance = balance
        
    def deposit(self, amount:float):
        if not isinstance(amount, int):
            raise Exception("")
        
        if amount <= 0:
            raise Exception("incorrect value!")
        
        self.__balance += amount
        return self.__balance

    def withdraw(self, amount:float):
        
        if amount > self.__balance:
            raise Exception("Insufficient balance")
        
        self.__balance -= amount
        return self.__balance
        
    def get_balance(self):
        return self.__balance
    
    def get_account_holder(self):
        return self.__account_holder