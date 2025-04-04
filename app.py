#!/usr/bin/env python
# coding: utf-8

# In[ ]:

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to the Bank Webpage!'

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, request, jsonify

app = Flask(__name__)

# Simulated database (a simple dictionary for this example)
accounts = {}

# Create New Account
@app.route('/create_account', methods=['POST'])
def create_account():
    data = request.get_json()
    account_number = data.get('account_number')
    if account_number in accounts:
        return jsonify({"error": "Account already exists."}), 400
    accounts[account_number] = {
        'balance': 0,
        'account_holder': data.get('account_holder', '')
    }
    return jsonify({"message": "Account created successfully!"}), 201

# Deposit Money
@app.route('/deposit', methods=['POST'])
def deposit():
    data = request.get_json()
    account_number = data.get('account_number')
    amount = data.get('amount')
    
    if account_number not in accounts:
        return jsonify({"error": "Account not found."}), 404

    accounts[account_number]['balance'] += amount
    return jsonify({"message": f"${amount} deposited successfully!"}), 200

# Withdraw Money
@app.route('/withdraw', methods=['POST'])
def withdraw():
    data = request.get_json()
    account_number = data.get('account_number')
    amount = data.get('amount')
    
    if account_number not in accounts:
        return jsonify({"error": "Account not found."}), 404

    if accounts[account_number]['balance'] < amount:
        return jsonify({"error": "Insufficient funds."}), 400

    accounts[account_number]['balance'] -= amount
    return jsonify({"message": f"${amount} withdrawn successfully!"}), 200

# Transfer Funds
@app.route('/transfer', methods=['POST'])
def transfer():
    data = request.get_json()
    from_account = data.get('from_account')
    to_account = data.get('to_account')
    amount = data.get('amount')
    
    if from_account not in accounts or to_account not in accounts:
        return jsonify({"error": "One or both accounts not found."}), 404

    if accounts[from_account]['balance'] < amount:
        return jsonify({"error": "Insufficient funds."}), 400

    accounts[from_account]['balance'] -= amount
    accounts[to_account]['balance'] += amount
    return jsonify({"message": f"${amount} transferred successfully!"}), 200

# Display Account Details
@app.route('/account_details/<account_number>', methods=['GET'])
def account_details(account_number):
    if account_number not in accounts:
        return jsonify({"error": "Account not found."}), 404
    
    account = accounts[account_number]
    return jsonify({
        "account_holder": account['account_holder'],
        "balance": account['balance']
    }), 200

if __name__ == '__main__':
    import os

port = os.environ.get('PORT', 5000)  # Get the port from environment or default to 5000
app.run(host='0.0.0.0', port=port, debug=True)




# In[ ]:




