import pytest
@pytest.fixture(scope='module',autouse=True)
def setup_teardown1():
    print('\nClose all Previous Browsers')
    print('Open new Browser')
    yield
    print('Test Completed')

@pytest.fixture(scope='class',params=('Flipkart','Amazon','Snapdeal','ShopClues','Myntra','Meesho','Nykaa','Ebay'),autouse=False)
def setup_teardown2(request):
    print(f'Open {request.param}')
    yield
    print(f'Close {request.param}')