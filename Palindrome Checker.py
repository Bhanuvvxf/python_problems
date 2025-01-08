#Palindrome Checker
string1 = input("Enter a string : ")
list = list(string1)
list.reverse()
string2 = ""
for i in range(len(list)):
    string2 += list[i]
if string1 == string2 :
    print(f"{string1} is a palindrome .")
    