def pow(a, b):
    # Base case: when exponent is 0, result is 1
    if b == 0:
        return 1
    
    # If exponent is negative, compute reciprocal
    if b < 0:
        a = 1 / a
        b = -b

    result = 1
    while b > 0:
        # If exponent is odd, multiply result with base
        if b % 2 == 1:
            result *= a
        # Square the base and halve the exponent
        a *= a
        b //= 2

    return result

# Example usage:
print(pow(2, 2))     # Output: 4
print(pow(98, 2))    # Output: 9604
print(pow(98, 0))    # Output: 1
print(pow(100, -2))  # Output: 0.0001
print(pow(-4, 5))     # Output: -1024
