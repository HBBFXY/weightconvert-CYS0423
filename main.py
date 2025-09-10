# 在这个文件下编写代码，题目具体要求见README.md文件
def weight_converter():
    input_str = input().strip().lower()
    
    if input_str.endswith('kg'):
        try:
            kg_value = float(input_str[:-2])
            pound_value = kg_value * 2.2046
            print(f"对应的英制重量为{pound_value:.3f}磅")
        except ValueError:
            print("输入格式错误，请输入数字后跟单位(如10kg或10pd)")
    
    elif input_str.endswith('pd'):
        try:
            pound_value = float(input_str[:-2])
            kg_value = pound_value / 2.2046
            print(f"对应的公制重量为{kg_value:.3f}公斤")
        except ValueError:
            print("输入格式错误，请输入数字后跟单位(如10kg或10pd)")
    
    else:
        print("输入格式错误，请以kg或pd结尾指定单位")

if __name__ == "__main__":
    weight_converter()
