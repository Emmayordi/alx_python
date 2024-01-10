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
        Public instance method: def integer_validator(self, name, value)
        """
        if not isinstance(value, int):
            raise TypeError('{} must be an integer'.format(name))

        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
        
    
class Rectangle(BaseGeometry):
    """
    Write a class Rectangle that inherits from BaseGeometry (5-base_geometry.py).

Instantiation with width and height: def __init__(self, width, height):
width and height must be private. No getter or setter
width and height must be positive integers, validated by integer_validator
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
    
class Rectangle(BaseGeometry):
    """
    Instantiation with width and height: def __init__(self, width, height)::
width and height must be private. No getter or setter
width and height must be positive integers validated by integer_validator
    """
    def __init__(self, width, height):
        self.__width = self.integer_validator("width", width)
        self.__height = self.integer_validator("height", height)
        
    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        return self.__width * self.__height