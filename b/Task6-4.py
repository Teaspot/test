class Car:
    def __init__(self, brand, newWheelNum, newColor, T):
        self.brand = brand
        self.wheelNum = newWheelNum
        self.color = newColor
        self.T = T
        self.info = [self.brand, self.wheelNum, self.color, self.T]
        self.index = -1

    def getBrand(self):
        return self.brand
    def getWheelNum(self):
        return self.wheelNum
    def getColor(self):
        return self.color
    def getT(self):
        return self.T
    def __iter__(self):
        print('品牌 车轮数 颜色 废气涡轮增压')
        return self
    def next(self):
        if self.index == 3:
            raise StopIteration
        self.index += 1
        return self.info[self.index]

class Land_Rover(Car):
    def __init__(self, brand, newColor):
        self.brand = brand
        self.wheelNum = 4
        self.color = newColor 
        self.T = 3
        Car.__init__(self, self.brand, self.wheelNum, self.color, self.T)

Luxury_car = Car('BMW', 4, 'green', 2.4)
print(Luxury_car.getColor())
iterator = iter(Luxury_car.next, 1)
for i in iterator:
    print(i)
