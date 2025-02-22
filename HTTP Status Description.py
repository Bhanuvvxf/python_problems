#HTTP Status Description
"""
Create a match-case statement to take an HTTP status code
 (e.g., 200, 404, 500) as input.

Print a descriptive message for each code
 (e.g., "OK", "Not Found", "Internal Server Error").

Include a wildcard case for unknown codes.
"""

while True :

    try:
        code1 = int(input("Enter the code : "))
    
    except (ValueError ,NameError):
        print("Enter only number . ")

    match code1:
        case 200:
            print("Ok")
            break
        case 404:
            print("Not Found")
            break
        case 500:
            print("Internal server error . ")
            break
        case _:
            print("Others")
            break