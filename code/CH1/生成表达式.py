from random import randint

print(tuple(randint(1, 99) for i in range(10)))

a = tuple(randint(1, 99) for i in range(20))
y = tuple(sorted(a[0:10]) + sorted(a[10:20], reverse=True))
print(y)

