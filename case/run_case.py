# coding:utf-8

import os
import unittest
import HTMLTestRunner

class RunCase(unittest.TestCase):

    def test_case01(self):
        case_path = os.path.join(os.getcwd())
        suite = unittest.defaultTestLoader.discover(case_path, "login_keyword_*")
        unittest.TextTestRunner().run(suite)

if __name__ == '__main__':
    file_path = os.path.join(os.getcwd()+"/report/"+"first_case.html")
    f = open(file_path,"wb")
    suite = unittest.TestLoader().loadTestsFromTestCase(RunCase)
    runner = HTMLTestRunner.HTMLTestRunner(stream=f,title="自动化测试报告",description="登录case",verbosity=2)
    runner.run(suite)

