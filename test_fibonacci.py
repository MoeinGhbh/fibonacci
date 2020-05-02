import pytest
import fibonacci
import random, string


def test_fibonacci():
    assert 1==1

def test_add_Node():
    result = fibonacci.Node(0)
    assert result.data == 0
    assert repr(result.next)== 'None'