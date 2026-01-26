class phone:
    def make_call(self):
        print("making phone call")
    def play_game(self):
        print("playing game")
p1=phone()
p1.make_call()
p1.play_game()

#class constrauctor
class Employee:
    def __init__(self,name,age,salary,gender):
        self.name=name
        self.age=age
        self.salary=salary
        self.gender=gender
    def employee_details(self):
        print("\n \n name of employee is",self.name)
        print("age of employee is",self.age)
        print("salary of employee is",self.salary)
        print("gender of employee is",self.gender)
e1=Employee('sam',32,85000,'male')
e1.employee_details()

#inheritance
class Vehicle:
    def __init__(self,mileage,cost):
        self.mileage=mileage
        self.cost=cost
    def show_details(self):
        print("\n \n I am a Vehicle")
        print("Mileage of Vehicle is",self.mileage)
        print("cost of Vehicle is", self.cost)
v1=Vehicle(500,500)
v1.show_details()

class Car(Vehicle):
    def show_car(self):
        print("\n I am a car")
c1=Car(200,1200)
c1.show_details()
c1.show_car()

#over riding int method
class Car(Vehicle):
    def __init__(self, mileage, cost, tyres, hp):
        super().__init__(mileage, cost)
        self.tyres = tyres     
        self.hp = hp

    def show_car_details(self):
        print("\n I am a car")
        print("number of tyres is", self.tyres)
        print("value of horse power is", self.hp)
c1=Car(20,12000,4,300)
c1.show_details()
c1.show_car_details()

#multiple inheritance
class Parent1():
    def assign_string_one(self,str1):
        self.str1=str1
    def show_string_one(self):
        return self.str1
class Parent2():
    def assign_string_two(self,str2):
        self.str2=str2
    def show_string_two(self):
        return self.str2
class Derived(Parent1,Parent2):
    def assign_string_three(self,str3):
        self.str3=str3
    def show_string_three(self):
        return self.str3
d1=Derived()
d1.assign_string_one("one")
d1.assign_string_two("two")
d1.assign_string_three("three")
print(d1.show_string_one())
print(d1.show_string_two())
print(d1.show_string_three())

#multi-level inheritance
class Parent:
    def assign_name(self, name):
        self.name = name

    def show_name(self):
        return self.name


class Child(Parent):
    def assign_age(self, age):
        self.age = age

    def show_age(self):
        return self.age


class GrandChild(Child):
    def assign_gender(self, gender):
        self.gender = gender

    def show_gender(self):
        return self.gender


g1 = GrandChild()
g1.assign_name("Sam")
g1.assign_age(25)
g1.assign_gender("Male")

print(g1.show_name())
print(g1.show_age())
print(g1.show_gender())
