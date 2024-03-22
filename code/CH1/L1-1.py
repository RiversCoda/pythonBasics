import random

# 随机生成一个数字作为只出现一次的数字
randomNum = random.randint(1, 30000)

# 利用循环生成剩下的数字，跳过只出现一次的数字
arr = []
for i in range(1, 30001):
    if i != randomNum:
        arr.append(i)
        arr.append(i)

# 将只出现一次的数字添加到数组中
arr.append(randomNum)

# 将数组打乱
random.shuffle(arr)

# 利用异或找出只出现一次的数字
result = 0
for i in arr:
    result ^= i

print(result)
