from enum import Enum
import time

class Color(Enum):
    RED = 0
    BLACK = 1

class Node:
    def __init__(self, data_type, key=None, color=Color.RED, left=None, right=None, parent=None):
        self.color = color
        self.left = left
        self.right = right
        self.key = key if key is None else data_type(key)
        self.parent = parent
        self.data_type = data_type

class RedBlackTree:
    def __init__(self, data_type):
        self.nil = Node(data_type=data_type, key=None, color=Color.BLACK)
        self.data_type = data_type
        self.root = self.nil

    def lookup(self, key):
        return self._lookup(self.root, key)

    def _lookup(self, node, key):
        if node == self.nil or node.key == key:
            return node
        if key < node.key:
            return self._lookup(node.left, key)
        else:
            return self._lookup(node.right, key)

    def insert(self, key):
        new_node = Node(data_type=self.data_type, key=key)
        parent = None
        current = self.root

        while current != self.nil:
            parent = current
            if new_node.key < current.key:
                current = current.left
            elif new_node.key > current.key:
                current = current.right
            else:
                return False

        new_node.parent = parent
        if parent is None:
            self.root = new_node
        elif new_node.key < parent.key:
            parent.left = new_node
        else:
            parent.right = new_node

        new_node.left = self.nil
        new_node.right = self.nil
        new_node.color = Color.RED

        self._insert_fixup(new_node)
        return True

    def _insert_fixup(self, z):
        while z.parent and z.parent.color == Color.RED:
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right
                if y.color == Color.RED:
                    z.parent.color = Color.BLACK
                    y.color = Color.BLACK
                    z.parent.parent.color = Color.RED
                    z = z.parent.parent
                else:
                    if z == z.parent.right:
                        z = z.parent
                        self._left_rotate(z)
                    z.parent.color = Color.BLACK
                    z.parent.parent.color = Color.RED
                    self._right_rotate(z.parent.parent)
            else:
                y = z.parent.parent.left
                if y.color == Color.RED:
                    z.parent.color = Color.BLACK
                    y.color = Color.BLACK
                    z.parent.parent.color = Color.RED
                    z = z.parent.parent
                else:
                    if z == z.parent.left:
                        z = z.parent
                        self._right_rotate(z)
                    z.parent.color = Color.BLACK
                    z.parent.parent.color = Color.RED
                    self._left_rotate(z.parent.parent)

        self.root.color = Color.BLACK
    
    def contains(self, key):
        node = self.lookup(key)
        if node is None or node == self.nil:
            return False
        return True

    def delete(self, key):
        node = self.lookup(key)
        if node is None or node == self.nil:
            return False

        y = node
        original_color = y.color
        if node.left == self.nil:
            x = node.right
            self._transplant(node, node.right)
        elif node.right == self.nil:
            x = node.left
            self._transplant(node, node.left)
        else:
            y = self._minimum(node.right)
            original_color = y.color
            x = y.right
            if y.parent == node:
                x.parent = y
            else:
                self._transplant(y, y.right)
                y.right = node.right
                y.right.parent = y
            self._transplant(node, y)
            y.left = node.left
            y.left.parent = y
            y.color = node.color

        if original_color == Color.BLACK:
            self._delete_fixup(x)
        return True

    def _transplant(self, u, v):
        if u.parent == self.nil:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        if v is not None:
            v.parent = u.parent

    def _delete_fixup(self, x):
        while x != self.root and x.color == Color.BLACK:
            if x == x.parent.left:
                w = x.parent.right
                if w.color == Color.RED:
                    w.color = Color.BLACK
                    x.parent.color = Color.RED
                    self._left_rotate(x.parent)
                    w = x.parent.right
                if w.left.color == Color.BLACK and w.right.color == Color.BLACK:
                    w.color = Color.RED
                    x = x.parent
                else:
                    if w.right.color == Color.BLACK:
                        w.left.color = Color.BLACK
                        w.color = Color.RED
                        self._right_rotate(w)
                        w = x.parent.right
                    w.color = x.parent.color
                    x.parent.color = Color.BLACK
                    w.right.color = Color.BLACK
                    self._left_rotate(x.parent)
                    x = self.root
            else:
                w = x.parent.left
                if w.color == Color.RED:
                    w.color = Color.BLACK
                    x.parent.color = Color.RED
                    self._right_rotate(x.parent)
                    w = x.parent.left
                if w.right.color == Color.BLACK and w.left.color == Color.BLACK:
                    w.color = Color.RED
                    x = x.parent
                else:
                    if w.left.color == Color.BLACK:
                        w.right.color = Color.BLACK
                        w.color = Color.RED
                        self._left_rotate(w)
                        w = x.parent.left
                    w.color = x.parent.color
                    x.parent.color = Color.BLACK
                    w.left.color = Color.BLACK
                    self._right_rotate(x.parent)
                    x = self.root
        x.color = Color.BLACK

    def _left_rotate(self, x):
        if x is None:
            return
        y = x.right
        if y is None:
            return
        x.right = y.left
        if y.left != self.nil:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y


    def _right_rotate(self, y):
        if y is None:
            return
        x = y.left
        if x is None:
            return
        y.left = x.right
        if x.right != self.nil:
            x.right.parent = y
        x.parent = y.parent
        if y.parent is None:
            self.root = x
        elif y == y.parent.right:
            y.parent.right = x
        else:
            y.parent.left = x
        x.right = y
        y.parent = x

    def _minimum(self, node):
        while node is not None and node.left != self.nil:
            node = node.left
        return node

    def print_tree(self):
        self._inorder_traversal(self.root)

    def _inorder_traversal(self, node):
        if node != self.nil:
            self._inorder_traversal(node.left)
            parent_key = node.parent.key if node.parent != self.nil else None
            color = node.color.name
            print(f"Key: {node.key}, Color: {color}, Parent: {parent_key}")
            self._inorder_traversal(node.right)

    def print_tree(self):
        self._inorder_traversal(self.root)

    def _inorder_traversal(self, node):
        if node != self.nil:
            parent_key = node.parent.key if node.parent is not None else None
            color = node.color.name
            print(f"Key: {node.key}, Color: {color}, Parent: {parent_key}")
            self._inorder_traversal(node.left)
            self._inorder_traversal(node.right)
    
    def __iter__(self):
        return self.KeysIterator(self.root, self.nil)
    
    def __reversed__(self):
        return self.KeysIterator(self.root, self.nil, reverse=True)

    class KeysIterator:
        def __init__(self, node, nil, reverse=False):
            self.stack = []
            self.nil = nil
            self.reverse = reverse
            if reverse:
                self._traverse_right(node)
            else:
                self._traverse_left(node)
        def __iter__(self):
            return self

        def __next__(self):
            if not self.stack:
                raise StopIteration
            node = self.stack.pop()
            key = node.key
            if self.reverse:
                self._traverse_right(node.left)
            else:
                self._traverse_left(node.right)
            return key

        def _traverse_left(self, node):
            while node != self.nil:
                self.stack.append(node)
                node = node.left

        def _traverse_right(self, node):
            while node != self.nil:
                self.stack.append(node)
                node = node.right

    def clone(self):
        new_tree = RedBlackTree(self.data_type)
        new_tree.root = self._clone_recursive(self.root, new_tree.nil)
        return new_tree

    def _clone_recursive(self, node, nil):
        if node is None:
            return nil
        if node.key is None:
            return nil
        new_node = Node(
            data_type=node.data_type,
            key=node.key,
            color=node.color,
            left=self._clone_recursive(node.left, nil),
            right=self._clone_recursive(node.right, nil),
            parent=nil if node.parent == nil else node.parent,
        )
        if new_node.left != nil:
            new_node.left.parent = new_node
        if new_node.right != nil:
            new_node.right.parent = new_node
        return new_node
"""
tree = RedBlackTree(int)
print(tree.insert(-1))
print(tree.contains(3))
print(tree.contains(-1))
start_time = time.time()
number = 10
for i in range(number, 0, -1):
    print(i)
    tree.insert(i)
end_time = time.time()
print(end_time - start_time)
start_time = time.time()
tree.insert(number)
end_time = time.time()
print(end_time - start_time)
print(tree.insert(1_000))
"""