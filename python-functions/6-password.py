def validate_password(password):
    # Check the length of the password
    if len(password) < 8:
        return False

    # Check for at least one uppercase letter, one lowercase letter, and one digit
    has_upper = False
    has_lower = False
    has_digit = False

    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True

    if not (has_upper and has_lower and has_digit):
        return False

    # Check if the password contains spaces
    if ' ' in password:
        return False

    # If all checks pass, return True
    return True


password = "SecureP@ss123"
result = validate_password(password)
print(result)
