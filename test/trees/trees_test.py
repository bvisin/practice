import pytest

from src.trees.node import Node

def test_node(capsys):
    n = Node(5)
    n.print()
    out,err=capsys.readouterr()
    assert out=="5\n"
