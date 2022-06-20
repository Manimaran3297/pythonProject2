
import time
class Login:
    textbox_username_xpath = "//*[@id='login-form']/div[1]/input"
    textbox_password_xpath = "//*[@id='login-form']/div[2]/span/input"
    login_button_xpath = "//*[@id='login-form']/div[4]/button"
    Checkbox_Login_xpath = "//*[@id='login-form']/div[3]/div/label/span[1]/input"
    link_Dropdown_xpath= "//*[@id='root']/div/div[1]/div[1]/div[2]/div[4]/span"
    button_logout_xpath = "/html/body/div[2]/div/div/ul/li[5]/span"
    headers_count_xpath = "//*[@id='root']/div/div[1]/div[2]"
    def __init__(self, driver):
        self.driver = driver

    def setUsername(self, username):
        self.driver.find_element_by_xpath(self.textbox_username_xpath).clear()
        time.sleep(2)
        self.driver.find_element_by_xpath(self.textbox_username_xpath).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element_by_xpath(self.textbox_password_xpath).clear()
        time.sleep(4)
        self.driver.find_element_by_xpath(self.textbox_password_xpath).send_keys(password)

    def checkbox(self):
        self.driver.find_element_by_xpath(self.Checkbox_Login_xpath).click()

    def clicklogin(self):
        self.driver.find_element_by_xpath(self.login_button_xpath).click()

    def dropdown(self):
        self.driver.find_element_by_xpath(self.link_Dropdown_xpath).click()

    def clicklogout(self):
        self.driver.find_element_by_xpath(self.button_logout_xpath).click()

    def headers(self):
        self.driver.find_element_by_xpath(self.headers_count_xpath)
