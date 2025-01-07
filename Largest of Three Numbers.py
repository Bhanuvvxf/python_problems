#Largest of Three Numbers
a,b,c = int(input("Enter frist number : ")) ,int(input("Enter second number : ")) ,int(input("Enter third number : "))
if a > b and a > c:
    print(f"largest number : {a}")
elif b > a and b > c:
    print(f"largest number : {b}")
else:
    print(f"largest number : {c}")