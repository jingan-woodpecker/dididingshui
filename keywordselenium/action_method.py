# coding:utf-8

import time
from selenium import webdriver
from base.find_element_way import FindElementWay


class ActionMethod(object):

    # 打开浏览器
    def open_browser(self, browser):
        if browser == "chrome":
            self.driver = webdriver.Chrome()
            self.driver.maximize_window()
        elif browser == "firefox":
            self.driver = webdriver.Firefox()
            self.driver.maximize_window()
        else:
            self.driver = webdriver.Edge()
            self.driver.maximize_window()

    # 获取url
    def get_url(self, url):
        self.driver.get(url)

    # 定位元素
    def get_element(self, key):
        find_element = FindElementWay(self.driver)
        element = find_element.get_element(key)
        return element

    # 输入框输入内容
    def send_keys(self, value, key):
        element = self.get_element(key)
        element.send_keys(value)

    # 点击元素
    def click_button(self, key):
        element = self.get_element(key)
        element.click()

    # 等待
    def sleep_time(self):
        time.sleep(3)

    # 关闭浏览器
    def close_browser(self):
        self.driver.close()

    # 获取title信息
    def get_title(self):
        title = self.driver.title
        return title

