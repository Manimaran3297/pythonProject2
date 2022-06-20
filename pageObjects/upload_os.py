#import string
import time
#from _ast import Assert
#from lib2to3.pgen2 import driver
#from tokenize import String

#from selenium.webdriver import ActionChains

class Upload_os:
    button_sdwan_xpath = "//*[@id='root']/div/div[2]/div[1]/div[2]/div/ul/li[6]/div/span"
    menu_overlay_xpath = "//*[@id='rc-menu-uuid-77541-2-4-popup']/li[1]/span/a"
    # submenu_upload_image_xpath = "//*[@id='rc-menu-uuid-17985-1-osimages-popup']"
    # dropdown_upload_xpath = "//*[@id='root']/div/div[2]/div[1]/div[2]/div/ul/li[5]/div/i"
    # button_add_xpath = "//*[@id='root']/div/div[2]/div[2]/div/div[2]/div[2]/div/button[1]/img"
    # textbox_image_name = "name"
    # dropdown_device_type_xpath = "/html/body/div[5]/div/div[2]/div/div[2]/div[2]/form/div[2]"
    # dropdown_device_subtype_xpath = "/html/body/div[5]/div/div/div/div[2]/div[1]/div/div/div[2]"
    # textbox_description_xpath = "/html/body/div[5]/div/div[2]/div/div[2]/div[2]/form/div[3]"
    # button_submit_xpath = "/html/body/div[4]/div/div[2]/div/div[2]/div[3]/button[1]"
    # button_cancel_xpath = "/html/body/div[4]/div/div[2]/div/div[2]/div[3]/button[2]"
    # textbox_html_xpath = "/html/body/div[4]/div/div[2]/div/div[2]/div[2]/form/div[4]/div/div[2]/div/div/div/div/div/div/input"
    def __init__(self, driver):
        self.driver = driver

    def clickSdwan(self):
        self.driver.find_element_by_xpath(self.button_sdwan_xpath).click()
        time.sleep(5)

    def clickOverlay(self):
        self.driver.find_element_by_xpath(self.menu_overlay_xpath).click()
        time.sleep(2)

    # def clickSubmenu(self):
    #     self.driver.find_element_by_xpath(self.submenu_upload_image_xpath).click()
    #     time.sleep(2)
    #     self.driver.find_element_by_xpath("self. dropdown_upload_xpath").click()
    #     time.sleep(2)
    # def clickadd(self):
    #     self.driver.find_element_by_xpath("self.button_add_xpath").click()
    #     time.sleep(2)
    #
    # def setName(self):
    #     self.driver.find_element_by_name("self.textbox_image_name").click()
    #     time.sleep(2)
    #     self.driver.find_element_by_name("self.textbox_image_name").send_keys("Test1")
    #     time.sleep(2)
    #
    # def setDropdown(self):
    #     self.driver.find_element_by_xpath("self.dropdown_device_type_xpath").click()
    #     time.sleep(2)
    #     self.driver.find_element_by_xpath("self.dropdown_device_subtype_xpath").click()
    #     time.sleep(2)
    #
    # def setDescription(self):
    #     self.driver.find_element_by_xpath("self.textbox_description_xpath").click()
    #     time.sleep(2)
    #
    # def clickSubmit(self):
    #     self.driver.find_element_by_xpath("self.button_submit_xpath").click()
    #     time.sleep(2)
    #
    # def clickHtmlurl(self):
    #     self.driver.find_element_by_xpath("self.textbox_html_xpath").click()
    #     time.sleep(2)
    #
    # def clickCancel(self):
    #     self.driver.find_element_by_xpath("self.button_cancel_xpath").click()
    #     time.sleep(2)