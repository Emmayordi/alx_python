def raise_exception_msg(message="c is fun"):
    raise NameError(message)


try:
    raise_exception_msg("python is cool")
except NameError as e:
    print("Caught a name exception:", e)
