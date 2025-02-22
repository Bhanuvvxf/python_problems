#Number Classifier

number = int(input("Enter the number : "))

result = ""

if number > 0 :
    result += "Pasitive "
    if number % 2 == 0 :
        result += "and Even "
    else:
        result += "and Odd "
elif number < 0 :
    result += "Nagative "
    if number % 2 == 0 :
        result += "and Even "
    else:
        result += "and Odd"
else:
    result += "Zero"

print(result)
        

    