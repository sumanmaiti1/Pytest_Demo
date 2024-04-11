# This file , class, functions will also be considered by Pytest as we have made related changes in pytest.ini file
# pytest test_junitxml.py --junit-xml='Report/junitxml.xml'   ---> This will create junit-xml report in New Report folder
# pytest test_junitxml.py --junit-xml='Report/Junit/junitxml.xml'   ---> This will create junit-xml report in New Junit subfolder under Report folder

class KrishnaDemo:
    @staticmethod
    def krishna_func1():
        print("inside krishna func 1")

    @classmethod
    def krishna_func2(cls):
        print("inside krishna func 2")

    def test_func3(self):
        print("inside Test func 2")
