from BaseApp import BasePage
from selenium.webdriver.common.by import By

class HerokuAppLocators:
    
    USERNAME = (By.ID, 'username')
    PASSWORD = (By.ID, 'password')
    LOGIN_BUTTON = (By.CLASS_NAME, 'radius')
    INFO_MESSAGE = (By.XPATH, '//*[@id="flash"]')
    LOGOUT_BUTTON = (By.XPATH, '//*[@id="content"]/div/a')


class HerokuHelper(BasePage):

    def enter_login(self, login):
        login_field = self.find_element(HerokuAppLocators.USERNAME)
        login_field.send_keys(login)
        return login_field

    def enter_password(self, password):
        password_field = self.find_element(HerokuAppLocators.PASSWORD)
        password_field.send_keys(password)
        return password_field    

    def click_on_the_login_button(self):
        return self.find_element(HerokuAppLocators.LOGIN_BUTTON,time=2).click()

    def click_on_the_logout_button(self):
        return self.find_element(HerokuAppLocators.LOGOUT_BUTTON,time=2).click()

    def check_info_bar(self):
        info_bar = self.find_element(HerokuAppLocators.INFO_MESSAGE,time=2)
        return info_bar
