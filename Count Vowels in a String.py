#count vowels in a string 
list = list(input("Enter a string : ").lower())
print(f"Number of vowels: {list.count("a")+list.count("e")+list.count("i")+list.count("o")+list.count("u")}")
