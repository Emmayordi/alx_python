def reverse_string(string):
    # Using string slicing to reverse the string
    reversed_str = string[::-1]
    return reversed_str

# Example usage:
input_str = "Hello, World!"
result = reverse_string(input_str)
print(result)
