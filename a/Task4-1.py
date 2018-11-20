'''
* 打印成绩的结果
* 创建 score 变量来存放数据
* 设置 if 语句来添加分支
* 打印结果
'''

score = int(input("请输入分数: "))
if (score >= 90):
    print("本次考试成绩为 A")
elif(score >= 80 and score <90):
    print("本次考试成绩为 B")
elif score >= 70 and score < 80:
    print("本次考试成绩为 C")
elif score >= 60 and score < 70:
    print("本次考试成绩为 D")
else:
    print("本次考试成绩为 E")