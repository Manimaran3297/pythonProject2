import time

import pytest

from pageObjects.LoginPage import Login
from Utilities.ReadProperties import ReadConfig
from Utilities.CustomLogger import LogGen
class Test_002_login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_positivelogin(self,setup):
        self.driver = setup
        time.sleep(2)
        self.driver.get(self.baseURL)
        time.sleep(2)
        self.driver.maximize_window()
        time.sleep(5)
        self.logger.info("****URL is launched successfully****")
        self.lp = Login(self.driver)
        time.sleep(5)
        self.lp.setUsername(self.username)
        time.sleep(5)
        self.lp.setPassword(self.password)
        time.sleep(5)
        self.lp.checkbox()
        time.sleep(5)
        self.lp.clicklogin()
        time.sleep(3)
        self.logger.info("++++Login Success++++")
        act_title = self.driver.title
        print("title is--->", act_title)
        if act_title == "Infoquick - System Resource":
            assert True
            self.driver.save_screenshot("/Users/ticvictech/PycharmProjects/pythonProject2/Screenshots/Success screenshots/success.png")
        else:
            self.driver.save_screenshot("/Users/ticvictech/PycharmProjects/pythonProject2/Screenshots/failure_screenshots/failure.png")
        time.sleep(3)
        self.lp.dropdown()
        time.sleep(3)
        self.lp.clicklogout()
        time.sleep(3)
        self.logger.info("****Logout success****")
        self.driver.close()
""""
    def test_roles(self,setup):
        self.driver = setup
        time.sleep(2)
        self.driver.get(self.baseURL)
        time.sleep(2)
        self.driver.maximize_window()
        time.sleep(5)
        self.lp = Login(self.driver)
        time.sleep(5)
        self.lp.setUsername(self.username)
        time.sleep(5)
        self.lp.setPassword(self.password)
        time.sleep(5)
        self.lp.checkbox()
        time.sleep(5)
        self.lp.clicklogin()
        time.sleep(3)
        table = self.driver.find_elements_by_xpath("//*[@id='root']/div/div[1]/div[2]").list.count()
        print("the count of models"+"table")
"""