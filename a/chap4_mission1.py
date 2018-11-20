# 猜数字游戏
import random

def random_count():
    print("随机生成一个 1 到 20 的随机数, 猜出正确答案即可进入下一轮")
    print("*" * 30)
    while(100):
        origin_number = random.randint(1, 20)
        print(origin_number) # 作弊
        count_number = int(input("请输入猜中的数字："))
        # 没猜对之前无法进入下一轮
        while count_number != origin_number:
            if count_number < origin_number:
                print("_" * 30)
                count_number = int(input("小了，请重新输入："))
                continue
            elif count_number > origin_number:
                print("_" * 30)
                count_number = int(input("大了，请重新输入："))
                continue

        print("猜对了, 开始下一轮")
        print("*" * 20)


random_count()

