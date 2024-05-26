import unittest
from TreeSet import TreeSet
from Exceptions import NullPointerException, ClassCastException, NoSuchElementException

class TestTreeSetWithElements(unittest.TestCase):
    
    def setUp(self):
        self.tree_set = TreeSet(int)
        self.values = list(range(1, 51))
        for value in reversed(self.values):
            self.tree_set.add(value)

    def test_size_after_adding_elements(self):
        self.assertFalse(self.tree_set.isEmpty())
        self.assertEqual(self.tree_set.size(), 50)

    def test_contains_elements(self):
        for value in self.values:
            self.assertTrue(self.tree_set.contains(value))

    def test_iterator(self):
        iterator_values = list(self.tree_set)
        self.assertEqual(iterator_values, self.values)

    def test_descending_iterator(self):
        descending_values = list(reversed(self.tree_set))
        self.assertEqual(descending_values, list(reversed(self.values)))

    def test_pollFirst(self):
        for value in self.values:
            self.assertEqual(self.tree_set.pollFirst(), value)
        self.assertTrue(self.tree_set.isEmpty())

    def test_pollLast(self):
        for value in reversed(self.values):
            self.assertEqual(self.tree_set.pollLast(), value)
        self.assertTrue(self.tree_set.isEmpty())

    def test_first(self):
        self.assertEqual(self.tree_set.first(), 1)
        self.tree_set.pollFirst()  # remove the first element
        self.assertEqual(self.tree_set.first(), 2)

    def test_last(self):
        self.assertEqual(self.tree_set.last(), 50)
        self.tree_set.pollLast()  # remove the last element
        self.assertEqual(self.tree_set.last(), 49)

    def test_floor(self):
        self.assertEqual(self.tree_set.floor(25), 25)
        self.assertEqual(self.tree_set.floor(26), 26)
        self.assertEqual(self.tree_set.floor(0), None)

    def test_ceiling(self):
        self.assertEqual(self.tree_set.ceiling(25), 25)
        self.assertEqual(self.tree_set.ceiling(24), 24)
        self.assertEqual(self.tree_set.ceiling(51), None)

    def test_higher(self):
        self.assertEqual(self.tree_set.higher(25), 26)
        self.assertEqual(self.tree_set.higher(50), None)

    def test_lower(self):
        self.assertEqual(self.tree_set.lower(25), 24)
        self.assertEqual(self.tree_set.lower(1), None)

    def test_add_null(self):
        with self.assertRaises(NullPointerException):
            self.tree_set.add(None)

    def test_contains_null(self):
        with self.assertRaises(NullPointerException):
            self.tree_set.contains(None)

    def test_remove_null(self):
        with self.assertRaises(NullPointerException):
            self.tree_set.remove(None)

    def test_remove_existing_element(self):
        self.assertTrue(self.tree_set.remove(25))
        self.assertFalse(self.tree_set.contains(25))
        self.assertEqual(self.tree_set.size(), 49)

    def test_remove_non_existing_element(self):
        self.assertFalse(self.tree_set.remove(100))
        self.assertEqual(self.tree_set.size(), 50)

    def test_floor_null(self):
        with self.assertRaises(NullPointerException):
            self.tree_set.floor(None)

    def test_ceiling_null(self):
        with self.assertRaises(NullPointerException):
            self.tree_set.ceiling(None)

    def test_higher_null(self):
        with self.assertRaises(NullPointerException):
            self.tree_set.higher(None)

    def test_lower_null(self):
        with self.assertRaises(NullPointerException):
            self.tree_set.lower(None)

if __name__ == '__main__':
    unittest.main()