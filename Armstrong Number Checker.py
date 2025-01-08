#Armstrong Number 
number1  = int(input("Enter a  number : "))
list = list(str(number1))
number2 = 0
for i in range(len(list)):
    number2 += int(list[i])**3
if number1 == number2 :
    print(f"{number1} is a Armstrong Number .")