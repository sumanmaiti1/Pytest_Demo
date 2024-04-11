# pytest -svrA -k Test_Zomato   ---> to Run a particular class by keyword :
# pytest -svrA test_classlevel.py::Test_Swiggy::test_login  ---> to Run a particular function of particular class of particular module
# pytest -svrA test_classlevel.py -k Swiggy   ---> to run Class based on keyword in particular module
# pytest -svrA test_classlevel.py::Test_Swiggy -k order  ---> to run functions based on keyword in particular module and particular Class


class Test_Zomato():
    def test_login(self):
        print('Inside Login')

    def test_sign_up(self):
        print('Inside Sign Up')

    def test_order_food(self):
        print('Inside Order Food')

    def test_cancel_order(self):
        print("Calcel Order")

class Test_Swiggy():
    def test_login(self):
        print('Inside Login')

    def test_sign_up(self):
        print('Inside Sign Up')

    def test_order_food(self):
        print('Inside Order Food')

    def test_cancel_order(self):
        print("Calcel Order")