# coding:utf-8

import sys
sys.path.append(r'D:\Pycharm\pythonProject\rtxProject')
import unittest
import HTMLTestRunner
from case import login_keyword_case


class MdCase(unittest.TestCase):

    def test001_login_case(self):
        """ 登录用例 """
        run_case = login_keyword_case.LoginKeywordCase()
        run_case.run_main()


if __name__ == '__main__':
    file_path = r"D:\Pycharm\pythonProject\rtxProject\report\login_case.html"
    f = open(file_path,"wb")
    suite = unittest.TestLoader().loadTestsFromTestCase(MdCase)
    runner = HTMLTestRunner.HTMLTestRunner(stream=f,title="自动化测试报告",description="登录case结果",verbosity=2)
    runner.run(suite)




