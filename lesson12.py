import os
from datetime import datetime
import smtplib
from email.message import EmailMessage

class Account:
    def __init__(self, full_name, acc_num, phone, balance, pin, email):
        self.full_name = full_name
        self.acc_num = acc_num
        self.phone = phone
        self.email = email
        self.pin = str(pin)  # Ensure the pin is stored as a string for easy comparison
        self.balance = balance
        self.transactions = []  # Initialize an empty list to store transaction history

    def validate_pin(self):
        entered_pin = input("Enter your PIN: ")
        if entered_pin == self.pin:
            return True
        else:
            print("Incorrect PIN.")
            return False

    def send_email_notification(self, subject, message, recipient_email):
        email = EmailMessage()
        email.set_content(message)
        email['Subject'] = subject
        email['From'] = os.environ.get("EMAIL_USER")  # Use the environment variable
        email['To'] = recipient_email

        # Connect to email server (e.g., Gmail)
        try:
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:  # Adjust based on your email provider
                smtp.login(os.environ.get("EMAIL_USER"), os.environ.get("EMAIL_PASSWORD"))  # Use environment variables for security
                smtp.send_message(email)
            print("Notification sent successfully.")
        except Exception as e:
            print("Error sending email:", e)

    def deposit(self, amount):
        # Check if account number is valid
        acc_num_input = input("Enter account number to confirm: ")
        if acc_num_input != self.acc_num:
            print("Account number does not match.")
            return

        # Proceed with deposit
        self.balance += amount
        transaction_time = datetime.now().strftime("%d/%m/%Y at %H:%M:%S")
        print(f"{amount} has been deposited to {self.full_name}'s account successfully on {transaction_time}. Your balance is {self.balance}")

        # Record the transaction
        self.transactions.append({
            "type": "Deposit",
            "amount": amount,
            "balance": self.balance,
            "datetime": transaction_time
        })

        # Send email notification using self.email
        self.send_email_notification(
            subject="Deposit Confirmation",
            message=f"Dear {self.full_name}, Ksh {amount} has been successfully deposited to your account. Your new balance is Ksh {self.balance}.",
            recipient_email=self.email
        )

    def withdraw(self, amount):
        if not self.validate_pin():
            return
        if self.balance < amount:
            print(f"Insufficient funds. Balance is {self.balance}.")
        else:
            self.balance -= amount
            transaction_time = datetime.now().strftime("%d/%m/%Y at %H:%M:%S")
            print(f"{amount} has been withdrawn successfully from {self.full_name}'s account on {transaction_time}. Your balance is {self.balance}.")
            # Record the transaction with date and time
            self.transactions.append({
                "type": "Withdrawal",
                "amount": amount,
                "balance": self.balance,
                "datetime": transaction_time
            })

    def transfer(self, amount, target_account):
        if not self.validate_pin():
            return
        if self.balance < amount:
            print(f"Insufficient funds. Balance is {self.balance}.")
        else:
            self.balance -= amount
            target_account.balance += amount
            transaction_time = datetime.now().strftime("%d/%m/%Y at %H:%M:%S")
            print(f"Transfer Successful! You have sent Ksh {amount} to {target_account.full_name} on {transaction_time}. Your new balance is Ksh {self.balance}.")
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
        if self.validate_pin():
            print(f"Your balance is {self.balance}.")

    def show_transactions(self):
        if self.validate_pin():
            print(f"Transaction history for {self.full_name}:")
            for transaction in self.transactions:
                if transaction["type"] == "Transfer Out":
                    print(f"{transaction['datetime']}: Transferred {transaction['amount']} to {transaction['to']}. Balance: {transaction['balance']}")
                elif transaction["type"] == "Transfer In":
                    print(f"{transaction['datetime']}: Received {transaction['amount']} from {transaction['from']}. Balance: {transaction['balance']}")
                else:
                    print(f"{transaction['datetime']}: {transaction['type']} of {transaction['amount']}. Balance: {transaction['balance']}")

# Example usage
if __name__ == "__main__":
    # Replace the below variables with your actual email and password
    os.environ["EMAIL_USER"] = "rodgerstarrodgers@gmail.com"
    os.environ["EMAIL_PASSWORD"] = "37519223Bad"

    kevo_acc = Account("Kevo", "50000", "07000100190", 10000, 1234, "kevo@example.com")
    kel_acc = Account("Kel", "4999", "07878700190", 17000, 6789, "kel@example.com")

    # Test a deposit
    kevo_acc.deposit(3000)

    # Uncomment the lines below to test other functionalities
    # kevo_acc.withdraw(500)
    # kevo_acc.transfer(2000, kel_acc)
    # kevo_acc.check_balance()
    # kevo_acc.show_transactions()
