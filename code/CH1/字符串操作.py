import re

# 定义一个字符串
text = "Python is an amazing language. Python is easy to learn."

# 编译一个正则表达式模式，用于匹配“Python”
pattern = re.compile(r"Python")

# 使用findall方法查找所有匹配项
matches = pattern.findall(text)

# 打印匹配项
for match in matches:
    print(match)

# 字符串的索引访问
str1 = "Hello, World!"
print("First character:", str1[0])
print("Last character:", str1[-1])

# 字符串的切片操作
print("First five characters:", str1[:5])
print("Last five characters:", str1[-5:])

# 字符串的长度
print("Length of the string:", len(str1))

# 字符串的遍历
for char in str1:
    print(char, end=" ")
print()

# 字符串的删除操作（注意：字符串是不可变类型，不能直接删除字符，可以通过切片或替换实现）
str2 = str1[:5] + str1[6:]
print("String after removing the comma:", str2)

# 字符串的分割
words = str1.split(", ")
print("Split string:", words)

# 清除字符串两端的空白
str3 = "   Hello, World!   "
print("String with stripped whitespace:", str3.strip())

# 字符串的大小写转换
print("Lowercase:", str1.lower())
print("Uppercase:", str1.upper())

# 判断字符串的开头和结尾
print("Starts with 'Hello':", str1.startswith("Hello"))
print("Ends with 'World!':", str1.endswith("World!"))

# 字符串的替换
print("Replace 'World' with 'Python':", str1.replace("World", "Python"))
print("test is:",str1)

# 字符串的格式化
name = "Alice"
age = 30
print(f"Name: {name}, Age: {age}")

# 字符串的编码和解码
encoded_str = str1.encode("utf-8")
print("Encoded string:", encoded_str)
decoded_str = encoded_str.decode("utf-8")
print("Decoded string:", decoded_str)