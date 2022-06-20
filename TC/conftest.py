"""
import pytest
from selenium import webdriver
@pytest.fixture()
def setup():
    driver = webdriver.Chrome(executable_path="/home/ticvictech/PycharmProjects/Sixvercel_project/Drivers/chromedriver")
    return driver
"""
import os.path
from datetime import datetime

from OpenSSL.rand import status
from py import test
from selenium import webdriver
import pytest
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from Utilities.CustomLogger import LogGen

logger = LogGen.loggen()

from termcolor import colored
@pytest.fixture()
def setup(browser):
    global driver

    if browser=='chrome':
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        yield driver
        #browser calling function
        #driver=webdriver.Chrome(executable_path="/Users/ticvictech/PycharmProjects/pythonProject2/Drivers/chromedriver")
        print("Launching Chrome browser")
    elif browser=='firefox':
        driver=webdriver.Firefox(executable_path="/Users/ticvictech/PycharmProjects/pythonProject2/Drivers/geckodriver")
        yield driver
        print("Launching Firefox browser")
    else:
        driver = webdriver.Chrome(executable_path="/Users/ticvictech/PycharmProjects/pythonProject2/Drivers/chromedriver")
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser", action='store', default="chrome")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

# PATH = lambda p:os.path.abspath(os.path.join(os.path.dirname(__file__),'..',p))
#
# @pytest.mark.hookwrapper
# def pytest_runtest_makereport(item):
#     """
#     Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
#     :param item:
#     """
#     pytest_html = item.config.pluginmanager.getplugin('html')
#     outcome = yield
#     report = outcome.get_result()
#     extra = getattr(report, 'extra', [])
#
#     if report.when == 'call' or report.when == "setup":
#         xfail = hasattr(report, 'wasxfail')
#         if (report.skipped and xfail) or (report.failed and not xfail):
#             add_name = '{}_{}'.format(report.nodeid.split("::")[1], datetime.now().strftime("%Y-%m-%d_%H.%M.%S"))
#             file_name = report.nodeid.replace("::","_")+".png"
#             print("file_name--",file_name)
#             cp_file_name = PATH('./Screenshots'+'/'+add_name +'.png')
#             print("CP_File_Name-", cp_file_name)
#             _capture_screenshot(cp_file_name)
#             if cp_file_name:
#                 html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
#                        'onclick="window.open(this.src)" align="right"/></div>' % cp_file_name
#                 extra.append(pytest_html.extras.html(html))
#         report.extra = extra
#
# #file:///Users/ticvictech/PycharmProjects/pythonProject2/Reports/TC/test_overlay.py_Test_001_Login_test_homePageTitle.png
# def _capture_screenshot(name):
#     print("name ", name)
#     driver.save_screenshot(name)
    #test.log(status, test.addScreenCapture(file));
# @pytest.fixture(scope='session', autouse=True)
# def browser():
#     global driver
#     if driver is None:
#         driver = webdriver.Firefox()
#     yield driver
#     return driver
#
# #test_screenshot.py
#
# def test_screenshot_on_test_failure(browser):
#     # driver = webdriver.Firefox()
#     browser.get("https://google.com")
#     assert False
@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    if not os.path.exists('Reports'):
        os.makedirs('Reports')
    config.option.htmlpath = 'reports/report_' + datetime.now().strftime("%d-%m-%Y_%H-%M-%S") + ".html"
