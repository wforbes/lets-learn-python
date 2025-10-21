import numbers

class BankAccount:
    def __init__(self, beginBal):
        self.balance = beginBal

    def deposit(amt):
        balance += amt

    def withdraw(amt):
        balance -= amt

def print_balance(account):
    print(f"account balance: ${account.balance:.2f}")

def print_choices():
    print("What would you like to do?")
    print("1 - deposit funds")
    print("2 - withdraw funds")
    print("3 - exit")

def handle_deposit(account):
    print("Depositing Funds")
    amt = float(input("Enter amount to deposit: "))
    if isinstance(amt, numbers.Number):
        account.deposit(amt)
    else:
        print("error: you must enter a number")

def handle_withdrawl(account):
    print("Withdrawing Funds")
    amt = float(input("Enter amount to withdraw: "))
    if not isinstance(amt, numbers.Number):
        print("error: you must enter a number")
        return
    if account.balance - amt < 0:
        print("error: insufficient funds")
        return

    account.withdraw(amt)
    print(f"Withdrew ${amt} from account")
    print(f"New balance: ${account.balance}")

def run():
    running = True
    account = BankAccount(100.00)
    while running:
        print_balance(account)
        print_choices()
        
        usr_input = input("Choice: ")
        if (usr_input == "1"):
            handle_deposit(account)
        elif(usr_input == "2"):
            handle_withdrawl(account)
        elif (usr_input == "3"):
            running = False
    print("Goodbyeeeeee")

run()
