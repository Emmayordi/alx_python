"""
Defines a Rectangle subclass Square.
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


class Rectangle(BaseGeometry):
    """
    A class representing a rectangle, inheriting from BaseGeometry.
    """

    def __init__(self, width, height):
        """
        Constructor for the Rectangle class.

        Parameters:
        - width: int
            The width of the rectangle.
        - height: int
            The height of the rectangle.
        """
  
