#print 1 to n
n=int(input("enter n:"))
for i in range(1,n+1):
    print(i)

#multiplication table
n=int(input("enter number"))
for i in range(1,11):
    print(n, "x", i, "=",n*i)

#sum n natural numbers
n=int(input("enter n:"))
sum=0
for i in range(1,n+1):
    sum+=i
print("sum:",sum)

#count digits
n=int(input("enter number:"))
count=0
while n>0:
    count+=1
    n//=10
print("digits:",count)

#reverse number
n=int(input("enter number:"))
rev=0
while n>0:
    rev=rev*10+n%10
    n//=10
print("reverse:",rev)
