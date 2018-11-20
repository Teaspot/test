def dec2bin(x):
    x-= int(x)
    bins = ['0', '.']
    while x:
        x *= 2
        bins.append(1 if x >= 1. else 0)
        x -= int(x)
    return bins

print(dec2bin(0.8125))
