#check positive ,negative or zero
n=int(input("enter number:"))
if n>0:
    print("positive")
elif n<0:
    prinr("negative")
else:
    print("zero")

#check even or odd
n=int(input("enter number:"))
if n%2==0:
    print("even")
else:
    print("odd")

#largest of three numbers
a=int(input("enter a:"))
b=int(input("enter b:"))
c=int(input("enter c:"))
if a>b and a>c:
    print("largest a:",a)
elif b>c:
    print("largest b:",b)
else:
    print("largest c:",c)

#leap year check
year=int(input("enter year:"))
if(year % 4==0 and year % 100!=0) or year %400==0:
    print("leap year")
else:
    print("not a leap year")

#grade calculation
marks=int(input("enter marks:"))
if marks>=90:
    print("grade a")
elif marks>=75:
    print("grade b")
elif marks>=50:
    print("grade c")
else:
    print("fail")
        
