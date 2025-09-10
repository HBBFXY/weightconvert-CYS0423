# 在这个文件下编写代码，题目具体要求见README.md文件
input_str = input().strip()
value = float(input_str[:-2])
unit = input_str[-2:]

if unit == 'kg':
    result = value * 2.2046
    print(f"对应的英制重量为{result:.3f}磅")
elif unit == 'pd':
    result = value / 2.2046
    print(f"对应的公制重量为{result:.3f}公斤")
else:
    print("输入格式错误，请使用'kg'或'pd'作为单位")
