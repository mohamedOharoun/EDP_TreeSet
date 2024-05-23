import unittest
from TreeSet import TreeSet, NoSuchElementException
from random import sample

class TestTreeSet(unittest.TestCase):

    def test_empty_treeset(self):
        tree = TreeSet(data_type=int)
        self.assertTrue(tree.isEmpty())
        self.assertEqual(tree.size(), 0)
        with self.assertRaises(NoSuchElementException):
            tree.first()
        with self.assertRaises(NoSuchElementException):
            tree.last()

    def test_ordered_insert(self):
        elements = list(range(1, 11))  # [1, 2, ..., 10]
        tree = TreeSet(data_type=int)
        for el in elements:
            tree.add(el)
        self.assertEqual(tree.size(), len(elements))
        self.assertFalse(tree.isEmpty())
        self.assertEqual(tree.first(), elements[0])
        self.assertEqual(tree.last(), elements[-1])
        self.assertTrue(tree.contains(5))
        self.assertFalse(tree.contains(11))

    def test_reverse_ordered_insert(self):
        elements = list(range(10, 0, -1))  # [10, 9, ..., 1]
        tree = TreeSet(data_type=int)
        for el in elements:
            tree.add(el)
        self.assertEqual(tree.size(), len(elements))
        self.assertFalse(tree.isEmpty())
        self.assertEqual(tree.first(), elements[-1])
        self.assertEqual(tree.last(), elements[0])
        self.assertTrue(tree.contains(5))
        self.assertFalse(tree.contains(11))

    def test_random_order_insert(self):
        elements = sample(range(1, 1001), 1000)  # 1000 unique random elements between 1 and 1000
        tree = TreeSet(data_type=int)
        for el in elements:
            tree.add(el)
        self.assertEqual(tree.size(), len(set(elements)))
        self.assertFalse(tree.isEmpty())
        self.assertEqual(tree.first(), min(elements))
        self.assertEqual(tree.last(), max(elements))
        self.assertTrue(tree.contains(elements[0]))
        self.assertFalse(tree.contains(1001))

    def test_remove(self):
        tree = TreeSet(data_type=int)
        tree.add(5)
        tree.add(10)
        tree.add(15)
        self.assertEqual(tree.size(), 3)
        tree.remove(5)
        self.assertFalse(tree.contains(5))
        self.assertEqual(tree.size(), 2)
        with self.assertRaises(NoSuchElementException):
            tree.remove(5)

    def test_clear(self):
        tree = TreeSet(data_type=int)
        tree.add(5)
        tree.add(10)
        tree.add(15)
        self.assertEqual(tree.size(), 3)
        tree.clear()
        self.assertEqual(tree.size(), 0)
        self.assertTrue(tree.isEmpty())
        with self.assertRaises(NoSuchElementException):
            tree.first()
        with self.assertRaises(NoSuchElementException):
            tree.last()

if __name__ == '__main__':
    unittest.main()
