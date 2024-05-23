# Red-Black Tree
from enum import Enum
from inspect import isabstract
from abc import ABC
from RedBlackTree import RedBlackTree

class Color(Enum):
    RED = 0
    BLACK = 1


class TreeSet:
    def __init__(self, data_type, collection=None):
        if data_type is None:
            raise Exception
        if not isinstance(data_type, type) and not isabstract(data_type):
            raise Exception
        count = 0
        if data_type is object or data_type.__eq__ is not object.__eq__:
            count += 1
        if data_type is object or data_type.__gt__ is not object.__gt__:
            count += 1
        if data_type is object or data_type.__lt__ is not object.__lt__:
            count += 1
        if count < 3:
            raise Exception
        self._type = data_type
        self._size = 0
        self._rb = RedBlackTree(self._type)
        if collection is not None:
            self.addAll(collection)

    def add(self, new_key):
        if not isinstance(new_key, self._type):
            raise Exception
        changed = self._rb.insert(new_key)
        if changed:
            self._size += 1
        return changed
    
    def addAll(self, new_keys):
        changed = False
        for new_key in new_keys:
            if not isinstance(new_key, self._type):
                raise Exception
            if self._rb.insert(new_key):
                self._size += 1
                changed = True
        return changed

    def remove(self, key):
        if not isinstance(key, self._type):
            raise Exception
        changed = self._rb.delete(key)
        if changed:
            self._size -= 1
        return changed
    
    def isEmpty(self):
        return True if self._size > 0 else False
    
    def size(self):
        return self._size

    def contains(self, key):
        return  self._rb.contains(key)

    def clear(self):
        self._size = 0
        self._rb = RedBlackTree(data_type=self._type)

    def clone(self):
        new_tree = TreeSet(data_type=self._type)
        new_tree._rb = self._rb.clone()
        return new_tree
    
    def __iter__(self):
        return self._rb.__iter__()
    
    def iterator(self):
        return self._rb.__iter__()
    
    def __reversed__(self):
        return self._rb.__reversed__()
    
    def descendingIterator(self):
        return self._rb.__reversed__()

tree = TreeSet(data_type=int, collection=[1, 5, 3, 4, 5])
tree2 = tree.clone()
print(tree.size())
print(tree.remove(1), tree.remove(2))
print(tree.size())
for i in reversed(tree2):
    print(i)
