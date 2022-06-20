import time

from pageObjects.LoginPage import Login
from TC.conftest import setup
from Utilities.CustomLogger import LogGen
from Utilities.ReadProperties import ReadConfig


class loginfunction:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def login(self, setup):
        data = loginfunction.LaunchURL(self, setup)
        time.sleep(5)
        self.lp = Login(data)
        self.logger.info("******* Enter the Username *******" + self.username)
        self.lp.setUsername(self.username)
        time.sleep(2)
        self.logger.info("******* Enter the Password *******" + self.password)
        self.lp.setPassword(self.password)
        self.logger.info("******* Click the Captcha checkbox *******")
        self.lp.checkbox()
        time.sleep(4)
        self.lp.clicklogin()
        time.sleep(3)
        self.logger.info("********** Click on Login button **************")
        # time.sleep(3)
        # self.lp.dropdown()
        # time.sleep(3)
        # self.lp.clicklogout()
        # self.logger.info("*****logout option working fine*****")
        return data

    def LaunchURL(self, setup):
        self.logger.info("************ Launch the Browser **************")
        self.driver = setup
        self.driver.get(self.baseURL)
        return self.driver

