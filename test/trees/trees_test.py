import pytest

from src.trees.node import Node

def test_node(capsys):
    n = Node(5)
    n.print()
    out,err=capsys.readouterr()
    assert out=="5 "

def test_insert_node_null():
    n = Node(5)
    n.insert(None)
    assert n.data == None

def test_insert_node_value():
    n = Node(5)
    n.insert(10)
    assert n.data == 5
    assert n.left == None
    assert n.right.data == 10

def test_insert_right_node_recursive():
    root_node = Node(5)
    assert root_node.data == 5
    root_node.insert(10)
    assert root_node.right.data == 10
    root_node.insert(20)
    assert root_node.right.right.data == 20

def test_insert_left_node_recursive():
    root_node = Node(20)
    assert root_node.data == 20
    root_node.insert(10)
    assert root_node.left.data == 10
    root_node.insert(5)
    assert root_node.left.left.data == 5

def test_print_tree(capsys):
    root = Node(30)
    root.insert(5)
    root.insert(15)
    root.insert(2)

    root.print_tree()
    out,err=capsys.readouterr()
    assert out=="2 5 15 30 "

def test_tree(capsys):
    ary = [10,9,55,25,75,5,30,100]
    root = Node(50)
    for x in ary:
        root.insert(x)

    #         50
    #     10      55
    #   9    25       75
    # 5       30        100

    root.print_tree()
    out,err=capsys.readouterr()
    assert out == "5 9 10 25 30 50 55 75 100 "




