f = open("code\CH4\\test.txt", "rt")
data = f.readlines()
f.close()

dic = dict()
for i in range(26):
    dic[chr(ord("A") + i)] = 0

for line in data:
    line = line.upper()
    for c in line:
        if "A" <= c <= "Z":
                dic[c] += 1

i = 0
for key in sorted(dic.keys()):
    print(key, dic[key])

