from openpyxl import load_workbook


class Data:
    def __init__(self,excel_name):
        self.excel_name = excel_name

    def get_data(self):
        date = load_workbook(self.excel_name)  # 加载
        sheet = date["Sheet1"]  # 选择编辑的工作簿
        action_to_info = {}
        for row in sheet:  # 按行循环
            row_value = []  # 将行的数据添加到列表里
            for cell in row:  # 再按一行里的每一列去循环
                row_value = row_value + [cell.value]
            action_to_info_temp = {str(row_value[0]): row_value[1:]}
            action_to_info.update(action_to_info_temp)
        return action_to_info


if __name__ == '__main__':
    a = Data("data.xlsx")
    action_to_info = a.get_data()
    print()
