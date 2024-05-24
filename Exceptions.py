class ClassCastException(Exception):
    def __init__(self, type):
        self.type = type
        self.message = f"class {type.__name__} is not comparable"
        super().__init__(self.message)

class NoSuchElementException(Exception):
    pass

class NullPointerException(Exception):
    pass