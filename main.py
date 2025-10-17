input_str = input("请输入一行字符：")

letter = 0
digit = 0
space = 0
other = 0

for char in input_str:
    if char.isalpha():  # 判断是否为英文字母（a-z, A-Z）
        letter += 1
    elif char.isdigit():  # 判断是否为数字（0-9）
        digit += 1
    elif char.isspace():  # 判断是否为空格（包括空格、制表符等空白）
        space += 1
    else:  # 不属于以上三类的就是其他字符
        other += 1

print("英文字符:", letter)
print("数字:", digit)
print("空格:", space)
print("其他字符:", other)
