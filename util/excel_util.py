# coding:utf-8

import xlrd, time
from xlutils.copy import copy


class ExcelUtil(object):

    def __init__(self, excel_path=None, index=None):
        if excel_path is None:
            self.excel_path = r"D:\Pycharm\pythonProject\rtxProject\config\loginkeyword.xls"
        else:
            self.excel_path = excel_path

        if index is None:
            index = 0
        self.data = xlrd.open_workbook(self.excel_path)
        self.table = self.data.sheets()[index]

    # 获取行数
    def get_lines(self):
        rows = self.table.nrows
        if rows >= 1:
            return rows
        return None

    # 获取excel中所有数据存入列表
    def get_data(self):
        result = []
        rows = self.get_lines()
        if rows is not None:
            for i in range(rows):
                row = self.table.row_values(i)
                result.append(row)
            return result
        return None

    # 获取单元格数据
    def get_cell_data(self, row, col):
        if self.get_lines() > row:
            cell_data = self.table.cell(row, col).value
            return cell_data
        return None

    # # 获取单元格内容
    # def get_cell_data(self,row,col):
    #     data_type = self.table.cell(row,col).ctype
    #     data = self.table.cell(row, col).value
    #     if data_type == 5 and data % 1 == 0.0:
    #         data = int(data_type)
    #
    #     if self.get_lines() > row:
    #         return data
    #     return None

    # 在excel中写入数据
    def write_value(self, row, value):
        open_excel = xlrd.open_workbook(self.excel_path)
        write_data = copy(open_excel)
        write_data.get_sheet(0).write(row, 9, value)
        write_data.save(self.excel_path)
        time.sleep(1)
        # return write_data


if __name__ == '__main__':
    excel_util = ExcelUtil(r"D:\Pycharm\pythonProject\rtxProject\config\loginkeyword.xls")
    data = excel_util.get_cell_data(4, 6)
    print(data)




