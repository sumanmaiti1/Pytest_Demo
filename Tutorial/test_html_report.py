# pip install pytest-html   --->  it will need pytest-html package to be installed
# pytest test_html_report.py::SumanDemo --html="Report/HtmlReports/html_report.html"   --->
#                           This will create junit-xml report in New Junit subfolder under Report folder
class SumanDemo:
    @staticmethod
    def suman_func1():
        print("inside SumanFunction 1")
        assert True
    @classmethod
    def suman_func2(cls):
        print("inside SumanFunction 2")

    def suman_func3(self):
        print("inside SumanFunction 3")

    def suman_func4(self):
        print("inside SumanFunction 4")
        assert 2==3