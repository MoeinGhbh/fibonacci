import pytest
import fibonacci

def test_compute():
    res=fibonacci.compute(100)
    test = False
    for i in res:
        if i.data==218922995834555169026:
            test = True
    assert test        

    res=fibonacci.compute(10)
    test = False
    for i in res:
        if i.data==34:
            test = True
    assert test  

    #  if existe
    res=fibonacci.compute(50)
    test = False
    for i in res:
        if i.data==7778742049:
            test = True
    assert test  

    #   if not existe
    res=fibonacci.compute(50)
    test = True
    for i in res:
        if i.data==7778742050:
            test = False
    assert test  


        

def test_add_Node():
    result = fibonacci.Node(0)
    assert result.data == 0
    assert repr(result.next)== 'None'

def test_add_list():
    linklist = fibonacci.LinkedList()
    assert repr(linklist.head) == 'None'

