a = {'1': 4, '2': 5}

ntt = 0
liu = 0
while True:
    name = input('请输入你的名字')
    type = input("请输入类别")
    score = a.get(type)
    if name == 'liu':
        liu += score
        print(f"刘双喜分数:{liu}")
    elif name == 'ntt':
        ntt += score
        print("农婷婷分数:", ntt)
