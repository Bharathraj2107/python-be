#
# class person:
#     def __init__(self,name):
#         self._name=name
#
#         #getter function
#         def get_name(self):
#             print("Getting name---")
#             return self._name
#
#         #setter function
#         def set_name(self,value):
#             print('setting name to',value)
#             self._name=value
#
#         #delete function
#         def del_name(self):
#             print("deleting name----")
#             del self._name
#
#         #set property() to use get_name,set_name and del_name methods
#         name=property(get_name,set_name,del_name)
#
# p=person('David')
# print(p.name)
# p.name='Rocky'
# del p.name

# class person:
#     def __init__(self,name):
#         self._name=name
#
#     def get_name(self):
#         print('getting name...')
#         return self._name
#     def set_name(self,value):
#         print('setting name to:',value)
#         self._name=value
#
#     def del_name(self):
#         print('deleting names...')
#         del self._name
#     name=property(get_name,set_name,del_name)#it takes above 3 has parameters
#
# p=person('david')
# print(p.name)
# p.name='rocky'
# del p.name
#@propeerty method other way
# class person:
#     def __init__(self,name):
#         self._name=name
#
#     @property
#     def name(self):
#         print("getting name--")
#         return self._name
#
#     @name.setter
#     def name(self,value):
#         print("setting name to ",value)
#         self._name=value
#
#     @name.deleter
#     def name(self):
#         print("deleting name--")
#         del self._name
#
# p=person('David')
# print(p.name)
# p.name='Rocky'
# del p.name

#abstraction
from abc import ABC
# class Shapes(ABC):
#     def araea(self):#abstract method
#         pass
# class Rectangle(Shapes):
#     length=6
#     breadth=4
#     def area(self):
#        return self.length*self.breadth
#
# class Circle(Shapes):
#     radius=7
#     def area(self):
#         return 3.14*self.radius*self.radius
# class square(Shapes):
#     length=4
#     def area(self):
#       return self.length *self.length
#
# r=Rectangle()#creating object for class rectangle
# c=Circle()
# s=square()
# print("the area of rectangle is ",r.area())
# print("the area of circle is",c.area())
# print("the area of square is",s.area())

# from abc import ABC
# class calculate(ABC):
#     def calculate_op(self):
#         pass
# class Add(calculate):
#     a=10
#     b=20
#     def calculate_op(self):
#        return self.a +self.b
# class Sub(calculate):
#     a=10
#     b=20
#     def calculate_op(self):
#         return self.a -self.b
# class Mul(calculate):
#     a=10
#     b=20
#     def calculate_op(self):
#         return self.a *self.b
# class Div(calculate):
#     a=10
#     b=20
#     def calculate_op(self):
#         return self.a /self.b
# class remainder(calculate):
#     a=10
#     b=20
#     def calculate_op(self):
#         return self.a %self.b
# class floordiv(calculate):
#     a=10
#     b=20
#     def calculate_op(self):
#         return self.a //self.b
# add=Add()
# sub=Sub()
# mul=Mul()
# div=Div()
# rem=remainder()
# flv=floordiv()
# print("the addition is ",add.calculate_op())
# print("the subtraction is",sub.calculate_op())
# print("the multiplication is",mul.calculate_op())
# print("the division is ",div.calculate_op())
# print("the remainder is",rem.calculate_op())
# print("the floordivision is",flv.calculate_op())
from abc import ABC
class RBI(ABC):
    loan=int(input("enter the loan amount"))
    def home_loan(self):
        pass
    def hospital_loan(self):
        pass
    def vehicle_loan(self):
        pass
class SBI(RBI):
    def home_loan(self):
            return self.loan*0.5
    def hospital_loan(self):
            return self.loan * 0.7
    def vehicle_loan(self):
            return self.loan * 0.25
class HDFC(RBI):
    def home_loan(self):
            return self.loan*0.8
    def hospital_loan(self):
            return self.loan * 0.9
    def vehicle_loan(self):
            return self.loan * 0.3
class Barath(RBI):
    def home_loan(self):
            return self.loan*0.5
    def hospital_loan(self):
            return self.loan * 0.6
    def vehicle_loan(self):
            return self.loan * 0.2
sb=SBI()
hd=HDFC()
bh=Barath()
choice=input("enter the choice of the bank from which you want to take the loan 1)SBI 2)HDFC 3)BARATH ")
if choice=="SBI":
    loan_type=input("enter the type of loan you need")
    if loan_type=="vehicleloan":
        print("The vehicle loan of sbi",sb.vehicle_loan())
    elif loan_type=="homeloan":
        print("The home loan of sbi",sb.home_loan())
    elif loan_type == "hospitalloan":
        print("The hospital loan of sbi",sb.hospital_loan())
elif choice=="HDFC":
    loan_type = input("enter the type of loan you need")
    if loan_type == "vehicleloan":
        print("The vehicle loan of Hdfc",hd.vehicle_loan())
    elif loan_type == "homeloan":
        print("The home loan of Hdfc",hd.home_loan())
    elif loan_type == "hospitalloan":
        print("The hospital loan of Hdfc",hd.hospital_loan())
elif choice=="BARATH":
    loan_type = input("enter the type of loan you need")
    if loan_type == "vehicleloan":
        print("The vehicle loan of barath",bh.vehicle_loan())
    elif loan_type == "homeloan":
        print("The home loan of barath",bh.home_loan())
    elif loan_type == "hospitalloan":
        print("The hospital loan of barath",bh.hospital_loan())