import pytest

from src.bv_recursive_depth_first_binary_tree import Tree
from src.trees.node import Node

def test_bfs():

    root_node = Node(1)
    root_node.insert(2)
    root_node.insert(3)
    root_node.insert(4)
    root_node.insert(5)
    root_node.insert(6)
    root_node.insert(7)
    root_node.insert(8)
    root_node.insert(9)


    tree = Tree()
    assert tree.dfs(root_node) == [1,2,4,8,9,5,3,6,7]
