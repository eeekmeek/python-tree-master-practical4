# Finding the number of uppercase letters in a string

def find_num_uppercase(str):
    if len(str) == 0:
        return 0
    if 65 <= ord(str[0]) <= 90:
        return find_num_uppercase(str[1:]) + 1
    else:
        return find_num_uppercase(str[1:])

string = input("Enter a sentence: ")
print("Number of uppercase: ",find_num_uppercase(string))
