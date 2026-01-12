#prime function
def is_prime(n):
    if n<=1:
        return False
    for i in range(2, n):
        if n %i==0:
            return False
    return True
num =int(input("enter a number:"))
if is_prime(num):
    print("prime number")
else:
    print("not prime number")

#factorial function
def factorial(n):
    f=1
    for i in range(1, n+1):
        f*=i
    return f
n=int(input("enter number:"))
print("factorial is:",factorial(n))

#largest of three
def largest(a,b,c):
    if a>b and a>c:
        return a
    elif b>c:
        return b
    else:
        return c
x=int(input("enter first number:"))
y=int(input("enter second number:"))
z=int(input("enter third number:"))
result=largest(x,y,z)
print("largest number is:",result)

#
def simple_interest(p,r,t):
    si=(p*r*t)/100
    return si
p=float(input("enter principal:"))
r=float(input("enter rate of inrerset:"))
t=float(input("enter time(in years):"))
result=simple_interest(p,r,t)
print("simple interest=",result)

#function palindrome
def is_palindrome(n):
    temp=n
    rev=0
    while n>0:
        rev=rev*10+n%10
        n=n//10
    if temp == rev:
        return "palindrome"
    else:
        return "not palindrome"
num=int(input("enter a number:"))
num1=int(input("enter a number:"))
print(is_palindrome(num,num1))

