# coding:utf-8

from handle.login_handle import LoginHandle


class LoginBusiness(object):

    def __init__(self, driver):
        self.login_h = LoginHandle(driver)


    def user_base(self, username, password):
        self.login_h.send_username(username)
        self.login_h.send_password(password)
        self.login_h.click_login_button()

    def login_success(self, username, password):
        self.user_base(username, password)
        # if self.login_h.get_login_text(error_info) is None:
        #     return True
        # else:
        #     return False


