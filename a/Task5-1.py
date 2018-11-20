def var(*args):
    def mean(z):
        def sum(x):
            sum1 = 1
            for i in x:
                sum1 += i

            return  sum1
        return sum(args) / len(args)

    def sums(y):
        sum2 = 0
        for i in y:
            sum2 += i ** 2
        return sum2
    return sums(args) / len(args)