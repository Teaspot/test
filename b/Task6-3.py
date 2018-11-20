# 创建 车 的实例
class Car:

    def __init__(self, new_Car_Name, new_Wheel_Num, new_Color, T, brand):
        print("----构造函数被调用----")
        self.car_Name = new_Car_Name
        self.wheel_Num = new_Wheel_Num
        self.color = new_Color
        self.T = T
        self.brand = brand
        self.Info = [self.car_Name, self.wheel_Num, self.color, self.T, self.brand]
        self.index = -1

    def show_Info(self):
        print("Name: ", self.car_Name)
        print("Wheel Number: ", self.wheel_Num)
        print("Color: ", self.color)

    def run(self):
        print("车在跑，目标：夏威夷")

    def __del__(self):
        print("----析构方法被调用----")

    def getBrand(self):
        return self.brand
    def getName(self):
        return self.car_Name
    def getWheelNum(self):
        return self.wheel_Num
    def getColor(self):
        return self.color
    def getT(self):
        return self.T

    def next(self):
        if self.index == 3:
            raise StopIteration
        self.index += 1
        return self.Info[self.index]



# BMW = Car("BMW", 4, "red")
# BMW.show_Info()
# BMW.run()
newcar = Car("BMW", 4, "red", 2.4, "BBMMWW")
print(newcar.getColor())
iterator = iter(newcar.next, 1)
for info in iterator:
    print(info)
