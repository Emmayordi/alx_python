"""
Defines a class and inherited class-checking function.
"""
def inherits_from(obj, a_class):
    """
    Check if obj is an instance of a class that inherited (directly or indirectly) from the specified class.

    Parameters:
    - obj: Any
        The object to check.
    - a_class: class
        The class to compare against.

    Returns:
    - bool
        True if obj is an instance of a class that inherited from a_class; otherwise, False.
    """
    return issubclass(type(obj), a_class)

# Test cases
if __name__ == "__main__":
    a = True
    if inherits_from(a, int):
        print("{} inherited from class {}".format(a, int.__name__))
    if inherits_from(a, bool):
        print("{} inherited from class {}".format(a, bool.__name__))
    if inherits_from(a, object):
        print("{} inherited from class {}".format(a, object.__name__))
