# Finding the largest number in an array

def find_largest(alist):
    if len(alist) == 0:
        return 0
    if len(alist) == 1:
        return alist[0]
    else:
        a = find_largest(alist[1: ])
        if alist[0] < a:
            return a
        else:
            return alist[0]

A = [4, 5, 3, 8, 11, 2]
print(find_largest(A))
