"""
CSCI-141 Computer Science 1 Presentation Code
13-Trees
Binary Tree Node

The definition of a binary tree node and maker functions for leaf
and non-leaf nodes.
"""

from dataclasses import dataclass
from typing import Any, Union

@dataclass
class BTNode:
    value: Any                          # node can hold any value
    left: Union[None, 'BTNode']         # the left child
    right: Union[None, 'BTNode']        # the right child

def mk_btnode_leaf(value):
    """
    Make and return a leaf node (no children).
    :param value: value for the node
    :return: a new BTNode
    """
    return BTNode(value, None, None)

def mk_btnode(value, left, right):
    """
    Make and return a non-leaf node.
    :param value: value for the node
    :param left: left child (BTNode)
    :param right: right child (BTNode)
    :return: a new BTNode
    """
    return BTNode(value, left, right)

def test_btnode():
    """
    Test routine for BTNode.
    """
    root_A = mk_btnode_leaf('A')
    print('root_A:', root_A)
    print('root_A value:', root_A.value)

    root_B = mk_btnode('B', mk_btnode_leaf('C'), mk_btnode_leaf('D'))
    print('root_B:', root_B)
    print('root_B left:', root_B.left)
    print('root_B right:', root_B.right)

if __name__ == '__main__':
    test_btnode()

"""
$ python3 btnode.py
root_A: BTNode(value='A', left=None, right=None)
root_A value: A
root_B: BTNode(value='B', left=BTNode(value='C', left=None, right=None), right=BTNode(value='D', left=None, right=None))
root_B left: BTNode(value='C', left=None, right=None)
root_B right: BTNode(value='D', left=None, right=None)
"""