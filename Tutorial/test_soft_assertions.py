# pip install pytest-soft-assertions   --> this package is needed for Soft Assertions
# pytest test_soft_assertions.py --html='Report/HtmlReports/html_report.html' --soft-asserts   ---> This will execute in Soft Assertions mode

import pytest
def test_fun1():
    a,b,c = 2,3,4
    assert a==b-1,"This assertion is not True"
    assert a==b,"This assertion is not True"
    pytest.raises(AssertionError)
    assert "man" in "Suman","man is not inside Suman"
    assert "Sri Krishna".upper().__contains__("Krishna".upper())
    assert b==c, "This assertions is not True"