# Summing the digits in an integer using recursion

def sum_digits(n):
    if len(n) == 1:
        return int(n)
    else:
        return sum_digits(n[1:]) + int(n[0])

num = int(input("Enter an integer: "))
print(sum_digits(num))
