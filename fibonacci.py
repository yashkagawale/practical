def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

if __name__ == "__main__":
    num = int(input("Enter the number of Fibonacci terms: "))
    if num <= 0:
        print("Please enter a positive number!")
    else:
        print(f"The first {num} Fibonacci numbers are: {fibonacci(num)}")
