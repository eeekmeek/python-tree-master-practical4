# Summing series

def sum_series2(i):
    if i == 1:
        return 1/3
    else:
        return i/(2*i+1) + sum_series2(i-1)

n = int(input("Enter number: "))
print("{0:.2f}".format(sum_series2(n)))
