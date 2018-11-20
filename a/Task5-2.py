def normal_Add():
    '''
    正常的累加函数
    :return: 数据累加得和
    '''
    def add(x):
        x += 3
        return x;

    data_add = range(1, 10, 2) # 累加得数据
    result_list = []

    for i in data_add:
        result_list.append(add(i))

    print("常规累加：",result_list)

    return None

def lambda_Add():
    '''
    使用 lambda 函数累加
    :return:
    '''
    data_add = range(1, 10, 2)
    result_list = []

    # 定义 lambda 函数
    new_function = lambda x : x + 3

    for i in data_add:
        result_list.append(new_function(i))

    print("使用 lambda 累加：", result_list)


normal_Add()

lambda_Add()