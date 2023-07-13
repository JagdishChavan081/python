"""In this version of the program in Listing bankV2, the code is broken up into
separate functions, one for each action. Again, this simulation is for a single
account.

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
# title: Bank Version 2
# implementation: Single_account Without Functions
# author: Jagdish_Chavan
# date: 13/7/2023

accountName = ''
accountBalance = 0
accountPassword = ''


# function1 to create new account
def new_account(name: str, balance: int, password: str) -> None:
    """
    :rtype: None
    :param name:name of account holder
    :param balance: initial balance
    :param password: initial password
    :return: None
    """
    global accountName, accountBalance, accountPassword
    accountName = name
    accountPassword = password
    accountBalance = balance


# function2 to display account holder details
def show():
    """
    :return:details of account holder like name balance and password
    """
    global accountName, accountBalance, accountPassword
    print(' Name:', accountName)
    print(' Balance:', accountBalance)
    print(' Password:', accountPassword)
    print()


# function3 to check available balance
def getbalance(password) -> int:
    global accountName, accountBalance, accountPassword
    if password != accountPassword:
        print('Incorrect password')
    return accountBalance


# function4 to deposit the amount
def deposit(amount: int, password: str) -> None | int:
    """
    :param amount: amount user want to deposit
    :param password: user password
    :return: new available balance after deposit
    """
    global accountName, accountBalance, accountPassword
    if amount < 0:
        print('You cannot deposit a negative amount')
        return None

    if password != accountPassword:
        print('Incorrect password')
        return None

    accountBalance = accountBalance + amount
    return accountBalance

#function5 to withdraw amount from account
def withdraw(withdrawamount: int, password: str) -> None | int:
    """
    :param withdrawamount: amount that need to be withdrawn
    :param password: user password
    :return: None | int
    """
    global accountName, accountBalance, accountPassword
    if withdrawamount < 0:
        print('You cannot withdraw a negative amount')
        return None

    if password != accountPassword:
        print('Incorrect password for this account')
        return None

    if withdrawamount > accountBalance:
        print('You cannot withdraw more than you have in your account')
        return None

    accountBalance = accountBalance - withdrawamount
    return accountBalance


#create an account
new_account("Jagdish", 100, '1234')

while True:
    print()
    print('Press b to get the balance')
    print('press d to make a deposit')
    print('press w to make withdrawal')
    print('press s to show the account')
    print('press q to quit')
    print()

    action = input('What do you want to do? ')
    action = action.lower()
    action = action[0]
    print()

    #
    if action == 'b':
        print('Get Balance:')
        userPassword = input('Please enter the password: ')
        theBalance = getbalance(userPassword)
        if theBalance is not None:
            print('Your balance is:', theBalance)

    elif action == 'd':
        print('Deposit:')
        userDepositAmount = input('Please enter amount to deposit: ')
        userDepositAmount = int(userDepositAmount)
        userPassword = input('Please enter the password: ')

        newBalance = deposit(userDepositAmount, userPassword)
        if newBalance is not None:
            print('Your new balance is: ', newBalance)

    elif action == 'w':
        print('Withdraw: ')
        userWithdrawAmount = input('Please enter amount to withdraw: ')
        userWithdrawAmount = int(userWithdrawAmount)
        userPassword = input('Please enter the password: ')

        newBalance = withdraw(userWithdrawAmount, userPassword)
        if newBalance is not None:
            print('Your new balance is: ', newBalance)

    elif action == 's':
        print(show())

    elif action == 'q':
        break

print('Done')
