def calculate_fibonacci(n):
    """Calculate the nth Fibonacci number."""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        print (a)
        for _ in range(2, n + 1):
            a, b = b, a + b
            print (b, end=' '   )
        return b