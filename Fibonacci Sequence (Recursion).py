#Fibonacci Sequence (Recursion)

def FS(n):

    if n <= 1:
        return n
    else:
        return (FS(n-1)+FS(n-2))
print(FS(int(input("Enter your number : "))))


