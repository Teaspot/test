import time
import math
import random

def Get_Radom_list(count):
    '''
    TODO
    随机生成 n 个数
    :param n:
    :return:返回随机数组
    '''

    radom_list = []
    for i in range(1, count):
        radom_list.append(random.randint(1, 20))

    print("The random list is: ", end="")
    print(radom_list)

    return radom_list


def cal_liner(random_list, count):
    # TODO 计算线性
    time_all = 0

    result = float(1)

    for i in range(1, len(random_list)):
        # todo 计算时间
        time_start = time.clock()
        list_number = random_list[i]

        # 计算 n 个 2 相乘
        # for j in range(1, list_number):
        #     result *= 2
        result = (2 * result) * list_number

        time_end = time.clock()
        time_interval = time_end - time_start
        time_all += time_interval

        print("Time Liner", i, ": ", time_interval)

    time_aver = time_all / len(random_list)
    return time_aver

def Which_is_faster(time_liner, time_nonliner):
    # TODO 判断哪个时间大
    print("-" * 20)
    if(time_liner > time_nonliner):
        print("线性大于非线性， 大了：", time_liner - time_nonliner)
    else:
        print("非线性大于线性， 大了：", time_nonliner - time_liner)
    return 1

def cal_nonliner(random_list, count):
    # TODO 计算非线性
    time_all = 0

    for i in range(1, len(random_list)):
        time_start = time.clock()

        list_number = random_list[i]
        result = math.pow(2, list_number)

        time_end = time.clock()
        time_interval = time_end - time_start

        time_all += time_interval

        print("Time Nonliner interval ", i,": ", time_interval)

    time_aver = time_all / len(random_list)
    return time_aver

def main():
    # TODO 主要函数：计算2的线性运算和非线性运算
    # 指定随机的个数
    count = 10
    random_list = Get_Radom_list(count)

    time_liner = float
    time_nonliner = float

    time_liner = cal_liner(random_list, count)
    print("*" * 20)
    time_nonliner = cal_nonliner(random_list, count)

    print("*" * 20)

    print("线性运算的时间：", end="")
    print(time_liner)
    print("*" * 20)
    print("非线性运算的时间为：", end="")
    print(time_nonliner)

    Which_is_faster(time_liner, time_nonliner)

    return True

main()