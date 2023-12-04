def convert_to_celsius(fahrenheit):
    # Convert Fahrenheit to Celsius using the formula: (F - 32) * 5/9
    celsius = (fahrenheit - 32) * 5/9
    # Round the result to 14 decimal places to match the expected output
    rounded_celsius = round(celsius, 14)
    return rounded_celsius

# Example usage:
print(convert_to_celsius(100))    # Output: 37.77777777777778
print(convert_to_celsius(-40))    # Output: -40.0
print(convert_to_celsius(-459.67))# Output: -273.15
print(convert_to_celsius(32))     # Output: 0.0
