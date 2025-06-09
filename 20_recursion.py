# function call itself

def sum(n):
    if n == 1:  # Base case
        return 1
    else:
        return n + sum(n - 1)

a=int(input("enter numbers"))

print(sum(a))  
