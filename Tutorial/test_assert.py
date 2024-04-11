import pytest

def test_func1():
    assert True
def test_func2():
    assert False
def test_func3():
    a=3,
    b=4
    assert a == b
def test_func4():
    a=3
    b=4
    assert a != b
def test_func5():
    a=5
    b=2
    assert multiply(a,b) == 10

def test_func6():
    a,b,c= "Suman","Maiti","Suman"
    assert a.__eq__(b), " a and b are not same"
def test_func7():
    a,b,c= "Suman","Maiti","Suman"
    assert a.__contains__("man"),"a contains man"
    assert a.endswith('Maiti'), "a doesn't end with Maiti"
def multiply(x,y):
    return x*y