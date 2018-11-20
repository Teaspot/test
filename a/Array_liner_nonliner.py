import numpy
import time
import random
# 定义 3 X 3 的全部值为 2 矩阵
origin_array = numpy.ones([3, 3])
two_array = origin_array * 2

def Cal_Nonliner(random_list):
    time_all = 0
    time_aver = 0

    for i in range(1, len(random_list)):
        list_number = random_list[i]
        new_array = origin_array * list_number
        time_start = time.clock()
        result_array = numpy.exp(two_array, new_array)
        time_end = time.clock()

        time_interval = time_end - time_start
        print("NONLINER time", i, ": ", time_interval)
        time_all += time_interval
        time_aver = time_all / len(random_list)

    return time_aver

def Cal_Liner(random_list):
    time_all = 0
    time_aver = 0

    for i in range(len(random_list)):
        list_number = random_list[i]
        new_array = origin_array * list_number
        time_start = time.clock()
        result_array = numpy.multiply(two_array, new_array)
        time_end = time.clock()

        time_interval = time_end - time_start
        print("LINER Time", i, ":",time_interval)
        time_all += time_interval
        time_aver = time_all / len(random_list)

    return time_aver

def Gen_Random_List():
    random_list = []
    # todo Generate list used to calculate
    for i in range(1, 10):
        random_list.append(random.randint(1, 20))
    return random_list

def Which_is_faster(liner, nonliner):
    if(liner > nonliner):
        print("线性更快，快了:", liner - nonliner)
    else:
        print("非线性更快，快了:", nonliner - liner)

    return 1


random_list = Gen_Random_List()

time_liner = Cal_Liner(random_list)
print("*" * 30)
time_nonliner = Cal_Nonliner(random_list)
print("*" * 30)


print("Liner average:", time_liner)
print("-" * 30)
print("Nonliner averafe:", time_nonliner)
print("=" * 30)
Which_is_faster(time_liner, time_nonliner)





