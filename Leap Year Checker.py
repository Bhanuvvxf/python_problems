#Leap Year Checker

year = int(input("Enter your year (To check leap year): "))

if year % 4 == 0 and year % 400 != 0 :
    print("Leap year")
else:
    print("Not a Leap Year.")