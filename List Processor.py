#List Processor

list = []

while True:
    x = input("Enter the number (you added completed then enter Exit) : ")
    if x == "Exit":
        break
    list.append(x)

match list:
    case []:
        print("Empty")
    case [x]:
        print(f"Single element : {x}")
    case [x,y]:
        print(f"Two elements : {x},{y}")
    case [x,*rest]:
        print(f"Frist element : {x},Reamaining elements {rest}")
    case _ :
        print("other")