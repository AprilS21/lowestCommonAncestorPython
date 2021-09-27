class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

class BST:
    def __init__(self):
        self.root = None
    def set_root(self,data):
        self.root = Node(data)
    def insert_node(self,data):
        if self.root is None:
            self.set_root(data)
        else:
            n = Node(data)
            troot = self.root
            while troot:
                if data < troot.data:
                    if troot.left:
                        troot = troot.left
                    else:
                        troot.left = n
                        break
                else:
                    if troot.right:
                        troot = troot.right
                    else:
                        troot.right = n
                        break
    def search_node(self,data):
        if self.root is None:
            return "Not found"
        else:
            troot = self.root
            while troot:
                if data < troot.data:
                    if troot.left:
                        troot = troot.left
                        if troot.data == data:
                            return "Found"
                    else:
                        return "Not found"
                elif data > troot.data:
                    if troot.right:
                        troot = troot.right
                        if troot.data == data:
                            return "Found"
                    else:
                        return "Not found"
                else:
                    return "Found"

    def lowestCommonAncestor(self, root: 'Node', p: 'Node', q: 'Node') -> 'Node':
        while (root.data - p.data) * (root.data - q.data) > 0:
            root = (root.left, root.right)[p.data > root.data]
        return root

    def search(self, value):
        """
        Value will be to the left of node if node > value; right otherwise.
        """
        node = self.root
        while node is not None:
            if node.data == value:
                return node    # node.value
            if node.data > value:
                node = node.left
            else:
                node = node.right
        return False

tree = BST()
tree.insert_node(10)
tree.insert_node(5)
tree.insert_node(20)
tree.insert_node(7)

print(tree.root.data)
print(tree.root.left.data)
print(tree.root.right.data)
print(tree.root.left.right.data)

print(tree.search_node(10))
print(tree.search_node(5))
print(tree.search_node(20))
print(tree.search_node(7))
print(tree.search_node(12))
print(tree.search_node(15))

value1 = int(input("Enter the first value: "))
value2 = int(input("Enter the second value: "))
node1 = tree.search(value1)
node2 = tree.search(value2)
print(tree.lowestCommonAncestor(tree.root, node1, node2).data)

