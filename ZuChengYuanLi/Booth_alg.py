class Booth_alg:
    # 定义最大位数
    Max_set = 8
    # 定义三个寄存器，共八位
    A = [0, 0, 0, 0, 0, 0, 0, 0]
    B = [0, 0, 0, 0, 0, 0, 0, 0]
    C = [0, 0, 0, 0, 0, 0, 0, 0]

    def __init__(self, x, y):
        '''
        带有 L_ 的表示list 格式
        带有 _N 的表示其补码
        带有 _N_C 的表示变补
        初始化输入两个数字，并且将其转化为二进制的数字
        这些二进制数字最后会用 list 来表示
        '''
        # self.X = bin(x)
        # self.Y = bin(y)
        # self.X_N = bin(~x)
        # self.Y_N = bin(~y)

        self.X_N = x
        self.Y_N = y

        print("二进制：", "*" * 30)
        # print(self.X)
        # print(self.Y)
        print(self.X_N)
        print(self.Y_N)
        print("*" * 30)

    def to_List(self):
        # 将之转化成 list 形式
        self.L_X_N = list(self.X_N)
        self.L_Y_N = list(self.Y_N)
        # 去除前三位 python 的符号
        # self.L_X_N = self.pop_Top(self.L_X_N)
        # self.L_Y_N = self.pop_Top(self.L_Y_N)

        print("list 格式：", "*" * 30)
        print(self.L_X_N)
        print(self.L_Y_N)
        print("*" * 30)
        # 添加位数
        # self.L_X_N = self.append_To_Max(self.L_X_N)
        # self.L_Y_N = self.append_To_Max(self.L_Y_N)


    # 废弃
    def pop_Top(self, code):
        # 返回去除前三位的-、0、b
        if '-' in code:
            code.pop(code.index('-'))
        code.pop(code.index('b'))
        code.pop(0)
        # code.pop(2)
        return code

    # 废弃
    def append_To_Max(self, code):
        # 将原来的 list 添加到最大的位数
        # 由于原来的第一位为符号为，所以从第二位开始添加
        lenth = len(code) # 获取长度
        if lenth > self.Max_set:
            print("你的长度超过限制，数值溢出")
            exec()
        else:
            gap = self.Max_set - lenth
            # 将其添加到设定的位数
            for i in range(gap + 1):
                code.insert(1, '0')
            print("补满位数后的：", "*" * 20)
            print(code)

    def change_complement(self, code):
        # TODO： 将收到的 code 变补
        # 将 code 中的每一项取出来并取反，然后加一
        for i in code:
            if i == '1':
                i = '0'
            elif i == '0':
                i = '1'
        return 0

    def calculation(self):
        # TODO： 计算
        return 0


x = "11.0011"
y = "10.1011"
x = list(x)
y = list(y)
b = Booth_alg(x, y)
b.to_List()