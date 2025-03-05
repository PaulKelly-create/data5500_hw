#Hey chat, can you quickly explain what a binary search tree is and how you would put it into a function?
# Example Binary Search Tree:
#        10
#       /  \
#      5   15
#     / \    \
#    3   7   20
#Is there a way I can see the output of this tree to check if I am doing it right?

#Making the class for the binary search tree
class Tree:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
#make a function to insert values into the tree, larger ones go on the right, smaller on the left
def insert_bst(root, value):
    if root is None:
        return Tree(value)
    #If the value is smaller then the one it is next to it goes on the left
    if value < root.val:
        root.left = insert_bst(root.left, value)
    #If the value is bigger it goes on the right
    else:
        root.right = insert_bst(root.right, value)
    return root
#I wanted to be able to see the tree, or at least the values 
#Made a function to see the values, the smallest to the biggest in the tree
def traversal(root):
    if root:
        traversal(root.left)
        print(root.val, end=' ')
        traversal(root.right)

#tested out the functions to see if it was inserting and the smaller values went on the left
root = Tree(18)
root = insert_bst(root, 6)
root = insert_bst(root, 12)
root = insert_bst(root, 5)
root = insert_bst(root, 19)
#Tested to see the values, smallest first 
traversal(root)
