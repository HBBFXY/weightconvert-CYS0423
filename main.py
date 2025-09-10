# 重量转换程序：千克(kg)与磅(pd)之间的转换
# 转换比例：1千克 = 2.2046磅

# 获取用户输入
input_str = input().strip()

# 提取数值和单位
try:
    # 查找单位起始位置
    if 'kg' in input_str:
        unit = 'kg'
        value = float(input_str.replace('kg', ''))
    elif 'pd' in input_str:
        unit = 'pd'
        value = float(input_str.replace('pd', ''))
    else:
        raise ValueError("单位不正确，请使用kg或pd")
    
    # 进行转换计算
    if unit == 'kg':
        # 千克转磅
        result = value * 2.2046
        print(f"对应的英制重量为{result:.3f}磅")
    else:
        # 磅转千克
        result = value / 2.2046
        print(f"对应的公制重量为{result:.3f}公斤")
        
except ValueError as e:
    print(f"输入错误: {e}")
    
