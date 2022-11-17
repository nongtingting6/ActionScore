from person import Person
import datetime
from openpyxl import load_workbook
import re

liu = Person('liusx')
ntt = Person('nongtt')
obj_dict = {'liu': liu, 'ntt': ntt}

while True:
    _input = input('输入名字和动作id，例如：ntt 1.或者Q退出,或者S保存:\n')  # ntt 1
    # 判断输入
    # 输入是S，则保存
    if _input.upper() == 'S':
        # 保存所有对象的信息,待实现
        liu.write_record_to_excel()
        ntt.write_record_to_excel()
    elif _input.upper() == 'Q':
        # 先保存
        liu.write_record_to_excel()
        ntt.write_record_to_excel()
        sure = input('已保存,请确认是否退出,输入yes退出:\n')
        if sure.upper() == 'YES':
            exit('退出程序')
    elif re.findall('\D+? \d', _input):  # 用正则表达式判断输入是不是符合预期
        # 分解输入信息ntt 1
        name, action_id = _input.split(' ')
        obj = obj_dict.get(name)
        obj.person_do_action(action_id)
    else:
        pass

    print()