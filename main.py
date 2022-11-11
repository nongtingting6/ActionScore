from person import Person
import datetime

ntt=Person(0)
liu=Person(0)
while True:
    name = input('请输入你的名字')
    action_id = input("请输入动作id")
    if name=="liu":
        liu.action(action_id)
    elif name=="ntt":
        ntt.action(action_id)


    print(f"刘双喜的分数为：{liu.score}")
    print(f"农婷婷的分数为：{ntt.score}")
    print(f'当前农婷婷做：{ntt.action_and_time}')



