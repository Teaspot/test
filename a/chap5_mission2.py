# 第 5 章得实训 2
import random

gen_list = []
for i in range(1, 10):
    gen_list.append(random.randint(1, 20))
# 定义 lambda 函数
new_sqare = lambda x : pow(x, 2)

result_list = []
for i in gen_list:
    result_list.append(new_sqare(i))
print("生成的列表", gen_list)
print("平方得列表", result_list)