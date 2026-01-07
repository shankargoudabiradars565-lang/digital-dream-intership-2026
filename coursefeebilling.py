print("Available courses:")
print("1.python programming:")
print("2.data analysis")
print("3.al&ml")
course=input("enter course name:")
is_student=input("are you a student?(yes/no):")
early_reg=input("early registration?(yes/no):")
if course.lower()=="python programming":fee=5000
elif course.lower()=="data analysis":fee=8000
elif course.lower()=="ai&mi":fee=12000
else:
    print("invalid course selected")
    exit()
discount=0
if is_student.lower()=="yes":discount+=0.10*fee
if early_reg.lower()=="yes":discount+=0.05*fee
final_amount=fee-discount
print("/n -------fee details----------")
print("course name:",course)
print("original fee:$",fee)
print("total discount:$",discount)
print("final payable:$",final_amount)
