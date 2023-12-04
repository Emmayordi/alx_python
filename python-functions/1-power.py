def custom_pow(base, exponent):
    
    if exponent == 0:
        return 1
    
    
    if exponent < 0:
        base = 1 / base
        exponent = -exponent

    result = 1
    while exponent > 0:
        
        if exponent % 2 == 1:
            result *= base
        
        base *= base
        exponent //= 2

    return result


print(custom_pow(2, 2))     
print(custom_pow(98, 2))    
print(custom_pow(98, 0))    
print(custom_pow(100, -2))  
print(custom_pow(-4, 5))     
