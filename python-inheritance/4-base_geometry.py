#4-base_geometry.py
"""   
Improve Geometry geometry.
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
