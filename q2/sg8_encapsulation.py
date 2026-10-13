class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = float(balance)

    @property
    def account_number(self):
        return self.__account_number
    
    @property
    def balance(self):
        return self.__balance

    def set_account_number(self, account_number):
        self.__account_number = account_number
        print("Account number has been changed.")

    def get_account_number(self):
        return self.__account_number

    def set_balance(self, balance):
        if float(balance) >= 0:
            self.__balance = float(balance)
            print(f"Balance updated to {self.__balance}")
        else:
            self.__balance = float(balance)
            print(f"Balance updated to {balance}")
            print("Warning! Your balance must not be negative! Fix it As soon as possible!")

    def get_balance(self):
        return self.__balance

accounts = []

ba1 = BankAccount("45754", 500)
accounts.append(ba1)

print(f"Account {len(accounts)}")
print(f"Account number: {accounts[0].get_account_number()}")
print(f"Balance: {accounts[0].get_balance()}")
print()

ba1.set_balance(-1000)
#ba1.set_balance(5000)
ba1.set_account_number("51515")

print()
print(f"Account {len(accounts)}")
print(f"Account number: {accounts[0].get_account_number()}")
print(f"Balance: {accounts[0].get_balance()}") 
