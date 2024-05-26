import unittest
from TreeSet import TreeSet
from Exceptions import NullPointerException, ClassCastException, NoSuchElementException

class TestTreeSetEmpty(unittest.TestCase):
    
    def setUp(self):
        self.tree_set = TreeSet(int)

    def test_initial_size(self):
        self.assertTrue(self.tree_set.isEmpty())
        self.assertEqual(self.tree_set.size(), 0)

    def test_contains_on_empty_set(self):
        self.assertFalse(self.tree_set.contains(1))

    def test_first_on_empty_set(self):
        with self.assertRaises(NoSuchElementException):
            self.tree_set.first()

    def test_last_on_empty_set(self):
        with self.assertRaises(NoSuchElementException):
            self.tree_set.last()

    def test_floor_on_empty_set(self):
        self.assertIsNone(self.tree_set.floor(1))

    def test_ceiling_on_empty_set(self):
        self.assertIsNone(self.tree_set.ceiling(1))

    def test_higher_on_empty_set(self):
        self.assertIsNone(self.tree_set.higher(1))

    def test_lower_on_empty_set(self):
        self.assertIsNone(self.tree_set.lower(1))

    def test_pollFirst_on_empty_set(self):
        self.assertIsNone(self.tree_set.pollFirst())

    def test_pollLast_on_empty_set(self):
        self.assertIsNone(self.tree_set.pollLast())

    def test_remove_on_empty_set(self):
        self.assertFalse(self.tree_set.remove(1))

    def test_add_null(self):
        with self.assertRaises(NullPointerException):
            self.tree_set.add(None)

    def test_add_wrong_type(self):
        with self.assertRaises(TypeError):
            self.tree_set.add("string")

    def test_contains_null(self):
        with self.assertRaises(NullPointerException):
            self.tree_set.contains(None)

    def test_remove_null(self):
        with self.assertRaises(NullPointerException):
            self.tree_set.remove(None)

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
