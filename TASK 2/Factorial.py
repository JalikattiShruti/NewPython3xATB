def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Calculate factorial of 5
print(factorial(5))  # Output: 120 = 5x4x3x2x1

