# Summing series

def sum_series1(i):
    if i == 1:
        return 1
    else:
        return 1/i + sum_series1(i-1)

n = int(input("Enter number: "))
print("{0:.2f}".format(sum_series1(n)))
