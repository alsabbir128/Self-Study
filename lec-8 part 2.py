##1(class and object)

# class Student:
#     name = "karan kumar"

# s1 = Student()
# print(s1.name)

# s2 = Student()
# print(s2.name)

##2(class and instance attributes)

# class Car:
#     color = "blue"
#     brand = "mercedes"

# car1 = Car()
# print(car1.color)
# print(car1.brand)

##3(constructor)

# class Student:
#     name = "karan kumar"
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#         print("adding new student in database..") 
    
# s1 = Student("karan",98)
# print(s1.name, s1.marks) #karan

# s2 = Student("arjun", 88)
# print(s2.name, s2.marks) #arjun

##4(methods)

# class Student:
#     #default Constructors
#     def __init__(sefl):
#         pass
#     #parameterized constructors
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#         print("adding new student in database..") 
    
# s1 = Student("karan",98)
# print(s1.name, s1.marks) #karan

# s2 = Student("arjun", 88)
# print(s2.name, s2.marks) #arjun

##5(static method)

# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
        
#     @staticmethod #its not working now 
#     def collage():
#         print("ABC collage")

#     def get_avg(self):
#         sum = 0
#         for val in self.marks:
#             sum += val
#         print("hi", self.name, "your avg score is",sum/3)

# s1 = Student("tony stark", [99,98,96])
# s1.get_avg()

# s1.name = "Ironman"
# s1.get_avg()

##6(Abstraction)

# class Car:
#     def __init__(self):
#         self.acc = False
#         self.brk = False
#         self.clutch = False

#     def start(self):
#         self.clutch = True
#         self.acc = True
#         print("Car started...")

# car1 = Car()
# car1.start()

##7(practice)Create Account class with 2 attributes - balance & account no. Create method for debit, credit & printing the balance.

# class Account:
#     def __init__(self, bal, acc):
#         self.balance = bal
#         self.account_no = acc

#     def debit(self, amount):
#         self.balance -= amount
#         print("Rs.", amount, "was debited")
#         print("total balance", self.get_balance())

#     def credit(self, amount):
#         self.balance += amount
#         print("Rs.", amount, "was credited")
#         print("total balance", self.get_balance())

#     def get_balance(self):
#         return self.balance
    

# a1 = Account(14455, 20090)
# a1.debit(1000)
# a1.credit(500)
# a1.credit(40000)

##8(Multi level inheritance)

# class Car:
#     @staticmethod
#     def start():
#         print("car started..")

#     @staticmethod
#     def stop():
#         print("car stoped")

# class ToyotaCar(Car):
#     def __init__(self, brand):
#         self.brand = brand

# class Forturer(ToyotaCar):
#     def __init__(self, type):
#         self.type = type

# car1 = Forturer("diesel")
# car1.start()

##9(Multiple Inheritance)

# class A:
#     val1="A"
# class B:
#     val2="B"
# class C(A, B):
#     val3="C"

# c1 = C()

# print(c1.val1)
# print(c1.val2)
# print(c1.val3)

##10(super method)

# class Car:
#     def __init__(self, type):
#         self.type = type
    
#     @staticmethod
#     def start():
#         print("car started..")

#     @staticmethod
#     def stop():
#         print("car stoped")

# class ToyotaCar(Car):
#     def __init__(self, name, type):
#         super().__init__(type)
#         self.name = name


# car1 = ToyotaCar("prius", "electric")
# print(car1.type)

##11(class method)

# class person:
#     name = "anonymous"

#     def changeName(self, name):
#         self.__class__.name = "rahi"
#         #self.__class__. /Person.

# p1 = person()
# p1.changeName("rahul kumar")
# print(p1.name)
# print(person.name)

##12(property)

# class Student:
#     def __init__(self, phy, chem, math):
#         self.phy = phy
#         self.chem = chem
#         self.math = math
#         #self.percentage = str((self.phy + self.chem + self.math) / 3) + "%"
#     @property
#     def percentage(self):
#         return str((self.phy + self.chem + self.math) / 3) + "%"

# stut1 = Student(98, 99, 97)
# print(stut1.percentage)

# stut1.phy = 86 
# print(stut1.percentage)

##13(polymorphism : operators and dunder function)

# class Complex:
#     def __init__(self,real,img):
#        self.real = real
#        self.img = img

#     def showNumber(self):
#         print(self.real,"i +", self.img,"j")
    
#     def __add__(self, num2):
#         newReal = self.real + num2.real
#         newImg = self.img + num2.img
#         return Complex(newReal, newImg)
    
#     def __sub__(self, num2):
#         newReal = self.real - num2.real
#         newImg = self.img - num2.img
#         return Complex(newReal, newImg)

# num1 = Complex(1 , 3)
# num1.showNumber()
# num2 = Complex(3 , 5)
# num2.showNumber()

# num3 = num1 - num2
# num3.showNumber()

##14(practice - 1)
#Define a Circle class to create a circle with radius r using the constructor.
#Define an Area() method of the class which calculates the area of the circle.
#Define a Perimeter() method of the class which allows you to calculate the perimeter of the circle.

# class Circle:
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return (22/7) * self.radius ** 2
    
#     def perimeter(self):
#         return 2 * (22/7) * self.radius
    
# c1 = Circle(7)
# print(c1.area())
# print(c1.perimeter())

##15(practice - 2)
#Define a Employee class with attributes role, department and salary. This class also has a showDetails() method.
#Create an Engineer class that inherits properties from Employee and has additional attributes: name & age

# class Employee:
#     def __init__(self, role, dept, salary):
#         self.role = role
#         self.dept = dept
#         self.salary = salary

#     def showDetails(self):
#         print("role =", self.role)
#         print("dept =", self.dept)
#         print("salary =", self.salary)

# class Engineer(Employee):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         super().__init__("Engineer", "IT", "75,000")

# engg1 = Engineer("Elon Mask", 40)    
# engg1.showDetails()
# e1 = Employee("accountant", "Finance", "60,000")
# e1.showDetails()

##16(practice - 3)
#Create a class called order which stores item and its price.
#Use Dunder function __gt__() to convey that:
#order1>order2 if price of order1> price of order2

class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price
    def __gt__(self, or2):
        return self.price > or2.price
        
or1 = Order("chips", 10)
or2 = Order("tea", 15)

print(or1 > or2)