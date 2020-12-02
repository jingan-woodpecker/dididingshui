# coding:utf-8

from page.login_page import LoginPage


class LoginHandle(object):

    def __init__(self, driver):
        self.driver = driver
        self.login_p = LoginPage(self.driver)

    def send_username(self, username):
        self.login_p.user_element().send_keys(username)

    def send_password(self, password):
        self.login_p.password_element().send_keys(password)

    def click_login_button(self):
        self.login_p.login_button_element().click()

    def get_login_text(self, error_info):
        if error_info == "longin_error_text":
            return self.login_p.login_text_element().text




