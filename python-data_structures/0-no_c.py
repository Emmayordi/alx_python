def no_c(my_string):
    # Create an empty string to build the new string
    new_string = ""
    
    # Loop through each character in the original string
    for char in my_string:
        # Only add the character to the new string if it is not 'c' or 'C'
        if char != 'c' and char != 'C':
            new_string += char
            
    # Return the new string
    return new_string

if __name__ == "__main__":
    print(end="")