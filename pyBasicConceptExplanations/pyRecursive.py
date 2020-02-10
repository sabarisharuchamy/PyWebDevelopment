#Factorial without using Recursive Function
def factorial(n):
    f=1
    while n>0:
        f*=n
        n-=1
        print(f)

#Factorial using Recursive Function
def factorial(n):
    if n==1:
        return 1
    return n*factorial(n-1)

#Sum of n numbers using Recursive Function
def sumofn(n):
    if n==1:
        return 1
    return n+sumofn(n-1)
