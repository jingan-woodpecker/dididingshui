# coding:utf-8

from util.read_ini import ReadIni


class FindElementWay(object):

    def __init__(self, driver):
        self.driver = driver

    def get_element(self, key):
        read_ini = ReadIni()
        data = read_ini.get_value(key)
        by = data.split(":")[0]
        value = data.split(":")[1]
        try:
            if by == "name":
                return self.driver.find_element_by_name(value)
            if by == "id":
                return self.driver.find_element_by_id(value)
            if by == "class":
                return self.driver.find_element_by_class_name(value)
            if by == "link":
                return self.driver.find_element_by_link(value)
            if by == "xpath":
                return self.driver.find_element_by_xpath(value)
        except:
            return None

# if __name__ == '__main__':
#     find_ele = FindElementWay()
#     value01 = find_ele.get_element("name")
#     print(value01)




