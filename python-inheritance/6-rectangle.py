"""
Defines a class Rectangle that inherits from BaseGeometry.
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
        super().__init__()
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """
        String representation of the rectangle.

        Returns:
        - str
            The rectangle description in the format [Rectangle] <width>/<height>.
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        """
        Compute the area of the rectangle.

        Returns:
        - int
            The area of the rectangle.
        """
        return self.__width * self.__height


# Example usage:
if __name__ == "__main__":
    # Create an instance of the Rectangle class
    r = Rectangle(3, 5)

    # Test the string representation and area method
    print(r)
    print(r.area())
