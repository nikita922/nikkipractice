def fibonacci(n):
    if n <= 0:
        return []
    if n == 1:
        return [0]
    if n == 2:
        return [0, 1]
    fib = fibonacci(n - 1)
    fib.append(fib[-1] + fib[-2])
    return fib

n = 12
fib_series = fibonacci(n)
print(f"Fibonacci series of {n} numbers: {fib_series}")
