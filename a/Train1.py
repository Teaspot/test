list_all = [] # 定义总的数列表
list_all.append(0)
list_all.append(1)

count = 8

for i in range(2, count):
    new_number = sum([list_all[i - 2], list_all[i - 1]])
    list_all.append(new_number)

list_all.pop(2) # 弹出第三项

print(list_all)
list11 = list_all.sort(reverse=True)
print(list11)