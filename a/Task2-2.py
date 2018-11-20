import math
PI = 3.1415

class Cal_Shape:
    PII = 3.1415
    def __init__(self):
        all = 0
    def cal_C_S(self):
        R = int(input("请输入半径:"))

        C = 2 * PI * R
        print("周长为：", C)
        S = PI * R * R
        print("面积为：", S)

    def cal_S_R(self):
        C = int(input("请输入周长："))

        R = C / 2 / PI
        print("半径为: ", R)
        S = R * R * PI
        print("面积为: ", S)

    def cal_C_R(self):
        S = int(input("请输入面积: "))

        tmp = S / PI
        R = math.sqrt(tmp)
        print("半径为: ", R)
        C = 2 * PI * R
        print("周长为：", C)


C = Cal_Shape()

C.cal_C_R()
C.cal_C_S()
C.cal_S_R()

