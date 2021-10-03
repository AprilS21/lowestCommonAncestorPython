from LCA import * # The code to test
import unittest   # The test framework

class TestLCA(unittest.TestCase):
   tree = BST()
   tree.insert_node(2)
   tree.insert_node(3)
   tree.insert_node(1)
   def test_root(self):
        self.assertEqual(self.tree.root.data, 2)
   def test_root_left(self):
        self.assertEqual(self.tree.root.left.data, 1)
   def test_root_right(self):
        self.assertEqual(self.tree.root.right.data, 3)
