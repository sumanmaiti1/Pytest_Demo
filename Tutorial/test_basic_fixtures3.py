import pytest

@pytest.fixture(scope='class',autouse=True)
def setup_teardown1():
    print('\nClose all Previous Browsers')
    print('Open new Browser')
    yield
    print('Test Completed')

@pytest.fixture(scope='class',params=('Flipkart','Amazon'))
def setup_teardown2(request):
    print(f'Open {request.param}')
    yield
    print(f'Close {request.param}')

class TestEcommerce:
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
