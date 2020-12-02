# coding:utf-8

import configparser


# 加载和读取配置文件
class ReadIni(object):

    def __init__(self, file_name=None, node=None):
        if file_name is None:
            file_name = r"D:\Pycharm\pythonProject\rtxProject\config\LocalElement.ini"
        if node is None:
            self.node = "MdLoginElement"
        else:
            self.node = node
        self.cf = self.load_ini(file_name)

    def load_ini(self, file_name):
        cf = configparser.ConfigParser()
        cf.read(file_name)
        return cf

    def get_value(self, key):
        data = self.cf.get(self.node, key)
        return data

if __name__ == '__main__':
    read_ini = ReadIni(r"D:\Pycharm\pythonProject\rtxProject\config\LocalElement.ini")
    data_value = read_ini.get_value("username")
    print(data_value)














