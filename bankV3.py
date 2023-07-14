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
    pass
