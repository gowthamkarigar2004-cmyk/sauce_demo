
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):

    #locators
    email = (By.ID,'user-name')
    password = (By.ID,'password')
    lgn_btn = (By.XPATH,'//input[@class="submit-button btn_action"]')


    #actions
    def enter_username(self,email_value):
        self.send_keys(self.email,email_value)


    def enter_password(self,password_value):
        self.send_keys(self.password,password_value)


    def click_login(self):
        self.click(self.lgn_btn)
