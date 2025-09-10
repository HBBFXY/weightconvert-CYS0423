weight_input = input()
value = float(weight_input[:-2])
unit = weight_input[-2:]

if unit == 'kg':
    result = value * 2.2046
    print(f"对应的英制重量为{result:.3f}磅")
elif unit == 'pd':
    result = value / 2.2046
    print(f"对应的公制重量为{result:.3f}公斤")
else:
    print("输入格式不正确，请输入如'10kg'或'10pd'的格式。")
