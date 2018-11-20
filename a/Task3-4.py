# 任务 3-5
set1 = ['apple', 'pear', 'watermelon', 'peach']
set2 = list(('pear', 'banana', 'orange', 'peach', 'grape'))

set1 = set(set1)
set2 = set(set2)

print(type(set1), "\n", type(set2))

set3 = set1 & set2 # 交集
set4 = set1 | set2 # 并集
set5 = set1 - set2 # 差集
set6 = set1.difference(set2)



