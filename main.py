from flask import Flask, render_template, request, redirect, url_for, flash

accounts= {
  #Database of accounts
}



#create function for each option
""" create User Account
      Ask User to provide:
        -Name
        -Birthdate
        -Email address
        -Password (6 characters minimum, at least one digit and one symbol)
        -Security Question

      Delete User Account
      Ask User to provide:
        -Email address
        -Password (6 characters minimum, at least one digit and one symbol)
        -Security Question answer
        -send farewell message

      Depositing Funds
      Ask User to provide:
        -Deposit Amount
        -Account Address
        -Username
        -Password

      Withdraw Funds
      Ask User to provide:
        -Withdraw Amount
        -Password
      
      Modify Account Details
      Ask User to provide:
        -Username
        -Password
        -New Username and or New Password
        - Give response of updated Account details
      
        
        
        
  """
def create_account():
  account_number = request.form.get('account_number')
  initial_balance = request.form.get('initial_balance')
  if account_number not in accounts: 
    accounts[account_number] = initial_balance
    flash(f"Account {account_number} created successfully!")
  else: 
    flash(f'Account {account_number} already exists.')


#Account balance
def account_balance():
  account_balance = request.form.get('account_number')
  if account_balance in accounts:
    balance = accounts[account_balance]
    flash(f"Your account balance is {balance}")
  else:
    flash(f"Account {account_balance} not found.")

  
 
#Withdraw fund
def Withdraw_amount():
  account_number = request.form.get('account_number')amount_str = request.form.get('amount')
  
  if amount_str is not None:
    amount = float(amount_str)
    if account_number in accounts: 
        if accounts[account_number] >= amount:
            accounts[account_number] -= amount
            flash(f"Withdrawal of {amount} successful. Your new balance is {accounts[account_number]}")
        else:
            flash("Insufficient funds.")
    else:
        flash(f'Account {account_number} not found.')
  else:
    flash("Amount is missing in the form data.")


#deposite money
def deposit():
  account_number = request.form.get('account_number')
  amount = float(request.form.get('amount'))
  if account_number in accounts: 
    accounts[account_number] += amount
    flash(f"Deposit of {amount} successful. Your new balance is {accounts[account_number]}")
  else:
    flash(f'Account {account_number} not found.')
  
 
#delete user_account
def delete_account():
  account_number = request.form.get('account_number')
  if account_number in accounts:
    del accounts[account_number]
    flash(f'Acccount {account_number} deleted successfully!')
  else:
    flash(f'Account {account_number} does not exist!')
    







