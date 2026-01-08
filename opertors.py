price = 1000
gst = price * 18 / 100
total_bill = price + gst

print("Product Price:", price)
print("GST:", gst)
print("Total Bill Amount:", total_bill)
total_students = 53
group_size = 5

remainder = total_students % group_size
print("Remaining students:", remainder)

power = 5
hours = 3

consumption = power ** hours
print("Power Consumption:", consumption)

age = 20

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")
salary_A = 45000
salary_B = 50000

if salary_A > salary_B:
    print("Employee A earns more")
else:
    print("Employee B earns more")
saved_pin = 1234
entered_pin = 1234

print("PIN Correct:", saved_pin == entered_pin)
marks = 65
attendance = 80

if marks > 40 and attendance > 75:
    print("Student Passed")
else:
    print("Student Failed")

username = ""
email = "user@gmail.com"

if username or email:
    print("Login Allowed")
else:
    print("Login Denied")


suspended = False

if not suspended:
    print("Access Granted")
else:
    print("Access Blocked")

wallet = 2000
shopping = 750

wallet -= shopping
print("Remaining Wallet Balance:", wallet)

score = 10
score += 5

print("Updated Score:", score)
stock = 100
sold = 20

stock -= sold
print("Remaining Stock:", stock)

a = 5   
b = 3   

print("AND:", a & b)
print("OR:", a | b)

num = 4
print("Left Shift:", num << 1)

num = 8
print("Right Shift:", num >> 1)
students = ["Alice", "Bob", "Charlie"]
name = "Bob"

print(name in students)

inventory = ["Laptop", "Phone", "Tablet"]

product = "Phone"
print(product in inventory)


x = 10
y = 10
z = 20

print(x is y)   
print(x is not z)  
