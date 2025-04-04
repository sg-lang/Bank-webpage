#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask, request, jsonify

app = Flask(__name__)

class BankAccount:
    def __init__(self, account_number, account_name, balance=0):
        self.account_number = account_number
        self.account_name = account_name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited: {amount}. New Balance: {self.balance}"
        else:
            return "Deposit amount must be positive."

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return f"Withdrew: {amount}. New Balance: {self.balance}"
        else:
            return "Invalid withdrawal amount."

    def display_details(self):
        return f"Account Number: {self.account_number}, Account Name: {self.account_name}, Balance: {self.balance}"

class BankSystem:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, account_name):
        if account_number in self.accounts:
            return "Account already exists."
        else:
            new_account = BankAccount(account_number, account_name)
            self.accounts[account_number] = new_account
            return "Account created successfully."

    def transfer_funds(self, from_acc, to_acc, amount):
        if from_acc in self.accounts and to_acc in self.accounts:
            if self.accounts[from_acc].balance >= amount:
                self.accounts[from_acc].withdraw(amount)
                self.accounts[to_acc].deposit(amount)
                return "Transfer completed successfully."
            else:
                return "Insufficient funds."
        else:
            return "One or both accounts not found."

    def list_accounts(self):
        accounts_details = []
        for account in self.accounts.values():
            accounts_details.append(account.display_details())
        return accounts_details

# API Routes
@app.route("/")
def home():
    return "Welcome to the Banking System API! Use the appropriate endpoints to interact with the system."

@app.route("/create_account", methods=["POST"])
def create_account():
    data = request.get_json()
    return jsonify({"message": bank_system.create_account(data["account_number"], data["account_name"])})

@app.route("/deposit", methods=["POST"])
def deposit():
    data = request.get_json()
    account = bank_system.accounts.get(data["account_number"])
    if account:
        return jsonify({"message": account.deposit(data["amount"])})
    else:
        return jsonify({"message": "Account not found."}), 404

@app.route("/withdraw", methods=["POST"])
def withdraw():
    data = request.get_json()
    account = bank_system.accounts.get(data["account_number"])
    if account:
        return jsonify({"message": account.withdraw(data["amount"])})
    else:
        return jsonify({"message": "Account not found."}), 404

@app.route("/transfer", methods=["POST"])
def transfer():
    data = request.get_json()
    return jsonify({"message": bank_system.transfer_funds(data["from_account"], data["to_account"], data["amount"])})

@app.route("/accounts", methods=["GET"])
def accounts():
    return jsonify({"accounts": bank_system.list_accounts()})

if __name__ == "__main__":
    bank_system = BankSystem()
    app.run(debug=True, host="0.0.0.0", port=5000)


# In[ ]:




