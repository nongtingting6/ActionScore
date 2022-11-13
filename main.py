from person import Person
from data import Data
import datetime
from openpyxl import load_workbook

ntt = Person(0)
liu = Person(0)
obj_dict = {'liu': liu, 'ntt': ntt}


while True:
    _input = input('输入名字和动作id，例如：ntt 1')  # ntt 1
    name = _input.split(' ')[0]
    action_id = _input.split(' ')[1]
    # 选择b本次需要操作的对象
    obj = obj_dict.get(name)


    # 判断输入
    # 输入是S，则保存
    if action_id=='S':
        date = load_workbook("data.xlsx")  # 加载
        sheet = date["记录事件"]  # 选择编辑的工作簿
        for record in obj.action_and_time:
            sheet["A1"]=name+record[0]+record[1]
        date.save('data.xlsx')



    elif action_id=='Q':
        exit('退出程序')

    # 输入是Q，则推出
    # 输入是其他，则运行动作
    else:
        name = _input.split(' ')[0]
        action_id = _input.split(' ')[1]
        # 选择b本次需要操作的对象
        obj = obj_dict.get(name)
        if obj is not None:
            obj.action(action_id)

    print(f"当前操作的对象{name}的分数为：{obj.score}")
    print(f"当前操作的对象{name}的记录为：{obj.action_and_time}")
