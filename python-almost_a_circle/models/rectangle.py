#!/usr/bin/python3
""" Rectangle module """
from models.base import Base

class Rectangle(Base):
    """ Rectangle class, inherits from Base """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Constructor method """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ Getter for width """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter for width """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ Getter for height """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter for height """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """ Getter for x """
        return self.__x

    @x.setter
    def x(self, value):
        """ Setter for x """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """ Getter for y """
        return self.__y

    @y.setter
    def y(self, value):
        """ Setter for y """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """ Calculate the area of the Rectangle """
        return self.__width * self.__height

    def display(self):
        """ Display the Rectangle using '#' character with x and y offset """
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """ Return the string representation of the Rectangle """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """ Update the Rectangle attributes with key-worded arguments """
        attr_list = ['id', 'width', 'height', 'x', 'y']
        if args:
            for i in range(len(args)):
                setattr(self, attr_list[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

if __name__ == "__main__":
    r1 = Rectangle(10, 10, 10, 10)
    print(r1)

    r1.update(height=1)
    print(r1)

    r1.update(width=1, x=2)
    print(r1)

    r1.update(y=1, width=2, x=3, id=89)
    print(r1)

    r1.update(x=1, height=2, y=3, width=4)
    print(r1)
