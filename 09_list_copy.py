# 실습
# temps = [34, 33, 35, 29, 28]
# print(temps)
# print(len(temps))
# empty = []
# print(empty)
# print(len(empty))

# temps = [22, 23, 24, 25, 26, 27]
# print(temps[0])
# print(temps[3])
# print(temps[-1])

# a = [220, 230, 240, 250, 260, 270]
# b = a[0]
# c = a[-1]
# print(b + c)
# print((b + c) / 2)

# # 실습 4
# temps = [20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
# print(temps[:3])
# print(temps[-3:])
# print(len(temps[:3]))
# print(len(temps[:3]))
# # 실습 5
# a = [30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41]
# first = a[:6]
# second = a[-6:]
# print(first)
# print(second)
# print(len(first))
# print(len(second))

# temps = [25, 26, 240, 28, 27]
# print(240 in temps)
# i = temps.index(240)
# temps[i] = 24
# print(temps)
# print(240 in temps)

# a = []
# a.append(30)
# print(a)
# a.insert(0, 28)
# print(a)
# a.extend([31, 32])
# print(a)

# a = [25, 26, 24, 28, 26, 999]
# a.remove(999)
# print(a)
# b = a.pop(1)
# print(b)
# del a[0]
# print(a)

temps = [24, 22, 28, 27, 30, 24, 26]
temps.sort()
print(temps)
temps.sort(reverse=True)
print(temps)
print(temps.count(24))
print(temps.index(24))
