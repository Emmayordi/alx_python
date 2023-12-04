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
       
        if b % 2 == 1:
            result *= a
       
        a *= a
        b //= 2

    return result

print(pow(2, 2))     
print(pow(98, 2))    
print(pow(98, 0))    
print(pow(100, -2))  
print(pow(-4, 5))     
