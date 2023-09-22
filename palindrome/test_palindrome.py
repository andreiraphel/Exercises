# test_palindrome.py
from palindrome import is_palindrome

def test_empty_string():
    assert is_palindrome("") == True

def test_single_character_string():
    assert is_palindrome("a") == True

def test_palindrome_strings():
    assert is_palindrome("racecar") == True
    assert is_palindrome("A man a plan a canal Panama") == True

def test_non_palindrome_strings():
    assert is_palindrome("hello") == False
    assert is_palindrome("Python") == False
    assert is_palindrome("not a palindrome") == False

def test_palindrome_strings_with_spaces():
    assert is_palindrome("race car") == True
    assert is_palindrome("Was it a car or a cat I saw") == True
