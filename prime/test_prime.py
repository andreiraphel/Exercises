# test_prime_checker.py
from prime import is_prime

def test_prime_numbers():
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(5) == True
    assert is_prime(7) == True
    assert is_prime(11) == True
    assert is_prime(13) == True
    assert is_prime(17) == True

def test_non_prime_numbers():
    assert is_prime(1) == False
    assert is_prime(4) == False
    assert is_prime(6) == False
    assert is_prime(9) == False
    assert is_prime(15) == False
    assert is_prime(25) == False
    assert is_prime(100) == False
