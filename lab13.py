from classes import Bankacc

account1 = Bankacc("Ahmed", 1000)

account1.deposit(1000)

try:
    account1.withdraw(3000)
except Exception as e:
    print(e)
    
print(account1.get_balance())
