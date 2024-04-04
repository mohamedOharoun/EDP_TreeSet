# Red-Black Tree
from enum import Enum


class Color(Enum):
    RED = 0
    BLACK = 1


class TreeSet:
    class Node:
        def __init__(self, key=None, color=Color.RED, left=None, right=None, parent=None):
            self.color = color
            self.left = left
            self.right = right
            self.key = key
            self.parent = parent

    def __init__(self, type, collection=None):
        if type is None:
            raise Exception
        self._type = type
        self._root = None


    def add(self, new_key):
        pass

        