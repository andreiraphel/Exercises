
class Bank_account:
    def __init__(self, balance, account_holder) -> None:
        self.account_holder = account_holder
        self.balance = balance

    def __str__(self) -> str:
        return(f"\nAccount holder: {self.account_holder}\nBalance: ${self.balance}\n")

    def deposit(self, n) -> None:
        self.balance += n

    def withdraw(self, n) -> None:
        if self.balance - n < 0:
            raise ValueError
        else:
            self.balance -= n

def main():
    while True:
        user_input = int(input("1. New Account\n2. Existing Account\n"))
        if user_input == 1 or user_input == 2:
            if user_input == 1:
                new_account()
            else:
                existing_account()
            break
        else:
            pass

def new_account():
    name = input("Name: ")
    amount = int(input("Initial deposit: "))
    bank = Bank_account(amount, name)
    print(bank)

def existing_account():
    bank = Bank_account(2500, "Andrei Amang")
    print(bank)
    while True:
        user_input = input("1. Withdraw\n2. Deposit\n")
        if user_input == "1" or user_input == "2":
            if user_input == "1":
                amount = int(input("Amount: "))
                bank.withdraw(amount)
                print(bank)
                break
            elif user_input == "2":
                amount = int(input("Amount: "))
                bank.deposit(amount)
                print(bank)
                break
        else:
            pass

if __name__ == "__main__":
    main()