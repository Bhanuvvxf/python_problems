#Data Validation

dictionary = {}

while True:
    key = input("Entet the key (or Exit) : ")
    if key == "Exit":
        break
    value = input("Enter the value : ")

    dictionary[key] = value

"""
If the dictionary has "name" and "age", print the name and age.

If the dictionary has "name" and "email" print the name and email.

If it only contains name, print just the name.

If it contains any other combination, print an "Invalid data" message.


"""

match dictionary:
    case {"name":x ,"age":y}:
        print(f"Name : {x} and Age : {y}.")
    case {"name":x}:
        print(f"Name : {x}")
    case {"name":x,"email":y}:
        print(f"Name : {x} and Email : {y}")
    case {"email":x}:
        print(f"Email : {x}")
    case {"age": x}:
        print(f"Age : {x}")
    case _ :
        print("Invalid data . ")