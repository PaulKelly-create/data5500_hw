"""
Explain the process of deleting a node from a binary search tree in Python. Discuss how you would handle different cases, such as deleting a node with one, or two children. 
Additionally, explain any potential challenges or edge cases that may arise during the deletion process and how you would address them. 

Deleting a node from a binary tree and how hard it is larger depends on what kind of node it is, whether is has no children (a leaf node), one child, or two children which is 
the most complex case. If you are deleting a node with no children or a leaf node, you can simply remove it by setting the parents reference to None which gets rid of it. 
If it has one child you need to bypass the node and link its parent to its only child, so the parents left or right child pointer will point directly to the nodes only
child. So you link the child to the parents parent from my understanding.
The hardest case of when the node has two children is a bit more complex. You need to find the in order successor/predecessor to replace the node, which is the smallest node
in the right subtree (successor), or the largest node in the left subtree(predecessor). Once you have found the right sucessor/predecessor you can copy its value to the node 
we are deleting, and delete the successor/predecessor which will have at most one child.
For edge cases and challenges, if the root is None there is nothing to delete it is an empty tree. If we are deleting the root node it needs special handling but can be 
handled by considering it's children and moving them to the appropriate spot. There shouldn't be multiple nodes with the same value as BST doesn't allow duplicate values.
Deletion can unbalance the tree, however you can rebalance the tree and won't be too big an issue for a standard BST, and can be handled seperately. 
So when deleting a node from a binary search tree in python you need to see if it is a node with no children, one child, or two children, and have your function be able to
adaquetly handle these three senarios, as well as if it is an empty tree and nothing needs to be deleted. For no children we return None to remove the node, for one child we
can return the child node to bypass the current node, and for two children we find the in order successor copy its value to the current node, and then delete the in order
successor. 
"""
#an example of a funtion that potential could delete a node, depending on no child, one child or two children
"""
def delete_node(root, key):
    # Base case: If the root is None, return None
    if not root:
        return root

    # Recursive case: traverse the tree
    if key < root.value:
        root.left = delete_node(root.left, key)
    elif key > root.value:
        root.right = delete_node(root.right, key)
    else:
        # Node to be deleted is a leaf (no children)
        if not root.left and not root.right:
            return None

        # Node to be deleted has one child
        elif not root.left:
            return root.right
        elif not root.right:
            return root.left

        # Node to be deleted has two children
        # Find the in-order successor (smallest in the right subtree)
        min_node = find_min(root.right)
        # Replace the node's value with the in-order successor's value
        root.value = min_node.value
        # Delete the in-order successor
        root.right = delete_node(root.right, min_node.value)
"""