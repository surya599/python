a = [45,32,98,76,14,26]

b = len(a)
temp = a[0]
a[0] = a[b-1]
a[b-1] = temp

print(a)
