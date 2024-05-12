# pip install pytest-allure   --> this package is needed for Parallel execution
# pytest allure_report.py --html='Report/HtmlReports/html_report.html' --alluredir Report/allure/allure-results --clean-alluredir -n 5   ---> This will execute with 5 workers parallaly
# allure.bat generate Report/allure/allure-results --clean -o Report/allure/allure-report

# ------------ for single allure html file run below ----------------------
# allure.bat generate --single-file Report/allure/allure-results --clean -o Report/allure/allure-report

import pytest
import allure

class TestEcommerce:
    def test_login_functionality(self):
        print("Login Functionality checked")
        assert 2==4

    def test_logout_functionality(self):
        print("Log out Functionality checked")
        assert 2==2

    def test_Signup_functionality(self):
        print("Sign Up Functionality checked")

    @pytest.mark.usefixtures()
    def test_search_product_functionality(self):
        print("Search product Functionality checked")

    @pytest.mark.usefixtures()
    def test_Create_order_functionality(self):
        print("Create Order Functionality checked")
        assert 3==4