def main():
    while True:
        user_input = input("String: ")
      #  print(user_input)
        print(is_palindrome(user_input))
        break

def is_palindrome(s):
    s = s.replace(" ", "").lower()
    if s == s[::-1]:
        return True
    else:
        return False


if __name__ == "__main__":
    main()