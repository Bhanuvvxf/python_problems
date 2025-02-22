#Grade Checker

try:
    score = int(input("Enter your score : "))
except ValueError:
    score = int(input("Enter score in only numbers : "))


if score > 100 or score < 0 :
    score = int(input("Enter score between( 1 to 100 ) : "))
else:
    if score >= 90 :
        print("A")
    elif score >= 80 and score <= 89:
        print("B")
    elif score >= 70 and score <= 79:
        print("C")
    elif score >= 60 and score <= 69 :
        print("D")
    else:
        print("F")

    
