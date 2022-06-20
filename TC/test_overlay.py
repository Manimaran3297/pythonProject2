import time

import pytest
from selenium import webdriver

from Utilities.CustomLogger import LogGen
from Utilities.ReadProperties import ReadConfig
from pageObjects.LoginPage import Login
from TC.conftest import setup
from TC.Loginfunction import loginfunction
from pageObjects.OverlayAdresses import overlay


class Test_001_Login(loginfunction):
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_homePageTitle(self, setup):
        data = loginfunction.login(self, setup)
        time.sleep(3)
        self.OS = overlay(data)
        print("hello")
        time.sleep(5)
        self.OS.clickSystem()
        print("how r u ")
        time.sleep(5)
        self.OS.clickMenu()
        print("good bye")
        time.sleep(5)
        self.OS.getTitle()
        print("success")
        self.OS.tableCount()
        print("good start")