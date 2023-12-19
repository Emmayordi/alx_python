#4-base_geometry.py
"""   
Improve Geometry geometry.
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


if __name__ == "__main__":
    # Create an instance of the BaseGeometry class
    bg = BaseGeometry()

    # Test the area method
    try:
        print(bg.area())
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

