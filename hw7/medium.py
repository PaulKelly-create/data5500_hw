#How would you search a binary tree for a specific value?
#This one was easier after the first problem of making a tree I understand the structure more and how to search that structure

#Make the class set values
class Tree:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
#Make a function to search the tree for sepcific target, or value
def search_bst(root, target):
    #Base case when the root is None it will return false
    if root is None:
        return False
    #If the target matches the root return true
    if root.value == target:
        return True
    #If the target is less search the left side where the smaller values are
    if target < root.value:
        return search_bst(root.left, target)
    #Vise versa if the target is larger search the right side with bigger values
    return search_bst(root.right, target)

#Test number for an example, make the binary search tree
root = Tree(10)
root.left = Tree(5)
root.right = Tree(15)
root.left.left = Tree(3)
root.left.right = Tree(7)
root.right.right = Tree(20)

# Search for value 7 which is in the tree and should output true
print(search_bst(root, 7))  

# Search for value 13 which is not in the tree and should output false
print(search_bst(root, 13)) 
