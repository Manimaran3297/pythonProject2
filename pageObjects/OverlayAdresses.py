import time

import self as self

from Utilities.CustomLogger import LogGen


class overlay:
    button_system_xpath = "//span[text()='SDWAN']"
    #self.driver.find_element_by_xpath("(//span[@class='ant-menu-title-content']/a)[1]").text
    #print(Alerttext)
    #menu_overlay_xpath = "(//span[@class='ant-menu-title-content']/a)[1]"
    menu_overlay_xpath = "/html/body/div[1]/div/div[2]/div[1]/div[2]/div/ul/li[6]/ul/li[1]/span/a"
    title_xpath = "(//div[@class='flex items-start']//div)"
    tablecount_xpath = "//div[@class='flex items-start']//div"
    logger = LogGen.loggen()

    def __init__(self, driver):
        self.driver = driver

    def clickSystem(self,):
        self.driver.find_element_by_xpath(self.button_system_xpath).click()
        time.sleep(5)

    def clickMenu(self,):
        self.driver.find_element_by_xpath(self.menu_overlay_xpath).click()
        time.sleep(2)
    #verifying the title of table
    def getTitle(self,):
        text = self.driver.find_elements_by_xpath(self.title_xpath)
        act_title = self.driver.title
        print("title is--->", act_title)

        if act_title == "Infoquick - Overlay Addresses3":
            #self.driver.save_screenshot("/Users/ticvictech/PycharmProjects/pythonProject2/Screenshots/Success screenshots/success.png")
            assert True
            print("pass")
            #text.close()
            #self.logger.info("*************Home Page Title verification is passed *************")
        else:
            #self.driver.save_screenshot("/Users/ticvictech/PycharmProjects/pythonProject2/Screenshots/failure_screenshots/failure.png")
            print("fail")
            #text.close()
            #self.logger.info("********** Home Page Title verification is Failed ***************")
            #assert False
        # time.sleep(5)
        # text1 = text
        # total_count = text1.count()
        # print("count is--->", total_count)
        #print("class names are--->", text)
        for e in text:
            contain_class = e.get_attribute("class")
            #print(contain_class)
            if "ibs-card-title" in contain_class:
                pass
                data = e.text
                if data == "Core Overlay IP Management123" or data == "Control Plane Overlay IP Management":
                    print(data)

                else:
                    print("fail")
                #print(contain_class)
        #print("class names are----->",text)
        #self.driver.find_elements_by_xpath(self.title_xpath)
        time.sleep(5)

    def tableCount(self,):
        name = self.driver.find_elements_by_xpath(self.tablecount_xpath)
        act_title = self.driver.title
        print("title is--->", act_title)
        for e in name:
            contain_class = e.get_attribute("class")
            print(contain_class)
            if "text-xs flex-auto" in contain_class:
                pass
                count = e.text
                if count == "1 to 1 of 1" or count == "1 to 4 of 4":
                    print(count)

                else:
                    print("fail")