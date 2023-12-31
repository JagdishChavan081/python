# approach: procedural approach
# title: Bank Version 1
"""Analysis of Required Operations and Data
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
# implementation: Single_account Without Functions
# author: Jagdish_Chavan
# date:13/7/2023

accountName = 'Jagdish'
accountBalance = 100
accountPassword = '1234'

while True:
    print()
    print('Press b to get the balance')
    print('Press d to make a deposit')
    print('Press w to make withdrawal')
    print('Press s to show the account')
    print('Press q to quit')
    print()

    action = input('What do you want to do?')
    action = action.lower()
    action = action[0]
    print()

    if action == 'b':
        print('Get the Balance')
        userPassword = input('Please enter the password: ')
        if userPassword != accountPassword:
            print('Incorrect password')
        else:
            print('Your balance is:', accountBalance)

    elif action == 'd':
        print('Deposit:')
        userDepositAmount = input('Please enter the amount: ')
        userDepositAmount = int(userDepositAmount)
        userPassword = input("Please enter the password: ")

        if userDepositAmount < 0:
            print('You cannot deposit a negative amount')

        elif userPassword != accountPassword:
            print('Incorrect password')

        else:  # ok
            accountBalance = accountBalance + userDepositAmount
            print('Your new Balance is:', accountBalance)

    elif action == 's':
        print('show')
        print(" Name:", accountName)
        print(" Balance:", accountBalance)
        print(" Password", accountPassword)
        print()

    elif action == 'q':
        break

    elif action == 'w':
        print('Withdraw:')

        userWithdrawAmount = input('Please enter the amount to withdraw: ')
        userWithdrawAmount = int(userWithdrawAmount)
        userPassword = input('Please enter the password: ')

        if userWithdrawAmount < 0:
            print('You cannot withdraw a negative amount')

        elif userPassword != accountPassword:
            print('Incorrect password for this account')

        elif userWithdrawAmount > accountBalance:
            print('You cannot withdraw more than you have in your account')

        else:
            accountBalance = accountBalance - userWithdrawAmount
            print('Your new balance is:', accountBalance)

print('Done')