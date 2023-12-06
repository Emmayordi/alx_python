def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Division by zero is not allowed")
        return None
    except Exception as e:
        print("An error occurred:", e)
        return None
    else:
        print("Inside result: {}".format(result))
        return result
    finally:
        print("Inside finally clause")

# Example usage:
a = 10
b = 2
result = safe_print_division(a, b)
