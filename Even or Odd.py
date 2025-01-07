# Even or Odd
number = int(input("Enter a number : "))
if number % 2 == 0 :
    print(f"{number} is Even.")
elif number % 2 != 0:
    print(f"{number} is odd.")
else:
    print("Enter only numbers .")