employee_name=input("enter the employee name:")
employee_id=int(input("enter the employee id:"))
basic_salary=float(input("enter basic salary"))
hra=0.20
da=0.10
pf=0.12
net_salary=basic_salary+hra+da-pf
print("employee name:",employee_name)
print("employee id:",employee_id)
print("basic salary:",basic_salary)
print("hra(20%):",hra)
print("da(10%):",da)
print("pf(12%):",pf)
print("net salary:",net_salary)
