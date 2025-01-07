#Reverse a String

string = input("Enter a string : ")
list = list(string)
list.reverse()
reversed_string = ""
for i in list:
    reversed_string += i
print(f"Reversed string : {reversed_string}")