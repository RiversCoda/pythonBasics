money = int(input("请输入待找零的金额"))

coins = (25, 10, 5, 1)
counts = []

for i in coins:
    counts.append(money // i)
    money %= i

for i in range(len(counts)):
    print("找零{0}美分硬币{1}个".format(coins[i], counts[i]))