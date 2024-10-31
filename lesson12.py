class Account:
    def __init__(self, full_name, acc_num, phone, balance):
        self.full_name = full_name
        self.acc_num = acc_num
        self.phone = phone
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} has been deposited to {self.full_name} account successfully. Your balance is {self.balance}")

    def withdraw(self, amount):
        if self.balance < amount:
            print(f"Insufficient funds. Balance is {self.balance}.")
        else:
            self.balance -= amount
            print(f"{amount} has been withdrawn successfully from  account {self.acc_num} your balance is {self.balance}.")

    def check_balance(self):
        print(f"Your balance is {self.balance}.")


kevo_acc = Account("Kevo", "50000", "07000100190", 10000)
kel_acc = Account("kel", "4999", "07878700190", 17000)

kevo_acc.deposit(1000)
kevo_acc.check_balance()
kevo_acc.withdraw(4000)
kevo_acc.check_balance()

kel_acc.deposit(5000)
kel_acc.check_balance()