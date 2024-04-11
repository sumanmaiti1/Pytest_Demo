# pytest -svrA -m student   --->   This will run all the tests under student marker
# pytest -svrA -m teacher   --->   This will run all the tests under teacher marker
# pytest -svrA -m "teacher or student"  --->   This will run all the tests under teacher and student marker
#  pytest -svrA -m "not student or teacher" test_pytest_marker.py  --->   This will run all the tests which is not Student but teacher marker
# pytest -svrA -k TestStudent   --->   This will run the TestStudent class tests using keyword
# pytest -svrA -m smoke  --->   This will run all the smoke tests
# pytest -svrA -m regression  --->   This will run all the regression tests
# pytest -svrA -m high  --->   This will run all the High Priority tests
# pytest -svrA -m "high and regression"  --->   This will run all the High Priority Regresion tests
# pytest -svrA -m "high and regression and student"  --->   This will run all the High Priority Regresion tests for Students

import pytest

@pytest.mark.student
class TestStudent():

    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.student
    @pytest.mark.high
    def test_enroll_student(self):
        print("Student enrolled")

    @pytest.mark.smoke
    @pytest.mark.student
    @pytest.mark.low
    def test_show_student_details(self):
        print("Student Details showed")

    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.student
    @pytest.mark.high
    def test_perform_test(self):
        print("Test Taken for Student")

    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.student
    @pytest.mark.high
    def test_teach_student(self):
        print("Students are taught")

    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.student
    @pytest.mark.medium
    def test_publish_result(self):
        print("Test result Published")


@pytest.mark.teacher
class TestTeacher():

    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.high
    def test_enroll_student(self):
        print("teacher enrolled")

    @pytest.mark.smoke
    @pytest.mark.low
    def test_show_teacher_details(self):
        print("teacher Details showed")

    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.high
    def test_perform_teaching(self):
        print("Teaching done forStudent")

    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.medium
    def test_upskill_teachers(self):
        print("Teachers are upskilled")

    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.high
    def test_pay_teachers(self):
        print("Teachers are Payed")