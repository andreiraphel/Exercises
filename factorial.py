def main():
    while True:
        try:
            user_input = int(input("N: "))
            print(factorial(user_input))
            break
        except:
            pass

def factorial(n):
    if n < 0:
        raise ValueError
    elif n == 0:
        return 1
    else:
        return n * factorial(n-1)

if __name__ == "__main__":
    main()