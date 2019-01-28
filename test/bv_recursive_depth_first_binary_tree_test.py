import pytest

from src.bv_recursive_depth_first_binary_tree import Tree
from src.trees.node import Node

def test_bfs():

    ary = [10,9,55,25,75,5,60,30,100]
    root = Node(50)
    for x in ary:
        root.insert(x)
    #         50
    #     10      55
    #   9    25      75
    # 5       30   60   100

    tree = Tree(root)
    assert tree.generate_list() == [50, 10, 9, 5, 25, 30, 55, 75, 60, 100]
