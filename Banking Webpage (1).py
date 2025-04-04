#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class BankAccount:
    def __init__(self, account_number, account_name, balance=0):
        self.account_number = account_number
        self.account_name = account_name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: {amount}. New Balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew: {amount}. New Balance: {self.balance}")
        else:
            print("Invalid withdrawal amount.")

    def display_details(self):
        print(f"Account Number: {self.account_number}, Account Name: {self.account_name}, Balance: {self.balance}")

class BankSystem:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, account_name):
        if account_number in self.accounts:
            print("Account already exists.")
        else:
            new_account = BankAccount(account_number, account_name)
            self.accounts[account_number] = new_account
            print("Account created successfully.")

    def transfer_funds(self, from_acc, to_acc, amount):
        if from_acc in self.accounts and to_acc in self.accounts:
            if self.accounts[from_acc].balance >= amount:
                self.accounts[from_acc].withdraw(amount)
                self.accounts[to_acc].deposit(amount)
                print("Transfer completed successfully.")
            else:
                print("Insufficient funds.")
        else:
            print("One or both accounts not found.")

    def list_accounts(self):
        for account in self.accounts.values():
            account.display_details()

def main():
    bank_system = BankSystem()
    while True:
        print("\nBanking System Menu:")
        print("1. Create New Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transfer Funds")
        print("5. Display Account Details")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            acc_num = input("Enter account number: ")
            acc_name = input("Enter account holder name: ")
            bank_system.create_account(acc_num, acc_name)
        elif choice == '2':
            acc_num = input("Enter account number: ")
            amount = float(input("Enter amount to deposit: "))
            if acc_num in bank_system.accounts:
                bank_system.accounts[acc_num].deposit(amount)
            else:
                print("Account not found.")
        elif choice == '3':
            acc_num = input("Enter account number: ")
            amount = float(input("Enter amount to withdraw: "))
            if acc_num in bank_system.accounts:
                bank_system.accounts[acc_num].withdraw(amount)
            else:
                print("Account not found.")
        elif choice == '4':
            from_acc = input("Enter from account number: ")
            to_acc = input("Enter to account number: ")
            amount = float(input("Enter transfer amount: "))
            bank_system.transfer_funds(from_acc, to_acc, amount)
        elif choice == '5':
            bank_system.list_accounts()
        elif choice == '6':
            print("Exiting system.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()


# In[ ]:




