# coding:utf-8

from base.find_element_way import FindElementWay


class LoginPage(object):

    def __init__(self, driver):
        self.find_way = FindElementWay(driver)

    def user_element(self):
        return self.find_way.get_element("username")

    def password_element(self):
        return self.find_way.get_element("password")

    def login_button_element(self):
        return self.find_way.get_element("login_button")

    def login_text_element(self):
        return self.find_way.get_element("longin_error_text")


# if __name__ == '__main__':
#     login = LoginPage()
