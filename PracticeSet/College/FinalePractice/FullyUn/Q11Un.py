'''
Write a Python program to create a class representing a bank. Include methods
for managing customer accounts and transactions. i.e., create_account().
make_deposite(), make_withdrawal(), check_balance().
'''


class Bank:
    def __init__(self):
        self.balance = 0

    def create_account(self):
        print("Account Created Successfully!")

    def make_deposite(self):
        amount = int(input("Enter amount to deposit: "))
        self.balance += amount
        print(amount, "rs Deposited.")
        print("Deposition Made")

    def make_withdrawal(self):
        amount = int(input("Enter amount to withdraw: "))
        if amount <= self.balance:
            self.balance -= amount
            print(amount, "rs Withdrawn.")
            print("Withdrawal Made")
        else:
            print("Insufficient Balance!")

    def check_balance(self):
        print("Your Balance is:", self.balance)


bank = Bank()

bank.create_account()
bank.make_deposite()
bank.make_withdrawal()
bank.check_balance()









class Bank:
    def __init__(self):
        self.accounts = {}     # Dictionary to store account_number: balance

    def create_account(self, acc_no):
        if acc_no in self.accounts:
            print("Account already exists!")
        else:
            self.accounts[acc_no] = 0
            print("Account created successfully!")

    def make_deposite(self, acc_no, amount):
        if acc_no in self.accounts:
            self.accounts[acc_no] += amount
            print("Amount deposited successfully!")
        else:
            print("Account not found!")

    def make_withdrawal(self, acc_no, amount):
        if acc_no in self.accounts:
            if self.accounts[acc_no] >= amount:
                self.accounts[acc_no] -= amount
                print("Withdrawal successful!")
            else:
                print("Insufficient balance!")
        else:
            print("Account not found!")

    def check_balance(self, acc_no):
        if acc_no in self.accounts:
            print("Current Balance:", self.accounts[acc_no])
        else:
            print("Account not found!")


# ---- Driver Code ----
bank = Bank()

bank.create_account(101)
bank.make_deposite(101, 5000)
bank.make_withdrawal(101, 1500)
bank.check_balance(101)
