def pow(a, b):
   
    if b == 0:
        return 1
    
   
    if b == 1:
        return a
    
    
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

result = pow(2, 3)
print(result)  
