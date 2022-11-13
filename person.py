import datetime
from openpyxl import load_workbook
from data import Data

class Person():

    def __init__(self, score):
        self.score = score
        self.action_and_time = []

    def action(self, action_id):
        # 从excel获取所有动作的信息
        date = Data("data.xlsx")
        action_to_info = date.get_data()

        # 获取当前动作的信息，是列表[动作，范围，频率，分数]
        action_info_cur = action_to_info.get(action_id)

        # 如果当前动作id在excel的所有动作信息里的话
        if action_info_cur is not None:
            cur_score = action_info_cur[3]
            cur_action_info = action_info_cur[0]
        else:
            cur_score = 0
            cur_action_info = '输入错误'

        # 获取当前时间的datetime对象
        cur_day = datetime.datetime.now()
        # datatime格式化输出
        cur_time = cur_day.strftime('%Y年%m月%d日%H点%M分%S秒')

        # 累加保存当前对象的分数和动作记录
        self.score = self.score + cur_score
        self.action_and_time = self.action_and_time + [[cur_action_info, cur_time]]

