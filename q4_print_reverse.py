# Reverse the digits in an integer recursively

def reverse_int(n):
    if len(n)==1:
        return n
    else:
        return n[-1]+reverse_int(n[:-1])

number = input("Enter an integer: ")
print(reverse_int(number))


