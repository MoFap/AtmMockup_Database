# register
# - first name,last name, password, email
# - generate user account
#

# login
# - account number and password

# bank operations


# Initializing the system

import random
import validation
import database
from getpass import getpass

account_number_of_user = None


def init():

    print("Welcome to bankOBA")

    have_account = int(input("Do you have an account with us: 1 (yes) 2 (no) \n"))

    if have_account == 1:

        login()
    elif have_account == 2:

        register()

    else:
        print("You have selected an invalid option")
        init()


def login():
    print("**** Login ****")

    global account_number_of_user
    account_number_of_user = input("What is your account number? \n")

    is_valid_account_number = validation.account_number_validation(account_number_of_user)

    if is_valid_account_number:

        password = getpass("What is your password \n")

        user = database.authenticated_user(account_number_of_user, password);

        if user:
            bank_operation(user)

        print('Invalid account or password')
        login()

    else:
        print("Account Number Invalid: check that you have up to 10 digits and only integers")
        init()


def register():
        print("*** Register ***")

        email = input("What is your email address? \n")
        first_name = input("What is your first name? \n")
        last_name = input("What is your last name? \n")
        # password = input("create a password for yourself \n")
        password = getpass("create a password for yourself \n")

        account_number = generation_account_number()

        is_user_created = database.create(account_number, first_name, last_name, email, password)

        if is_user_created:

            print("Your Account Has Been Created")
            print("Your account number is: %d" % account_number)
            print("Make sure to keep it safe")

            login()

        else:
            print("Something went wrong, please try again")
            register()



def bankOperation(user):
    print("Welcome %s %s " % (user[0], user[1]))

def bank_operation(user):
    print("Welcome %s %s " % (user[0], user[1]))

    selected_option = int(input("What would you like to do? (1) deposit (2) withdrawal (3) logout (4) exit \n"))

    if selected_option == 1:
        deposit_operation(user)

    elif selected_option == 2:
        withdrawal_operation(user)

    elif selected_option == 3:
        logout_operation()

    elif selected_option == 4:
        exit()
    else:

        print("Invalid option selected")
        bank_operation(user)

def deposit_operation(user):

    current_balance = int(get_current_balance(user))
    amount_to_deposit = int(input("How much do you want to deposit?"))
    current_balance += amount_to_deposit
    set_current_balance(user, str(current_balance))

    if database.update(account_number_of_user, user):
        print("Your account balance is {}".format(current_balance))
        bank_operation(user)


    else:
        print("Transaction not successful")
        bank_operation(user)


def withdrawal_operation(user):

    current_balance = int(get_current_balance(user))
    amount_to_withdraw = int(input("How much do you want to withdraw?"))
    current_balance -= amount_to_withdraw
    set_current_balance(user, str(current_balance))

    if database.update(account_number_of_user, user):
        print("Your account balance is {}".format(current_balance))
        bank_operation(user)



def generation_account_number():

    return random.randrange(1111111111, 9999999999)


def get_current_balance(user_details):
    return user_details[4]


def set_current_balance(user_details, balance):
    user_details[4] = balance


def logout_operation():
     login()

init()
