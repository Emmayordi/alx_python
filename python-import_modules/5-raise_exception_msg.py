def raise_exception_msg(message=""):
    raise NameError(message)

# Example usage:
try:
    raise_exception_msg("Python is cool\nC is fun")
except NameError as e:
    print("Caught a name exception:", e)
