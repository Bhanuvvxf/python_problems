#List Statistics

def Statistics(numbers):

    sum_of_numbers = sum(numbers)
    average_of_numbers = sum(numbers)/len(numbers)
    sorted_numbers = sorted(numbers)
    min_number = sorted_numbers[0]
    max_number = sorted_numbers[-1]

    dict =  {"Sum ":sum_of_numbers,"Average ":average_of_numbers,"Max ":max_number,"Min ":min_number}
    return dict

numbers = []

while True:

    number = input("Enter the number (or Exit) : ")

    if number == "Exit":
        break

    numbers.append(int(number))


print(Statistics(numbers))