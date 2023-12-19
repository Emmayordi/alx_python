class Square:
    def __init__(self, size):
        self.__size = size  # Private attribute

    def get_size(self):
        return self.__size

    def set_size(self, new_size):
        # Add validation logic here if needed
        self.__size = new_size
