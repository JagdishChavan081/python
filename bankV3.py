"""
Implementation 3—Two Accounts
The version of the bank simulation program in Implementation-3 uses the same
approach as BankV2 but adds the ability to have two accounts.

Analysis of Required Operations and Data
A list of operations a person would want to do with a bank account would
include:
•	 Create (an account)
•	 Deposit
•	 Withdraw
•	 Check balance
Next, here is a minimal list of the data we would need to represent a
bank account:
•	 Customer name
•	 Password
•	 Balance"""
from typing import Any

# approach: procedural approach
# title: Bank Version 3
# implementation: Two account with Functions
# author: Jagdish_Chavan
# date: 14/7/2023

#account 0
account0Name = ''
account0Balance = 0
account0Password = ''

#account 1
account1Name = ''
account1Balance = 0
account1Password = ''

#functon1 to create new account
def newaccount(accountnumber: str, name: str, balance: int, password: int) -> None:
    """
    :param accountnumber: account number by bank
    :param name: name of customer
    :param balance: balance in bank
    :param password: account password
    :return: None
    """
    global account0Name, account0Balance, account0Password
    global account1Name, account1Balance, account1Password

    if accountnumber == 0:
        account0Name = name
        account0Balance = balance
        account0Password = password

    if accountnumber == 1:
        account1Name = name
        account1Balance = balance
        account1Password = password

#function2 to display details
def show():
    global account0Name, account0Balance, account0Password
    global account1Name, account1Balance, account1Password

    if account0Name != '':
        print('Account0')
        print('   Name: ',account0Name)
        print('   Balance: ',account0Balance)
        print('   Password:',account0Password)
        print()

    if account1Name != '':
        print('Account1')
        print('   Name: ', account1Name)
        print('   Balance: ', account1Balance)
        print('   Password:', account1Password)
        print()

#function3 get current balance
def getBalance(accountNumber: int, password: int) -> None | int:
    """

    :param accountNumber: account number of customer
    :param password: password of customer
    :return: None | Int
    """
    global account0Name, account0Balance, account0Password
    global account1Name, account1Balance, account1Password

    if accountNumber == 0:
        if password != account0Password:
            print('Incorrect password')
            return None
        return account0Balance

    if accountNumber == 1:
        if password != account1Password:
            print('Incorrect password')
            return None
        return account1Balance


#function4 deposit amount into account
def deposit(account_number: int, password: int, amount_d: int) -> None | int:
    """
    :param account_number: account number of customer
    :param password: password of customer
    :param amount_d: amount to deposit
    :return: None | int
    """
    global account0Name, account0Balance, account0Password
    global account1Name, account1Balance, account1Password

    #deposit in account =0
    if account_number == 0:
        if password != account0Password:
            print('Incorrect password')
            return None

    amount_d = int("Enter the amount you want to deposit")
    if amount_d < 0:
        print("enter valid amount")
        return None

    account0Balance = account0Balance + amount_d
    return account0Balance

    #deposit for account = 1
    if account_number == 1:
        if password != account1Password:
            print('Incorrect password')
            return None







