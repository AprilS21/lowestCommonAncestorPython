from LCA import *
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
        if(node1 == False or node2 ==False):
            print("LCA does not exist for these two values")
            done = True
        else:
            print("The lowest common ancestor of these values is: " )
            print(tree.lowestCommonAncestor(tree.root, node1, node2).data)
            done = True