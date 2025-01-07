#Fibonacci Series
number = int(input("Enter N :"))
list = [0,1]
i = 0
j = 1
while list[-1] < number:
    z = list[i] + list[j] 
    list.append(z)
    i += 1
    j += 1

list.pop()
print(list)
    