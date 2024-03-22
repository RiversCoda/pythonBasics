#十进制整数转二进制
def dec2bin(n):
    if n < 0:
        return '输入的数字必须是正整数'
    else:
        return bin(n)[2:]
#测试
print(dec2bin(65511))

# def decimal_to_binary(decimal):
#     # 整数部分的二进制表示
#     integer_part = int(decimal)
#     binary_integer_part = bin(integer_part).replace("0b", "")

#     # 小数部分的二进制表示
#     decimal_part = decimal - integer_part
#     binary_decimal_part = "."
#     while decimal_part > 0:
#         decimal_part *= 2
#         if decimal_part >= 1:
#             binary_decimal_part += "1"
#             decimal_part -= 1
#         else:
#             binary_decimal_part += "0"

#     # 合并整数部分和小数部分的二进制表示
#     binary_number = binary_integer_part + binary_decimal_part
#     return binary_number


def floatToBin(num):
	# part1
	num1 = int(num)
	num1Bin = bin(num1).replace("0b","")
	# num1Bin = bin(num1)[2:]
	
	# part2
	num2 = num - num1
	num2Bin = "."
	while num2 > 0:
		num2 *= 2
		if num2 >= 1:
			num2Bin += "1"
			num2 -=1
		else:
			num2Bin +="0"
	outputNum = num1Bin + num2Bin
	return outputNum

# 测试代码
decimal_number = 10.625
# binary_number = decimal_to_binary(decimal_number)
binary_number = floatToBin(decimal_number)
print(f"十进制小数 {decimal_number} 转换为二进制小数为 {binary_number}") # 此处f的作用是将{}中的内容替换为变量的值

