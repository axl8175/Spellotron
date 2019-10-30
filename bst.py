"""
CSCI-141 Computer Science 1 Presentation Code
13-Trees
Binary Search Trees

Example code with a binary search tree for inserting and creating a string
of elements in order.  This BST does not allow duplicate elements.
"""

from btnode import *

@dataclass
class BST:
    size: int                   # number of elements in tree
    root: Union[None, BTNode]   # the root node of the tree

def mk_bst():
    """
    Create and return an empty BST.
    :return: new empty BST
    """
    return BST(0, None)

def insert_rec(value, node):
    """
    A helper function for recursively inserting a new element into
    the BST.
    :param value: the element to insert
    :param node: the current node (BSTNode)
    :return: whether the element was inserted or not (a duplicate)
    """
    if value == node.value:                       # don't insert a duplicate
        return False
    elif value < node.value:                      # if going left
        if node.left == None:                     # insert new node if no left child
            node.left = mk_btnode_leaf(value)
            return True
        else:                                     # otherwise recurse with the left child
            return insert_rec(value, node.left)
    else:                                         # if going right
        if node.right == None:                    # insert new node if no right child
            node.right = mk_btnode_leaf(value)
            return True
        else:                                     # otherwise recurse with the right child
            return insert_rec(value, node.right)

def insert(value, tree):
    """
    Insert a new value into the BST.
    :param value: the element to insert
    :param tree: the BST
    :return: whether the element was inserted or not (a duplicate)
    """
    inserted = True

    if tree.root == None:   # if tree is empty make a root node
        tree.root = mk_btnode_leaf(value)
    else:                   # otherwise call helper function with root node
        inserted = insert_rec(value, tree.root)

    if inserted == True:    # increase tree size if the value was not a duplicate
        tree.size = tree.size + 1

    return inserted

def to_string_rec(node):
    """
    Helper function for creating a string representation out of a node
    (BSTNode) by doing an inorder traversal.  The string will have spaces
    between each value.
    :param node: the current node (BSTNode)
    :return: a string with spaces
    """
    if node == None:   # an empty node means we append a space
        return ' '
    else:              # otherwise traverse and build the string using concatenation
        return to_string_rec(node.left) + repr(node.value) + to_string_rec(node.right)

def to_string(tree):
    """
    Get a string representation out of the BST.
    :param tree: the BST
    :return: a python style list string of the values
    """
    result = to_string_rec(tree).strip()   # get string with spaces
    result = result.replace(' ', ', ')     # replace all spaces with commas
    return "[" + result + "]"              # bookend the string with brackets

def test_bst(values):
    """
    Test a BST by inserting a list of values into an initially empty one
    and then determining the size and its string representation.
    :param values: a list of values to insert into the BST
    :return:
    """
    print('values:', values)

    tree = mk_bst()
    for value in values:
        insert(value, tree)

    print('size:', tree.size)
    print('to_string:', to_string(tree.root))
    print()

def test_bsts():
    """
    Test building several BST's from a list of values.
    """
    test_bst([])
    test_bst(['hello'])
    test_bst([20, 10, 30])
    test_bst([17, 5, 35, 2, 16, 29, 38, 19, 33])
    test_bst(['the', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog'])

if __name__ == '__main__':
    test_bsts()

"""
$ python3 bst.py
values: []
size: 0
to_string: []

values: ['hello']
size: 1
to_string: ['hello']

values: [20, 10, 30]
size: 3
to_string: [10, 20, 30]

values: [17, 5, 35, 2, 16, 29, 38, 19, 33]
size: 9
to_string: [2, 5, 16, 17, 19, 29, 33, 35, 38]

values: ['the', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']
size: 8
to_string: ['brown', 'dog', 'fox', 'jumps', 'lazy', 'over', 'quick', 'the']
"""