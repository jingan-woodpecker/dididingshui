# coding:utf-8

import unittest,time
from selenium import webdriver


class Test(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get('https://md.dididingshui.com')
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.close()

    def test_order(self):
        user_ele = self.driver.find_element_by_name('account')
        user_ele.send_keys('18836123123')
        pw_ele = self.driver.find_element_by_id("p")
        pw_ele.send_keys('888888')
        click_button = self.driver.find_element_by_class_name('layui-btn')
        click_button.click()

        # 点击订单管理
        order_manager_ele = self.driver.find_element_by_class_name('fi-manage-order')
        order_manager_ele.click()

        # 点击订单列表
        order_list_ele = self.driver.find_element_by_xpath('//*[@class="item-main"]/ul/li[1]/a/em[2][text()="订单列表"]')
        order_list_ele.click()

        # 点击业务受理
        business_accept = self.driver.find_element_by_xpath('//*[@class="navContainer"]/ul/li[1]/a/em[text()="业务受理"]')
        business_accept.click()

        # 点击客户名称
        customer_name = self.driver.find_element_by_id('memberName')
        customer_name.click()
        time.sleep(2)

        # 点击客户编号搜索框
        customer_code = self.driver.find_element_by_id('alertSelectClient_like_memberCode_')
        customer_code.send_keys('KHzd0001')

        check_customer = self.driver.find_element_by_xpath('//*[@id="alertSelectClient_alertContainer"]/div[2]/div/div/div/div[2]/div/div[1]/div[3]/div[2]/table/tbody/tr/td/div/div/span[1]')
        check_customer.click()
        time.sleep(2)

        # 点击确认按钮
        click_confirm = self.driver.find_element_by_xpath('//*[@id="alertSelectClient_alertContainer"]/script/div[3]/button[2]/em')
        click_confirm.click()
        time.sleep(2)




if __name__ == '__main__':
    unittest.main()






