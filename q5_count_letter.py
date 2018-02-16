# Occurrences of a specified character in a string

def count_letter(str, ch):
    if len(str) == 0:
        return 0
    if len(str) == 1:
        if ch == str:
            return 1
        else:
            return 0
    else:
        return count_letter(str[0:len(str)//2],ch)+ count_letter(str[len(str)//2: ],ch)

string = input("Enter a string: ")
letter = input("Enter a letter: ")
print(count_letter(string, letter))
