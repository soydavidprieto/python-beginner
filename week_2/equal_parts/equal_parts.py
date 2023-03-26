import math
i = input("Enter sequence: ")
a = list(i.split())
b = math.floor(len(a)//2)
first = a[:b]
second = a[b:]
print(first)
print(second)
