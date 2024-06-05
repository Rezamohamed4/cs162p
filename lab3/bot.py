
import sys

def factorial1(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

def factorial2(n):
    if n == 0:
        return 1
    else:
        return n * factorial2(n-1)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python lab3a.py <method> <integer>")
    else:
        method = sys.argv[1]
        num = int(sys.argv[2])

        if method == "iterative":
            result = factorial1(num)
            print(f"Factorial of {num} using iterative approach is: {result}")
        elif method == "recursive":
            result = factorial2(num)
            print(f"Factorial of {num} using recursive approach is: {result}")
        else:
            print("Invalid method. Please use 'iterative' or 'recursive'.")