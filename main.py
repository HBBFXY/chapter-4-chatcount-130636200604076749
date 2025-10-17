input_str = input("请输入一行字符：")

letter = 0
digit = 0
space = 0
other = 0

for char in input_str:
    if char.isalpha():  
        letter += 1
    elif char.isdigit():  
        digit += 1
    elif char.isspace(): 
        space += 1
    else:  
        other += 1

print("英文字符:", letter)
print("数字:", digit)
print("空格:", space)
print("其他字符:", other)
