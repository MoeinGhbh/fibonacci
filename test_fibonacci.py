import pytest
import fibonacci
import random, string

def test_add_Node():
    result = fibonacci.Node(0)
    assert result.data == 0
    assert repr(result.next)== 'None'

def test_add_list():
    linklist = fibonacci.LinkedList()
    assert repr(linklist.head) == 'None'


def test_first_list():
    node = fibonacci.Node(0)
    repr(fibonacci.LinkedList().add_first(node))