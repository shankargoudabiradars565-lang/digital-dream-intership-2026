name=input("enter employee name:")
salary=float(input("enter salary:"))
rating=int(input("enter performance ratinh(1-5):"))
if rating==5:
    bonus=0.20*salary
elif rating==4:
    bonus=0.15*salary
elif rating==3:
    bonus=0.10*salary
else:
    bonus=0
final_salary = salary+bonus
print("\n-----------bonus summary-----------")
print("employee name:",name)
print("performance rating:",rating)
print("bonus amount:",bonus)
print("final slary:",final_salary)
