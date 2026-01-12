#even numbers 1-100
for i in range(1,101):
    if i % 2==0:
        print(i)

#prime number check
n=int(input("enter number:"))
flag = True
for i in range(2,n):
    if n %i==0:
        flag=False
        break
if  flag and n>1:
    print("prime")
else:
    print("not prime")

#factorial
n=int(input("enter number:"))
fact=1
for i in range(1,n+1):
      fact*=i
print("factorial:",fact)

#fibonacci series
n=int(input("enter terms:"))
a,b=0,1
for i in range(n):
    print(a)
    a,b=b,a+b

#sum of digits
n=int(input("enter number:"))
sum=0
while n>0:
    sum+=n%10
    n//=10
print("sum of digits:",sum)
