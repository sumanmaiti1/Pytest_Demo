import pytest
class TestFlipkart:
    @staticmethod
    @pytest.fixture()
    def setup_teardown1():
        print('\nClose all Previous Browsers')
        print('Open new Browser')
        yield
        print('Test Completed')
    @staticmethod
    @pytest.fixture()
    def setup_teardown2():
        print('Open Flipkart')
        yield
        print('Close Flipkart')

    def test_login_functionality(self,setup_teardown1,setup_teardown2):
        print("Login Functionality checked")
    @pytest.mark.usefixtures('setup_teardown1','setup_teardown2')
    def test_logout_functionality(self):
        print("Log out Functionality checked")

    def test_Signup_functionality(self,setup_teardown1,setup_teardown2):
        print("Sign Up Functionality checked")

    @pytest.mark.usefixtures('setup_teardown1', 'setup_teardown2')
    def test_search_product_functionality(self):
        print("Search product Functionality checked")

    @pytest.mark.usefixtures('setup_teardown1', 'setup_teardown2')
    def test_Create_order_functionality(self):
        print("Create Order Functionality checked")

class TestAmazon:
    @staticmethod
    @pytest.fixture()
    def setup_teardown1():
        print('\nClose all Previous Browsers')
        print('Open new Browser')
        yield
        print('Test Completed')
    @staticmethod
    @pytest.fixture()
    def setup_teardown2():
        print('Open Amazon')
        yield
        print('Close Amazon')

    def test_login_functionality(self,setup_teardown1,setup_teardown2):
        print("Login Functionality checked")
    @pytest.mark.usefixtures('setup_teardown1','setup_teardown2')
    def test_logout_functionality(self):
        print("Log out Functionality checked")

    def test_Signup_functionality(self,setup_teardown1,setup_teardown2):
        print("Sign Up Functionality checked")

    @pytest.mark.usefixtures('setup_teardown1', 'setup_teardown2')
    def test_search_product_functionality(self):
        print("Search product Functionality checked")

    @pytest.mark.usefixtures('setup_teardown1', 'setup_teardown2')
    def test_Create_order_functionality(self):
        print("Create Order Functionality checked")