"""
This module provides a function to check if an object is exactly an instance of a specified class.
"""

def is_same_class(obj, a_class):
    """
    Check if obj is exactly an instance of a_class.

    Parameters:
    - obj: Any
        The object to check.
    - a_class: class
        The class to compare against.

    Returns:
    - bool
        True if obj is exactly an instance of a_class; otherwise, False.
    """

    return type(obj) is a_class

# Test cases
if __name__ == "__main__":
    a = 1
    if is_same_class(a, int):
        print("{} is an instance of the class {}".format(a, int.__name__))
    if is_same_class(a, float):
        print("{} is an instance of the class {}".format(a, float.__name__))
    if is_same_class(a, object):
        print("{} is an instance of the class {}".format(a, object.__name__))
