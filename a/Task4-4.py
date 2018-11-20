num = eval(input("输入一个整数: "))
print("金字塔显示如下:")
level = 1

while level < num:
    kk = 1
    t = level
    lenth = 2*t - 1
    while kk <= lenth:
        if kk == 1:
            if kk == lenth:
                print(format(t, str(2 * num - 1) + "d"), "\n")
                break
            else:
                print(format(t, str(2 * num + 1 - 2 * level) + "d"), "", end="")
                t -= 1
        else:
            if kk == lenth:
                print(t, "\n")
                break

            elif kk <= lenth/2:
                print(t, "", end="")
                t -= 1

            else:
                print(t, "", end="")
                t += 1

        kk +=1
    level += 1


