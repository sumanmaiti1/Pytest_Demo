def setup_module(module):
    print('open browser')

def teardown_module(module):
    print('close browser')

def setup_function(function):
    print('open Flipkart')

def teardown_function(function):
    print('close Flipkart')

class TestDemo:
    def test_1(self):
        print('function 1')
        print('hook function do not work with Instance method')

    @classmethod
    def test_2(cls):
        print('function 2')
        print('hook function do not work with Class method')

    @staticmethod
    def test_3():
        print('function 3')

    @staticmethod
    def test_4():
        print('function 4')

    @staticmethod
    def test_5():
        print('function 5')

    @staticmethod
    def test_6():
        print('function 6')