# -------------------- Thumb Rule --------------------
# Every Python file/Module must Start with either "test_" or "_test".
# Every Python function must Start with either "test_".
# Run with pytest or py.test
# Run single file : pytest test_first_pytest.py
# Run multiple file pytest : python -m pytest -vs demo_file_test.py test_first_pytest.py
# Run multiple file pytest : pytest -vs demo_file_test.py test_first_pytest.py
def first_func():
    print("inside first function")


def second_function():
    print("inside second function")


def test_third_function():
    print("inside third function")


def fourth_function_test():
    print("inside fourth function")
