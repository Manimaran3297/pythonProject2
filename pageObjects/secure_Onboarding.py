import time

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common import keys
from webdriver_manager import driver

from Utilities.CustomLogger import LogGen


class Actions:
    pass


class Secure:
    button_system_xpath = "//span[text()='SDWAN']"
    menu_secure_xpath = "/html/body/div/div/div[2]/div[1]/div[2]/div/ul/li[6]/ul/li[2]/span/a"
    title_xpath = "//div[@class='w-full p-4 overflow-scroll']//div"
    secure_class_xpath = "//div[@class='w-full p-4 overflow-scroll']//div"
    text_xpath = "//div[@class='ibs-card-body w-full h-full']//div"
    edit_xpath = "//*[@id='root']/div/div[2]/div[2]/div[2]/div/div/div/div/div[1]/div[2]/img"
    gettitle_xpath = "//*[@class='ant-modal-header']/div"
    getcontent_xpath = "//*[@class='ant-form ant-form-horizontal w-full flex flex-col']/span/label"
    checkbox_xpath = "/html/body/div[3]/div/div[2]/div/div[2]/div[2]/form/span/label"
    content_xpath = "//*[@class='w-full ibs-field-div']/div/div/div/div"
    content1_xpath = "//*[@class='flex']/span"
    content4_xpath = "//*[@class='ibs-form-label']/span"
    content3_xpath = "/html/body/div[3]/div/div[2]/div/div[2]/div[2]/form/div[2]/div/div/div/div/div"
    logger = LogGen.loggen()
    onboard_number_xpath = "//*[@class='ant-input-number-input-wrap']/input"
    button_xpath = "//*[@class='ant-modal-footer']/button"
    def __init__(self, driver):
        self.driver = driver

    def clickSystem(self,):
        self.driver.find_element_by_xpath(self.button_system_xpath).click()
        time.sleep(5)

    def clickMenu(self,):
        self.driver.find_element_by_xpath(self.menu_secure_xpath).click()
        time.sleep(2)

    def getTitle(self,):
        text = self.driver.find_elements_by_xpath(self.title_xpath)
        act_title = self.driver.title
        print("title is--->", act_title)

        if act_title == "secure onboarding":
            assert True
        else:
            print("fail")
        for e in text:
            contain_class = e.get_attribute("class")
            if "flex-auto text-white" in contain_class:
                pass
                data = e.text
                if data == "Secure Onboarding":
                    print("the title is----->",data)
                else:
                    print("fail")

    def getIcon(self,):
        text = self.driver.find_elements_by_xpath(self.title_xpath)
        for e in text:
            contain_class = e.get_attribute("class")
            #print("the classes are", contain_class)
            if "cursor-pointer" in contain_class:
                pass
                data = self.driver.find_element_by_xpath("//img[@alt='edit']").get_attribute('class')
                print("the data's are--->", data)
                if data == "ant-tooltip-open":
                    print("the title is----->",data)
                    print("the tooltip verification passed")
                else:
                    print("fail")
                    print("the tooltip verification failed")

    def getalltext(self):
        text = self.driver.find_elements_by_xpath(self.text_xpath)
        for e in text:
            contain_class = e.get_attribute("class")
            print("the classes are", contain_class)
            #for e in text:
                #contain_class = e.get_attribute("class")
            if "w-100 flex space-x-6" in contain_class:
                pass
                data = e.text
                print("the text is----->", data)
                str = data
                arr = str.split(' ')
                print("the array-->", arr[0])
                print("the array-->", arr[1])

                content = self.driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div[2]/div/div/div/div/div[2]/div/span").text
                print("the Hint is--->", content)
                # str = content
                # arr1 = str.split()
                # print("the array-->", arr1)

            else:
                print("fail")

    def edit(self):
        self.driver.find_element_by_xpath(self.edit_xpath).click()
        print("first step")
        text = self.driver.find_element_by_xpath(self.gettitle_xpath).text
        print("the title is ", text)
        if text == "Add/Edit Secure Onboarding":
            print("Title verification successfully done")
        else:
            print("Title verification failed")
        self.driver.find_element_by_xpath(self.checkbox_xpath).click()
        text1 = self.driver.find_element_by_xpath(self.getcontent_xpath).get_attribute('class')
        print("the contents are", text1)
        if "checked" in text1:
            print("Secure Onboarding is enabled")
        else:
            print("Secure Onboarding is disabled")
        text2 = self.driver.find_element_by_xpath(self.content1_xpath).text
        print("the field is", text2)
        if "*" in text2:
            print("the field is mandatory")
        else:
            print("the field is not mandatory")

        text3 = self.driver.find_element_by_xpath(self.content3_xpath).text
        print("the default onboarding window field is", text3)
        if "*" in text3:
            print("the field is mandatory")
        else:
            print("the field is not mandatory")
        time.sleep(5)
        # textbox = self.driver.find_element_by_xpath(self.onboard_number_xpath).click()
        var = self.driver.find_element_by_xpath(self.onboard_number_xpath)
        action = ActionChains(self.driver)
        # double click operation
        action.double_click(var).perform()
        time.sleep(2)
        # var.send_keys(Keys.DELETE)
        #both works for removing text from textbox field
        var.send_keys(Keys.BACKSPACE)
        var.send_keys("10")
        buttons = self.driver.find_elements_by_xpath(self.button_xpath).text()
        print("the buttons available are", buttons)
        # Actions  a=Actions(driver);
        # a.moveToElement(self.driver.find_element_by_xpath(self.onboard_number_xpath)).doubleClick().click().sendkeys(keys.BACK_SPACE).perform();
        print("i am back")

        print("Future Automation Test Engineers")