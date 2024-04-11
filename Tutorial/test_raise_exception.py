import pytest

def generate_exception1():
    raise IndexError()

def generate_exception2():
    raise ExceptionGroup(
        "Group_Exception",[TypeError(),NameError(),ZeroDivisionError()]
    )
def test_func1():
    with pytest.raises(IndexError) as exp:
        generate_exception1()
def test_func2():
    with pytest.raises(ExceptionGroup) as exp:
        generate_exception2()
    assert exp.group_contains(TypeError)
    assert exp.group_contains(NameError)
    assert not exp.group_contains(ZeroDivisionError)