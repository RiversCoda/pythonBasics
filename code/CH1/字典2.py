numbers = {}
numbers[(1,2,3)] = 1
numbers[(2, 1)] = 2
numbers[(1, 2)] = 3
sum = 0
for k in numbers:
    sum += numbers[k]
print(len(numbers) + sum)