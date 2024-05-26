from enum import Enum
from inspect import isabstract
from RedBlackTree import RedBlackTree
from Exceptions import *

class Color(Enum):
    RED = 0
    BLACK = 1

class TreeSet:
    """
    This TreeSet is an implementation of the Java TreeSet that maintains order using a Red-Black Tree.
    """

    def __init__(self, data_type, collection=None):
        """
        Initializes a new TreeSet.
        
        Args:
            data_type (type): The type of elements to be stored in the TreeSet.
            collection (iterable, optional): A collection of elements to be added to the TreeSet.
        
        Raises:
            TypeError: If data_type is not a valid class or if an element of the collection is of the wrong type.
        """
        if data_type is None or (not isinstance(data_type, type) and not isabstract(data_type)):
            raise TypeError("TreeSet must be provided a class")
        self._type = data_type
        self._size = 0
        self._rb = RedBlackTree(self._type)
        if collection is not None:
            self.addAll(collection)

    def _check(self, key):
        """
        Checks if the key is valid for the TreeSet.
        
        Args:
            key: The key to check.
        
        Raises:
            NullPointerException: If the key is None.
            TypeError: If the key is not an instance of the TreeSet's data type.
            ClassCastException: If the key is not comparable.
        """
        if key is None:
            raise NullPointerException()
        if not isinstance(key, self._type):
            raise TypeError(f"Element must be instance of {self._type.__name__}, {type(key).__name__} provided")
        if not self._is_comparable(key):
            raise ClassCastException(type(key))

    def _is_comparable(self, key):
        """
        Checks if the key is comparable.
        
        Args:
            key: The key to check.
        
        Returns:
            bool: True if the key is comparable, False otherwise.
        """
        data_type = type(key)
        count = 0
        if data_type is object or data_type.__eq__ is not object.__eq__:
            count += 1
        if data_type is object or data_type.__gt__ is not object.__gt__:
            count += 1
        if data_type is object or data_type.__lt__ is not object.__lt__:
            count += 1
        return count == 3

    def add(self, new_key):
        """
        Adds a new element to the TreeSet.
        
        Args:
            new_key: The element to add.
        
        Returns:
            bool: True if the element was added, False if it was already present.
        """
        self._check(new_key)
        changed = self._rb.insert(new_key)
        if changed:
            self._size += 1
        return changed
    
    def addAll(self, new_keys):
        """
        Adds a collection of elements to the TreeSet.
        
        Args:
            new_keys (iterable): The collection of elements to add.
        
        Returns:
            bool: True if the TreeSet was modified, False otherwise.
        """
        changed = False
        for new_key in new_keys:
            self._check(new_key)
            if self._rb.insert(new_key):
                self._size += 1
                changed = True
        return changed

    def remove(self, key):
        """
        Removes an element from the TreeSet.
        
        Args:
            key: The element to remove.
        
        Returns:
            bool: True if the element was removed, False if it was not present.
        """
        self._check(key)
        changed = self._rb.delete(key)
        if changed:
            self._size -= 1
        return changed
    
    def isEmpty(self):
        """
        Checks if the TreeSet is empty.
        
        Returns:
            bool: True if the TreeSet is empty, False otherwise.
        """
        return self._size == 0
    
    def size(self):
        """
        Returns the size of the TreeSet.
        
        Returns:
            int: The number of elements in the TreeSet.
        """
        return self._size

    def contains(self, key):
        """
        Checks if the TreeSet contains a specific element.
        
        Args:
            key: The element to check for.
        
        Returns:
            bool: True if the element is present, False otherwise.
        """
        self._check(key)
        return self._rb.contains(key)

    def clear(self):
        """
        Clears all elements from the TreeSet.
        """
        self._size = 0
        self._rb = RedBlackTree(data_type=self._type)

    def clone(self):
        """
        Creates a shallow copy of the TreeSet.
        
        Returns:
            TreeSet: A new TreeSet containing the same elements.
        """
        new_tree = TreeSet(data_type=self._type)
        new_tree._rb = self._rb.clone()
        new_tree._size = self._size
        return new_tree
    
    def pollFirst(self):
        """
        Retrieves and removes the first (lowest) element, or returns None if the set is empty.
        
        Returns:
            The first element, or None if the set is empty.
        """
        result = self._rb.pollFirst()
        if result is not None:
            self._size -= 1
        return result

    def first(self):
        """
        Retrieves, but does not remove, the first (lowest) element.
        
        Returns:
            The first element.
        
        Raises:
            NoSuchElementException: If the set is empty.
        """
        if self._size == 0:
            raise NoSuchElementException()
        return self._rb.first()

    def floor(self, key):
        """
        Retrieves the greatest element in this set less than or equal to the given element, or None if there is no such element.
        
        Args:
            key: The element to compare.
        
        Returns:
            The greatest element less than or equal to the given element, or None if there is no such element.
        """
        self._check(key)
        return self._rb.floor(key)

    def higher(self, key):
        """
        Retrieves the least element in this set strictly greater than the given element, or None if there is no such element.
        
        Args:
            key: The element to compare.
        
        Returns:
            The least element strictly greater than the given element, or None if there is no such element.
        """
        self._check(key)
        return self._rb.higher(key)

    def last(self):
        """
        Retrieves, but does not remove, the last (highest) element.
        
        Returns:
            The last element.
        
        Raises:
            NoSuchElementException: If the set is empty.
        """
        if self._size == 0:
            raise NoSuchElementException()
        return self._rb.last()

    def lower(self, key):
        """
        Retrieves the greatest element in this set strictly less than the given element, or None if there is no such element.
        
        Args:
            key: The element to compare.
        
        Returns:
            The greatest element strictly less than the given element, or None if there is no such element.
        """
        self._check(key)
        return self._rb.lower(key)

    def pollLast(self):
        """
        Retrieves and removes the last (highest) element, or returns None if the set is empty.
        
        Returns:
            The last element, or None if the set is empty.
        """
        result = self._rb.pollLast()
        if result is not None:
            self._size -= 1
        return result
    
    def ceiling(self, key):
        """
        Retrieves the least element in this set greater than or equal to the given element, or None if there is no such element.
        
        Args:
            key: The element to compare.
        
        Returns:
            The least element greater than or equal to the given element, or None if there is no such element.
        """
        self._check(key)
        return self._rb.ceiling(key)
    
    def __iter__(self):
        """
        Returns an iterator over the elements in this set in ascending order.
        
        Returns:
            iterator: An iterator over the elements in ascending order.
        """
        return self._rb.__iter__()
    
    def iterator(self):
        """
        Returns an iterator over the elements in this set in ascending order.
        
        Returns:
            iterator: An iterator over the elements in ascending order.
        """
        return self.__iter__()
    
    def __reversed__(self):
        """
        Returns an iterator over the elements in this set in descending order.
        
        Returns:
            iterator: An iterator over the elements in descending order.
        """
        return self._rb.__reversed__()
    
    def descendingIterator(self):
        """
        Returns an iterator over the elements in this set in descending order.
        
        Returns:
            iterator: An iterator over the elements in descending order.
        """
        return self.__reversed__()
