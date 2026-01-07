name=input("enter name")
age=int(input("enter age"))
email_id=input("enter email_id")
contact_no=input("enter contact no")
g_percentage=float(input("enter g_percentage"))
if age<=18:
    print("reject:age must be 18 or above")
elif g_percentage<60:
    print("reject:percentage must be 60% or above")
elif len(contact_no)!=10:
         print("rejected:conatct no must be extacly 10 digits")
else:
    print("intern eligible for intership")
