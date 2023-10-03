# Import the BankAccount class from your implementation
import pytest
from Bank_account_class import Bank_account

# Define test cases using pytest
def test_initial_balance():
    # Create a BankAccount object with an initial balance
    account = Bank_account(1000, "Andrei")
    # Check that the initial balance is set correctly
    assert account.balance == 1000

def test_deposit():
    account = Bank_account(1000, "Andrei")
    # Deposit 500 into the account
    account.deposit(500)
    # Check that the balance has increased by 500
    assert account.balance == 1500

def test_withdraw():
    account = Bank_account(1000, "Andrei")
    # Withdraw 200 from the account
    account.withdraw(200)
    # Check that the balance has decreased by 200
    assert account.balance == 800

def test_insufficient_funds():
    account = Bank_account(100, "Andrei")
    # Try to withdraw 200, which should result in an insufficient funds error
    with pytest.raises(ValueError):
        account.withdraw(200)
