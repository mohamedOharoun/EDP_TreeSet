# Red-Black Tree
from enum import Enum
from inspect import isabstract
from RedBlackTree import RedBlackTree
from Exceptions import *

class Color(Enum):
    RED = 0
    BLACK = 1

class TreeSet:
    def __init__(self, data_type, collection=None):
        if data_type is None or (not isinstance(data_type, type) and not isabstract(data_type)):
            raise TypeError("TreeSet must be provided a class")
        self._type = data_type
        self._size = 0
        self._rb = RedBlackTree(self._type)
        if collection is not None:
            self.addAll(collection)

    def _check(self, key):
        if not isinstance(key, self._type):
            raise TypeError(f"Element must be instance of {self._type.__name__}, {type(key).__name__} provided")
        if not self._is_comparable(key):
            raise ClassCastException(type(key))

    def _is_comparable(self, key):
        data_type = type(key)
        count = 0
        if data_type is object or data_type.__eq__ is not object.__eq__:
            count += 1
        if data_type is object or data_type.__gt__ is not object.__gt__:
            count += 1
        if data_type is object or data_type.__lt__ is not object.__lt__:
            count += 1
        if count < 3:
            return False
        return True

    def add(self, new_key):
        self._check(new_key)
        changed = self._rb.insert(new_key)
        if changed:
            self._size += 1
        return changed
    
    def addAll(self, new_keys):
        changed = False
        for new_key in new_keys:
            self._check(new_key)
            if self._rb.insert(new_key):
                self._size += 1
                changed = True
        return changed

    def remove(self, key):
        self._check(key)
        changed = self._rb.delete(key)
        if changed:
            self._size -= 1
        return changed
    
    def isEmpty(self):
        return True if self._size == 0 else False
    
    def size(self):
        return self._size

    def contains(self, key):
        self._check(key)
        return  self._rb.contains(key)

    def clear(self):
        self._size = 0
        self._rb = RedBlackTree(data_type=self._type)

    def clone(self):
        new_tree = TreeSet(data_type=self._type)
        new_tree._rb = self._rb.clone()
        new_tree._size = self._size
        return new_tree
    
    def pollFirst(self):
        result = self._rb.pollFirst()
        if result is not None:
            self._size -= 1
        return result

    def first(self):
        if self._size == 0:
            raise NoSuchElementException()
        return self._rb.first()

    def floor(self, key):
        self._check(key)
        return self._rb.floor(key)

    def higher(self, key):
        self._check(key)
        return self._rb.higher(key)

    def last(self):
        if self._size == 0:
            raise NoSuchElementException()
        return self._rb.last()

    def lower(self, key):
        self._check(key)
        return self._rb.lower(key)

    def pollLast(self):
        result = self._rb.pollLast()
        if result is not None:
            self._size -= 1
        return result
    
    def ceiling(self, key):
        self._check(key)
        return self._rb.ceiling(key)
    
    def __iter__(self):
        return self._rb.__iter__()
    
    def iterator(self):
        return self._rb.__iter__()
    
    def __reversed__(self):
        return self._rb.__reversed__()
    
    def descendingIterator(self):
        return self._rb.__reversed__()

tree = TreeSet(data_type=int)
print(tree.size())
tree.remove(3)
print(tree.size())