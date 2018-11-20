def LRU_alg(list_order, maxNum):
    '''
    模仿 LRU 算法
    :param list_order: 输入的列表
    :param maxNum: 最大长度 3
    :return: 列表
    '''
    temp = 0;
    list_stack = []
    count = 0 # 最大长度为 3, 初始长度为 0
    loss = 0 # 缺页次数

    for i in list_order:
        if i in list_stack:
            # 如果在列表中则弹出该元素并且放到列表顶端，此时不缺页
            temp = list_stack.pop(list_stack.index(i))
            list_stack.append(temp)

        else:
            if count < maxNum:
                # 如果列表未满则直接放入
                list_stack.append(i)
                count += 1 # 此时列表未满，增加
                loss += 1
            elif count >= maxNum:
                # 否则弹出最低端的元素并加入新的元素， 并记录缺页次数
                list_stack.pop(0) # 弹出低端元素
                list_stack.append(i)
                loss += 1 # 记录缺页次数
        print("queue: ", list_stack)

    return loss

new_list = [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5]
print(new_list, "的缺页次数：", LRU_alg(new_list, 3))