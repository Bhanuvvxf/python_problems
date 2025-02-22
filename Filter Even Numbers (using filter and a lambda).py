#Filter Even Numbers (using filter and a lambda)

even_numbers = filter(lambda x : x%2==0 , range(0,int(input("Enter the number : "))))
print(list(even_numbers))