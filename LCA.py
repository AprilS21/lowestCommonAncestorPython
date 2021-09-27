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

done = False

while done == False :
    user = input("Enter a value to add to bst or 'lca': ")
    if(user != "lca"):
        tree.insert_node(int(user))
    else:
        value1 = int(input("Enter the first value: "))
        value2 = int(input("Enter the second value: "))
        node1 = tree.search(value1)
        node2 = tree.search(value2)
        print("The lowest common ancestor of these values is: " )
        print(tree.lowestCommonAncestor(tree.root, node1, node2).data)
        done = True



""" tree.insert_node(7)
tree.insert_node(3)
tree.insert_node(8)
tree.insert_node(12)
tree.insert_node(1)
tree.insert_node(9)
tree.insert_node(4)
tree.insert_node(6)

value1 = int(input("Enter the first value: "))
value2 = int(input("Enter the second value: "))
node1 = tree.search(value1)
node2 = tree.search(value2)
print(tree.lowestCommonAncestor(tree.root, node1, node2).data) """

