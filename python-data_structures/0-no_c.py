def no_c(my_string):
    result = ""
    for char in my_string:
        if char.lower() != 'c':
            result += char
    return result

# Test cases
print(no_c("Holberton School"))
print(no_c("Chicago"))
print(no_c("C is fun!"))
