import os
import pytest
import allure
from datetime import datetime as dt
from selenium import webdriver

driver = None

@pytest.fixture(scope='class',autouse=True)
def setup_teardown1(request):
    print('\nClose all Previous Browsers')
    print('Open new Browser')
    driver = webdriver.Chrome()
    request.cls.driver = driver
    driver.get("https:\\google.com")
    yield
    print('Test Completed')
    driver.quit()

@pytest.fixture(scope='class',params=('Flipkart','Amazon','Snapdeal','ShopClues','Myntra','Meesho','Nykaa','Ebay'),autouse=False)
def setup_teardown2(request):
    print(f'Open {request.param}')
    yield
    print(f'Close {request.param}')


# --------------- Adding Screenshots only for the steps which are failed --------------
# ----------for Allure -  https://github.com/pytest-dev/pytest/issues/230 ---------
# ----------for html-report -  https://github.com/rafitur2/Python-Pytest-Selenium-HTML-report-with-multiple-screenshots/blob/master/conftest.py ---------


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    try:
        global driver
        pytest_html = item.config.pluginmanager.getplugin('html')
        outcome = yield
        rep = outcome.get_result()
        extra = getattr(rep, 'extras', [])

        # ----------- Only Take screenshots when test doesn't pass -----------
        if not rep.passed:
            screenshot_path = "D:\\Work\\Projects\\Python\\Pytest\\Tutorial\\Report\\screenshots"
            if not os.path.exists(screenshot_path):
                os.makedirs(screenshot_path)
            # file_name = report.nodeid.replace("::", "_") + ".png"
            file_name = screenshot_path + "\\" + "Failure_" + str(dt.now().strftime("%H_%M_%S")) + ".png"
            driver.get_screenshot_as_file(file_name)
            if file_name:
                html_report = f'<div><img src=%s alt="screenshot" style="width:300px; height:200px; " ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html_report))
            rep.extra = extra

        setattr(item, "rep_" + rep.when, rep)
        return rep
    except Exception as err:
        print(f' Runtime exception generated. Err: {err}\n')


# ------------------- For allure screenshots ------------------
@pytest.fixture(scope='function', autouse=True)
def log_on_failure(request):
    try:
        yield
        item = request.node
        current_timestamp = str(dt.now().strftime("%H_%M_%S"))
        if not item.rep_call.passed:
            allure.attach(request.cls.driver.get_screenshot_as_png(), name='Screenshot_' + current_timestamp, attachment_type=allure.attachment_type.PNG)
    except Exception as err:
        print(f' Runtime exception generated. Err: {err}\n')


# --------------- for html Report Title ---------------
def pytest_html_report_title(report):
    try:
        report.title = "Pytest Automation Execution :- " + str(dt.now().strftime("%d-%b-%Y %H:%M:%S"))
    except Exception as err:
        print(f' Runtime exception generated. Err: {err}\n')
