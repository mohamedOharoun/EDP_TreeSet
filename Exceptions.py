class ClassCastException(Exception):
    """
    Exception raised when an attempt is made to compare elements of incompatible types.
    """
    def __init__(self, type):
        """
        Initializes the ClassCastException.
        
        Args:
            type (type): The type of the element causing the exception.
        """
        self.type = type
        self.message = f"class {type.__name__} is not comparable"
        super().__init__(self.message)

class NoSuchElementException(Exception):
    """
    Exception raised when attempting to access an element that does not exist.
    """
    pass

class NullPointerException(Exception):
    """
    Exception raised when attempting to use a null reference.
    """
    pass