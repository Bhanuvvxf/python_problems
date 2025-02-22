#Palindrome Checker

def Palindrome_Checker(s):
    s.lower()
    return s == s[::-1]

print(Palindrome_Checker(input("Enter the word : ")))