
#Simple Calculator
frist_number = int(input("Enter frist number : "))
second_number = int(input("Enter second number : "))
operator = input("Enter operator (+,-,*,/): ")
if operator == "+" :
    print(f"Result: {frist_number + second_number }")
elif operator == "-":
    print(f"Result: {frist_number - second_number}")
elif operator == "*":
    print(f"Result: {frist_number * second_number}")
elif operator == "/":
    print(f"Result: {frist_number - second_number}")
else:
    print("Enter the valid operator")