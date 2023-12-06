def raise_exception_msg(message=""):
    raise NameError(message)

# Example usage:
try:
    raise_exception_msg("Python is cool\nC is fun")
except NameError as e:
    lines = str(e).split('\n')
    if len(lines) >= 2:
        print(lines[1])
    else:
        print("No valid message found in the exception")
