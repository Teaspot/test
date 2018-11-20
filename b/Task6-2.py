# 定义 car 类

class Car:
    wheel_number = 0
    color = "default"

    def set_Info(self, wheelNum, color):
        self.wheel_number = wheelNum
        self.color = color

    def get_Name_Info(self, name):
        # 获取汽车的相关参数
        self.name = name
        print(self.name, "有 %d 个车轮， 颜色是 %s" %(self.wheel_number, self.color))

    def run(self, name):
        self.name = name
        print("有 %d 个车轮的%s 的 %s 正行驶在路上" % (self.wheel_number, self.color, self.name))

car1 = Car()
car1.set_Info(4, "red")
car_Name = "Cal"
car1.get_Name_Info(car_Name)
car1.run(car_Name)
