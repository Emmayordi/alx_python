"""Improve Geometry

--------

This script requirea  Python
environment install where you are running this script in.

write an empty class

"""


class BaseGeometry:
    """
    A class defined

    -------

    def area(self): --> methods to return exception

    Raise:
    Exception with meassage
    """
    def __dir__(self):
        """
        define the function:

    parameters-->
    self -> no parameters
        """
        attributes = super().__dir__()
        new_attribute_list = [x for x in attributes if x != "__init_subclass__"]
        return new_attribute_list
    
    def area(self):
        """
        Function to raise exception
        """
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """
        Public instance method: def integer_validator(self, name, value): that validates value:
you can assume name is always a string
if value is not an integer: raise a TypeError exception, with the message <name> must be an integer
if value is less or equal to 0: raise a
ValueError exception with the message <name> must be greater than 0
        """
        if not isinstance(value, int):
            raise TypeError('{} must be an integer'.format(name))

        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
        
    
class Rectangle(BaseGeometry):
    """
    Write a class Rectangle that inherits from BaseGeometry (5-base_geometry.py).

    """
    def __init__(self, width, height):
        self.__width = self.integer_validator("width", width)
        self.__height = self.integer_validator("height", height)
        
    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
          
    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height
          
    def area(self):
        return self.__width * self.__height