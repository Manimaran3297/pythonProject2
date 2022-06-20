import time

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains

from Utilities.CustomLogger import LogGen
from Utilities.ReadProperties import ReadConfig
from pageObjects.LoginPage import Login
from TC.conftest import setup
from TC.Loginfunction import loginfunction
from pageObjects.secure_Onboarding import Secure

class Test_001_Login(loginfunction):
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_homePageTitle(self, setup):
        data = loginfunction.login(self, setup)
        time.sleep(3)
        self.OS = Secure(data)
        print("start")
        self.OS.clickSystem()
        print("one")
        time.sleep(3)
        self.OS.clickMenu()
        print("two")
        time.sleep(3)
        self.OS.getTitle()
        print("three")
        a = ActionChains(data)
        m = data.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div[2]/div/div/div/div/div[1]/div[2]/img")
        a.move_to_element(m).perform()
        time.sleep(3)
        self.OS.getIcon()
        print("four")
        time.sleep(3)
        self.OS.getalltext()
        print("five")
        self.OS.edit()
        print("six")


