weight_input = input()
num = float(weight_input[:-2])
unit = weight_input[-2:].lower()
if unit == "kg":
    result = num * 2.2046
    print("对应的英制重量为{:.3f}磅".format(result))
elif unit == "pd":
    result = num / 2.2046
    print("对应的公制重量为{:.3f}公斤".format(result))
