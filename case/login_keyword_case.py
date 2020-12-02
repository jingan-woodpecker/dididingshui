# coding:utf-8

import sys
sys.path.append(r"D:\Pycharm\pythonProject\rtxProject")
from util.excel_util import ExcelUtil
from keywordselenium.action_method import ActionMethod


class LoginKeywordCase(object):

    def run_main(self):
        self.action_method = ActionMethod()
        handle_excel = ExcelUtil(r"D:\Pycharm\pythonProject\rtxProject\config\loginkeyword.xls")
        case_lines = handle_excel.get_lines()

        if case_lines:
            for i in range(1, case_lines):
                is_run = handle_excel.get_cell_data(i, 3)
                if is_run == "yes":
                    method = handle_excel.get_cell_data(i, 4)
                    send_value = handle_excel.get_cell_data(i, 5)
                    handle_value = handle_excel.get_cell_data(i, 6)
                    expect_result_method = handle_excel.get_cell_data(i, 7)
                    expect_result = handle_excel.get_cell_data(i, 8)
                    self.run_method(method, send_value, handle_value)

                    if expect_result != "":
                        expect_value = self.get_expect_result_value(expect_result)
                        if expect_value[0] == "text":
                            result = self.run_method(expect_result_method)
                            if expect_value[1] in result:
                                handle_excel.write_value(i, "pass")
                            else:
                                handle_excel.write_value(i, "fail")
                        else:
                            print("无")
                    else:
                        print("case预期结果为空")


    def get_expect_result_value(self, data):
        return data.split("=")


    def run_method(self, method, send_value="", handle_value=""):
        method_value = getattr(self.action_method, method)
        if send_value == "" and handle_value != "":
            result = method_value(handle_value)
        elif send_value != "" and handle_value == "":
            result = method_value(send_value)
        elif send_value == "" and handle_value == "":
            result = method_value()
        else:
            result = method_value(send_value, handle_value)
        return result


# if __name__ == '__main__':
#     file_path = r"D:\Pycharm\pythonProject\rtxProject\report\login_case.html"
#     f = open(file_path,"wb")
#     suite = unittest.TestLoader().loadTestsFromTestCase(LoginKeywordCase)
#     runner = HTMLTestRunner.HTMLTestRunner(stream=f,title="自动化测试报告",description="登录case",verbosity=2)
#     runner.run(suite)

