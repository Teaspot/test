user_name = input("请输入您的姓名：")
print("编号   |   星座  |   日期          ")
string1 = ("1      |   水瓶  |   1月20——2月18")
string2 = ("2      |   双鱼  |   2月19——3月20")
string3 = ("3      |   白羊  |   3月21——4月19")
string4 = ("4      |   金牛  |   4月20——5月20")
string5 = ("5      |   双子  |   5月21——6月21")
string6 = ("6      |   巨蟹  |   6月21——7月22")
string7 = ("7      |   狮子  |   7月23——8月22")
string8 = ("8      |   处女  |   8月23——9月22")
print(string1)
print(string2)
print(string3)
print(string4)
print(string5)
print(string6)
print(string7)
print(string8)
print("")
number = int(input("请根据如上提示选择对应的编号: "))

print(user_name + ", 你好！\n 您的星座分析如下：")

if(number == 1):
    print(string1)
elif(number == 2):
    print(string2)
elif(number == 3):
    print(string3)
elif(number == 4):
    print(string4)
elif(number == 5):
    print(string5)
elif(number == 6):
    print(string6)
elif(number == 7):
    print(string7)
elif(number == 8):
    print(string8)
