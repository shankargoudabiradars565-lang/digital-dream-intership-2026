def is_prime(n):
    if n<=1:
        return False
    for i in range(2, n):
        if n%i==0:
            return False
    return True
def primes_in_range(a,b):
    for n in range(a, b+1):
        if is_prime(n):
            print(n)
primes_in_range(10,30)

#vowels constonants
def count_vowels_consonants(s):
    vowels=0
    consonants=0
    for ch in s.lower():
        if ch in "aeiou":
            vowels+=1
        elif ch.isalpha():
            consonants+=1
    print("vowels:",vowels)
    print("consonants:",consonants)
text=input("enter a string:")
count_vowels_consonants(text)

#armstrong
def is_armstrong(n):
    temp=n
    sum=0
    while n>0:
        digit=n%10
        sum=sum+digit**3
        n=n//10
    if temp==sum:
        print("Armstrong number")
    else:
        print("not an Armstrong number")
num=int(input("enter a number:"))
is_armstrong(num)

#function fibonacci
def fibonacci(n):
    a,b=0, 1
    for i in range(n):
        print(a, end=" ")
        a,b=b,a+b
num=int(input("enter number of terms:"))
fibonacci(num)

#function sum of even and odd
def even_odd_sum(lst):
    even_sum=0
    odd_sum=0
    for num in lst:
        if num%2 ==0:
            even_sum+=num
        else:
            odd_sum+=num
    print("\n sum of even numbers:",even_sum)
    print("sum of odd numbers:",odd_sum)
numbers=[1,2,3,4,5,6,7]
even_odd_sum(numbers)
