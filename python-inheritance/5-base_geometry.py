"""
Defines a base geometry class BaseGeometry.
"""
class BaseGeometry:
    """
    A class representing the base geometry.
    """

    def area(self):
        """
        Public instance method that raises an Exception with the message "area() is not implemented".
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Public instance method that validates the value.

        Parameters:
        - name: str
            The name of the value.
        - value: int
            The value to validate.

        Raises:
        - TypeError: If value is not an integer.
        - ValueError: If value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

# Example usage:
if __name__ == "__main__":
    # Create an instance of the BaseGeometry class
    bg = BaseGeometry()

    # Test the integer_validator method
    bg.integer_validator("my_int", 12)
    bg.integer_validator("width", 89)

    try:
        bg.integer_validator("name", "John")
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        bg.integer_validator("age", 0)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        bg.integer_validator("distance", -4)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
