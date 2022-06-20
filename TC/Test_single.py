import time

import pytest
from selenium import webdriver

from Utilities.CustomLogger import LogGen
from Utilities.ReadProperties import ReadConfig
from pageObjects.LoginPage import Login
from TC.conftest import setup
from TC.Loginfunction import loginfunction


class Test_001_Login(loginfunction):
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_homePageTitle(self, setup):
        data = loginfunction.LaunchURL(self, setup)

        time.sleep(3)
        act_title = data.title
        time.sleep(3)

        # if act_title == "Infoquick - Login34":
        #     data.save_screenshot(
        #         "/Users/ticvictech/PycharmProjects/pythonProject2/Screenshots/Success screenshots/success.png")
        #     assert True
        #     data.close()
        #     self.logger.info("*************Home Page Title verification is passed *************")
        # else:
        #     data.save_screenshot(
        #         "/Users/ticvictech/PycharmProjects/pythonProject2/Screenshots/failure_screenshots/failure.png")
        #     data.close()
        #     self.logger.info("********** Home Page Title verification is Failed ***************")
        #     assert False

    @pytest.mark.sanity
    def test_login(self, setup):

        data = loginfunction.login(self, setup)
        time.sleep(5)

        act_title = data.title
        print("act_title --", act_title)
        time.sleep(3)
        data.close()
        if act_title == "Infoquick - System Resources":
            self.logger.info("************** Login Page URTitle verification Passed ***************")
            print("************** Login Page URTitle verification Passed ***************")
            assert True
        else:
            self.logger.info("*************** Login Page Title verification ******************** ")
            print("*************** Login Page Title verification ******************** ")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_overlay(self, setup):
        data = loginfunction.LaunchURL(self, setup)
        data = loginfunction.login(self, setup)
        time.sleep(3)


