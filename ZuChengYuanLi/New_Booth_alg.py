class Booth_Alg:
    # 定义最大位数
    Max_set = 8
    # 定义三个寄存器，共八位
    A = [0, 0, 0, 0, 0, 0, 0, 0]
    B = [0, 0, 0, 0, 0, 0, 0, 0]
    C = [0, 0, 0, 0, 0, 0, 0, 0]



    def __init__(self, x, y):
        # 得到两个的 list 格式的数据
        # 此处或得到的 list 已经是补码
        self.X = x
        self.Y = y
        self.X_C = self.change_Complement(self.X) # 将 x 化为变补
        # 将各个寄存器装入数据
        self.A = ['0', '0', '.', '0', '0', '0', '0']
        self.B = self.X
        self.C = self.Y + ['0']
        print("ABC三个寄存器此时的状态")
        print(self.A)
        print(self.B)
        print(self.C)

        # 操作类型
        self.RIGHT_00 = '00'
        self.ADD_RIGHT_01 = '01'
        self.SUB_RIGHT_10 = '10'
        self.RIGHT_11 = '11'




    def change_Complement(self, code):
        lenth = len(code) - 1
        new_list = []
        flag = False
        # 寻找到第一个 1
        while lenth >= 0 and flag == False:
            if code[lenth] =='1':
                new_list.append(code[lenth])
                flag = True
            else:
                new_list.append(code[lenth])

            lenth -= 1

        while lenth >= 0:
            if code[lenth] == '1':
                new_list.append('0')

            elif code[lenth] == '0':
                new_list.append('1')

            elif code[lenth] == '.':
                new_list.append('.')

            lenth -= 1

        new_list.reverse()
        print("*" * 30)
        print(new_list)
        return new_list
        # # 获得 变补 的数据
        # new_list = []
        # count = len(code) - 1
        # flag = False
        # while count > 0:
        #     # 在找到第一个 1 以后，后面的位数逐个取反，遇到小数点原封不动放进去
        #     if flag == True:
        #         if code[count] == '1':
        #             new_list.append('0')
        #         elif code[count] == '0':
        #             new_list.append('1')
        #         elif code[count] == '.':
        #             new_list.append('.')
        #
        #     # 若是找到了第一个 1 则 更改 flag 表示找到了
        #     elif code[count] == '1' and flag == False:
        #         flag = True
        #         new_list.append(code[count])
        #         continue
        #     else: new_list.append(code[count])
        #
        #     count -= 1
        #
        # print("转换之前的：", "\n" ,new_list)
        #
        # new_list.reverse()
        # print("转换之后的: " , "*" * 30)
        # print(new_list)
        # print("*" * 30)
        # return new_list

    def calculation(self):
        # TODO 计算补码一位乘法
        # 有多少位就做多少步
        count = len(self.B) - 1
        last_one = len(self.C) - 1
        last_two = len(self.C) - 2
        while count >= 0:
            # TODO 计算步骤内部
            Cn = self.C[last_one]
            Cn_ = self.C[last_two]

            if Cn == '1' and Cn_ == '0':
                self.A = self.add_(self.A, self.X_C)

            elif Cn == '0' and Cn_ == '1':
                self.A =  self.add_(self.A, self.X)

            elif Cn == '1' and Cn_ == '1':
                None

            elif Cn == '0' and Cn_ == '0':
                None

            if count != 0:
                self.push_()

            count -= 1

        print("答案是：", "=" * 30)
        print(self.A," + " ,self.C)
        return 1


    # 将 list 向右推进一位
    def push_(self):
        # 获取 A 最后一位并转移到 C
        # 先去除 小数点 然后计算
        print("+_" * 30)
        print(self.A)
        dot = self.A.index('.')
        self.A.pop(dot)
        temp = self.A.pop(len(self.A) - 1)
        self.C.insert(0, temp)
        self.C.pop(len(self.C) - 1)
        self.A = [self.A[0]] + self.A
        # 此处加入小数点
        self.A.insert(1, '.')
        print("Push: ", self.A[0])

    def add_(self, code1, code2):
        # 已检测，二进制加法成功/
        # 定义运算元
        temp1 = None
        temp2 = None
        next_ = '0' # 进位，默认为 0
        new_list = []
        # 长度
        lenth = len(code1)
        # 循环加
        for i in range(lenth):
            # 获取当前的位
            temp1 = code1[lenth - i - 1]
            temp2 = code2[lenth - i - 1]
            # 判断当前的情况
            if temp1 == temp2 == next_ == '1':
                # 如果三位都为 1 ，则当前位为 1， 并进位
                next_ = '1'
                new_list.append('1')
            elif temp1 == temp2 == next_ == '0':
                # 如果三位都为 0 ， 则当前为为 0，不进位
                next_ = '0'
                new_list.append('0')
            elif temp1 == temp2 == '1' and next_ == '0':
                # 如果两位为 1，进位为 0 ， 则进位为 1，当前位为 0
                next_ = '1'
                new_list.append('0')
            elif temp1 == temp2 == '0' and next_ == '1':
                # 如果两位为 0，进位为 1， 则进位为 0，当前位为 1
                next_ = '0'
                new_list.append('1')
            elif temp1 == next_ == '1' and temp2 == '0':
                # 一位 0 一位 1，进位为 1， 则进位为 1， 当前位为 0
                next_ = '1'
                new_list.append('0')
            elif temp2 == next_ == '1' and temp1 == '0':
                # 同上
                next_ = '1'
                new_list.append('0')
            elif temp1 == next_ == '0' and temp2 == '1':
                # 同上
                next_ = '0'
                new_list.append('1')
            elif temp2 == next_ == '0' and temp1 == '1':
                # 同上
                next_ = '0'
                new_list.append('1')
            elif temp1 == temp2 == '.' and next_ == '1':
                next_ = '1'
                new_list.append('.')
            elif temp1 == temp2 == '1' and next_ == '0':
                next_ = '0'
                new_list.append('.')
            # print(next_)

        new_list.reverse()
        print("相加结果：", "*" * 30)
        print(new_list)

        return new_list




x = "11.0011"
y = "1.0101"
x = list(x)
y = list(y)
# print("原来的数据：")
# print(x, "\n" , y)
# print("*" * 30)

b = Booth_Alg(x, y)
b.calculation()
code1 = '0101'
code2 = '0011'
# code1 = list(code1)
# code2 = list(code2)
# b.add_(code1, code2)