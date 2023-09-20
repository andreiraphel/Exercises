import sys

def fibonacci_generator(n):
    a = 0
    b = 1
    fibonacci = []

    if n == 1:
        fibonacci.append(a)
        return fibonacci
    else:
        fibonacci = [a, b]
        for i in range(2, n):
            c = a+b
            fibonacci.append(c)
            a = b
            b = c
        return fibonacci
            

def main():
    while True:
        try:
            user_input = int(input("How many fibonacci sequence: "))
            break
        except ValueError:
            pass
    print(fibonacci_generator(user_input))

if __name__ == "__main__":
    main()