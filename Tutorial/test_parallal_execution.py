# pip install pytest-xdist   --> this package is needed for Parallel execution
# pytest test_parallal_execution.py --html='Report/HtmlReports/html_report.html' -n 5   ---> This will execute with 5 workers parallaly

import pytest

class TestEcommerce:
    def test_login_functionality(self):
        print("Login Functionality checked")

    def test_logout_functionality(self):
        print("Log out Functionality checked")

    def test_Signup_functionality(self):
        print("Sign Up Functionality checked")

    @pytest.mark.usefixtures()
    def test_search_product_functionality(self):
        print("Search product Functionality checked")

    @pytest.mark.usefixtures()
    def test_Create_order_functionality(self):
        print("Create Order Functionality checked")
