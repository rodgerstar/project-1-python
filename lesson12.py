from datetime import datetime


class Account:
    def __init__(self, full_name, acc_num, phone, balance, pin):
        self.full_name = full_name
        self.acc_num = acc_num
        self.phone = phone
        self.pin = pin
        self.balance = balance

        self.transactions = []  # Initialize an empty list to store transaction history

    def deposit(self, amount):
        self.balance += amount
        transaction_time = datetime.now().strftime("%d/%m/%Y at %H:%M:%S")
        print(
            f"{amount} has been deposited to {self.full_name}'s account successfully on {transaction_time}. Your balance is {self.balance}")

        # Record the transaction with date and time
        self.transactions.append({
            "type": "Deposit",
            "amount": amount,
            "balance": self.balance,
            "datetime": transaction_time
        })

    def withdraw(self, amount, pin):
        if pin != self.pin:
            print("entered wrong pin")
            return
        if self.balance < amount:
            print(f"Insufficient funds. Balance is {self.balance}.")
        else:
            self.balance -= amount
            transaction_time = datetime.now().strftime("%d/%m/%Y at %H:%M:%S")
            print(
                f"{amount} has been withdrawn successfully from {self.full_name}'s account on {transaction_time}. Your balance is {self.balance}.")

            # Record the transaction with date and time
            self.transactions.append({
                "type": "Withdrawal",
                "amount": amount,
                "balance": self.balance,
                "datetime": transaction_time
            })

    def transfer(self, amount, target_account, pin):
        if pin != self.pin:
            print("entered wrong pin")
            return
        if self.balance < amount:
            print(f"Insufficient funds. Balance is {self.balance}.")
        else:
            self.balance -= amount
            target_account.balance += amount
            transaction_time = datetime.now().strftime("%d/%m/%Y at %H:%M:%S")
            print(
                f"Transfer Successful! You have sent Ksh {amount} to {target_account.full_name} on {transaction_time}. Your new balance is Ksh {self.balance}.")


            # Record the transaction for sender with date and time
            self.transactions.append({
                "type": "Transfer Out",
                "amount": amount,
                "balance": self.balance,
                "to": target_account.full_name,
                "datetime": transaction_time
            })
            # Record the transaction for recipient with date and time
            target_account.transactions.append({
                "type": "Transfer In",
                "amount": amount,
                "balance": target_account.balance,
                "from": self.full_name,
                "datetime": transaction_time
            })

    def check_balance(self):
        print(f"Your balance is {self.balance}.")

    def show_transactions(self):
        print(f"Transaction history for {self.full_name}:")
        for transaction in self.transactions:
            if transaction["type"] == "Transfer Out":
                print(
                    f"{transaction['datetime']}: Transferred {transaction['amount']} to {transaction['to']}. Balance: {transaction['balance']}")
            elif transaction["type"] == "Transfer In":
                print(
                    f"{transaction['datetime']}: Received {transaction['amount']} from {transaction['from']}. Balance: {transaction['balance']}")
            else:
                print(
                    f"{transaction['datetime']}: {transaction['type']} of {transaction['amount']}. Balance: {transaction['balance']}")


kevo_acc = Account("Kevo", "50000", "07000100190", 10000, 1234)
kel_acc = Account("kel", "4999", "07878700190", 17000, 6789)



#kevo_acc.deposit(1000)
#kevo_acc.check_balance()
#kevo_acc.withdraw(4000)
#kevo_acc.check_balance()

#kel_acc.deposit(5000)
kevo_acc.transfer(5000, kel_acc, 1234)
#kel_acc.check_balance()
#kel_acc.check_balance()
#kel_acc.transfer(12000, kevo_acc)
#kevo_acc.check_balance()
#kel_acc.show_transactions()
#kel_acc.deposit(7000)
