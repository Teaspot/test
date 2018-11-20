class My_Booth_alg:
    '''
    参数、方法
    双符号位
    '''
    # 数据处理方式
    STATE_COMPLEMENT_CODE = 0
    STATE_CHANGE_COMPLEMENT = 1
    # 两个位的判断
    Cn = None
    Cn_1 = None

    def __init__(self, num1, num2):
        # 初始化三个寄存器，以及输入两个数以进行以后的运算
        self.num1 = num1
        self.num2 = num2
        # AB 考虑符号位，且符号为保持不动
        self.A = ['0', '0', '.', '0', '0', '0', '0', '0']
        self.B = ['0', '0', '.', '0', '0', '0', '0', '0']
        self._B = ['0', '0', '.', '0', '0', '0', '0', '0'] # _B -B补
        # C 不考虑符号位 且 小数点可以移动
        self.C = ['0', '.', '0', '0', '0', '0', '0', '0']

    def calculation(self):
        '''
        整个代码的计算，总框架
        :return: None
        '''
        self.B = self._B = self.dec2bin(self.num1)
        # print("B: ", self.B)
        temp = self.B
        self.C = self.dec2bin(self.num2)
        self.B = self.change_Complement(temp, self.STATE_COMPLEMENT_CODE)
        self._B = self.change_Complement(self.B, self.STATE_CHANGE_COMPLEMENT)
        self.C = self.change_Complement(self.C, self.STATE_CHANGE_COMPLEMENT)
        # 单独处理 C
        self.C.pop(0)
        self.C.insert(len(self.C), '0')

        # TODO 上一次做到这里

        return None

    def change_Complement(self, number, state):
        '''
        将输入进来的数据变为规定的数据类型，补码或者变补
        :param state: 输入进来的数据的操作类型：
        :param number:
        :return:
        '''
        # 新的数据存放点
        new_list = []
        # 操作时变补还是补码
        if state == self.STATE_COMPLEMENT_CODE:
            # 补码操作 取出符号位，再变补
            temp = number.pop(0)
            number.pop(0)
            new_list = self.change_C(number)
            new_list.insert(0, temp)
            new_list.insert(0, temp)

        elif state == self.STATE_CHANGE_COMPLEMENT:
            # 变补操作，连着符号为一起求补
            new_list = self.change_C(number)

        print("*" * 20)
        print("转换后：")
        print(new_list)
        return new_list

    def change_C(self, code):
        new_list = []
        flag = False
        length = len(code) - 1
        # 遇到 第一个 1 之前，直接添加进 new_list 中
        while length >= 0 and flag == False:
            if code[length] == '1':
                new_list.append(code[length])
                flag = True
                print("Flag Changed")
            else:
                new_list.append(code[length])
            length -= 1
        # 找到之后，反码
        while length >= 0:
            if code[length] == '1':
                new_list.append('0')
            elif code[length] == '0':
                new_list.append('1')
            elif code[length] == '.':
                new_list.append('.')
            length -= 1

        new_list.reverse()
        return new_list

    def change_Bin(self, number):
        '''
        进行二进制转换，但是输出的是 list 格式的，位数位 8 位的数据
        :param number: 输入的数据
        :return: 八位 list 格式的数据
        '''
        # TODO: 将输入的数据进行二进制变化

        print("*" * 20)
        print(number, ": ")

        # 转换成二进制和 list 格式
        number = bin(number)
        number = list(number)
        # 删除 python 的一些冗余项并添加符号项
        if '-' in number:
            number.pop(number.index('-'))
            number.insert(0, '1')
        if 'b' in number:
            number.pop(number.index('b'))
            number.insert(0, '0')
        number.pop(0)

        # 如果长度小于 8 则添加到 8 位
        if len(number) < 8:
            # 接受添加好的数据
            number = self.append_To_8(number)
        elif len(number) > 8:
            exit("长度超标")

        return number

    def dec2bin(self, number):
        '''
        将收到的小数转变为二进制小数
        :param number: 输入的小数
        :return: 转换成二进制的 list 格式的小数
        '''
        # 初始化小数
        new_list = ['.']
        print("*" * 20)
        print(number, ": ")
        # 判断小数是正数还是负数
        if number < 0:
            # 是负数去掉符号加上符号位，取绝对值
            new_list.insert(0, '1')
            new_list.insert(0, '1')
            number = abs(number)
        elif number > 0:
            new_list.insert(0, '0')
            new_list.insert(0, '0')

        count = 0
        number -= int(number)
        # 每次乘以二来转换二进制
        while number:
            number *= 2
            new_list.append('1' if number >= 1 else '0')
            number -= int(number)
            count += 1
            if count >= 5:
                break

        if len(new_list) > 8:
            i = 0
            length = len(new_list)
            while i <  length - 8:
                new_list.pop()

        new_list = self.append_2_8(new_list)
        print(new_list)
        return new_list

    def append_2_8(self, number):
        '''
        将未打到八位的二进制小数填充到八位
        :param number: 输入的小数
        :return: 八位的 list 格式的小数
        '''
        for i in range(8 - len(number)):
            # 小数的二进制在末尾添加 0 不会使得值产生变化
            number.append('0')
        print("*" * 20)
        # print("Appended: ")
        # print(number)
        return number


    def append_To_8(self, number):
        '''
        二进制变化后的数据不一定是八位，所以需要填充到八位
        :param number: 输入的数据
        :return:  八位填充后的数据
        '''
        # TODO 填充到八位数据
        for i in range(8 - len(number)):
            number.insert(1, '0')
        print("Appended: ")
        print(number)
        return number

    def add_(self, num1, num2):
        '''
        进行两个数的相加 格式：list  此处相加可以不考虑小数点
        :param num1: 第一个数据
        :param num2: 第二个数据
        :return: 加好的两个数据
        '''
        return None

    def push_(self):
        '''
        将数据向右移动一位，首位加入和前一位相同的数，是 1 加 1
        此处 push 的时候 A 中小数点不随推进而变化位置，而 C 是会随着位数变化的
        :return:
        '''
        return None

mb = My_Booth_alg(-0.8125, -0.25)
mb.calculation()
# mb.dec2bin(-0.8125)