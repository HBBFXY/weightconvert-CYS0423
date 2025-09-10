# 获取用户输入
weight = input()

# 判断输入的是千克还是磅
if weight.endswith('kg'):
    # 提取重量值
    kg = float(weight[:-2])
    # 进行千克到磅的转换
    pd = kg * 2.2046
    # 输出结果，保留 3 位小数
    print(f"对应的英制重量为{pd:.3f}磅")
elif weight.endswith('pd'):
    # 提取重量值
    pd = float(weight[:-2])
    # 进行磅到千克的转换
    kg = pd / 2.2046
    # 输出结果，保留 3 位小数
    print(f"对应的公制重量为{kg:.3f}公斤")
