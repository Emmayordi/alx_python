def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius
temperature_fahrenheit = 32  # Replace this with the Fahrenheit temperature you want to convert
temperature_celsius = convert_to_celsius(temperature_fahrenheit)
print(f"{temperature_fahrenheit} Fahrenheit is {temperature_celsius:.2f} Celsius")
