import time

from selenium.webdriver.common.by import By

from Utilities.CustomLogger import LogGen
from TC.Loginfunction import loginfunction
from Utilities import CustomLogger
from pageObjects.upload_os import Upload_os


class Test_002_Uploadimage(loginfunction):
    logger = LogGen.loggen()

    def test_upload(self, setup):
        data = loginfunction.login(self, setup)
        time.sleep(10)
        print("***** start uploading OS Image **** ")
        time.sleep(5)
        data.OS = Upload_os(data)
        print("****selecting OS Images****")
        time.sleep(10)
        #self.driver.find_element_by_xpath("//*[@id='root']/div/div[2]/div[1]/div[2]/div/ul/li[2]/div/i").click()
        #self.driver.find_element_by_xpath("//*[@id='root']/div/div[2]/div[1]/div[2]/div/ul/li[5]/div").click()
        #self.driver.find_element(by=By.XPATH, value="//*[@id='root']/div/div[2]/div[1]/div[2]/div/ul/li[2]/div/i").click()
        #print("hello world")
        #self.driver.find_element(by=By.XPATH, value="//*[@id='root']/div/div[2]/div[1]/div[2]/div/ul/li[5]/div").click()
        print("world cup")
        #data.OS.clickSystem()
        time.sleep(5)
        data.OS.clickMenu()
        print("**** select upload OS")
        time.sleep(2)
        data.OS.clickSubmenu()
        time.sleep(2)
        act_title = data.title
        if act_title == "Infoquick - OS Images":
            print("overlay page opened successfully")
            data.OS.clickadd()
            time.sleep(2)
            data.OS.setName()
            time.sleep(2)
            data.OS.setDropdown()
            time.sleep(2)
            data.OS.setDescription()
            time.sleep(2)
            data.OS.clickSubmit()
            time.sleep(2)
            data.OS.clickHtmlurl()
            time.sleep(2)
            print("Url is a required field")
            time.sleep(2)
            print("Upload Os Image not created")
            data.OS.clickCancel()
            time.sleep(2)
            print("Upload Os Images canceled")


