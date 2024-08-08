# class cars:
#     # def __init__(self,name,color,price):
#     #     self.name=name
#     #     self.color=color
#     #     self.price=price
#     def cars_info(self):
#        self. name=input("enter name")#we haveto use self compulsory
#        self. color=input("enter the color")
#        self. price = input("enter the price")
#     def display(self):
#         print(self.name,self.color,self.price)
# c1=cars()
# c1.cars_info()
# c1.display()
#single in heritances
# class ABC_company:
#     def __init__(self,name,age,sal):
#         self.name = name
#         self.age = age
#         self.sal = sal
#
# class employee(ABC_company):
#
#     def __init__(self, name,age,sal ,address):
#         self.name = name
#         self.age = age
#         self.sal = sal
#         self.address = address
#
#     def emp_dtls(self):
#         print(self.name,self.age,self.sal,self.address)
#
# e1=employee("raj",23,23000,"Bangalore")
# e1.emp_dtls()

# class BE_Practicals:
#     def __init__(self,location,course,guide_name):
#         self.guide_name = guide_name
#         self.location = location
#         self.course = course
#
# class student(BE_Practicals):
#
#     def __init__(self,guide_name,location,course,stuname,stuage):
#         self.guide_name = guide_name
#         self.location = location
#         self.course = course
#         self.name = stuname
#         self.age = stuage
#
#     def stu_dtls(self):
#         print(f"Guide_name:{self.guide_name} \n BE practical Institution:{self.location} \n course: {self.course} \n student_name:{self.name} \n student_age:{self.age}\n")
#
# s1=student("Namitha","Basvashvanagar","Python","Bharath raj",23)
# s1.stu_dtls()

#multilevel inheritances
import math
class maths:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def math_operations(self,a,b):
       add=self.a + self.b
       sub= self.a - self.b
       Mul = self.a * self.b

    def math_display(self,add,sub,Mul):
        print(f"Addition:{add},Subtraction:{sub},Multiplication:{Mul}")

class Algebra(maths):
    def __init__(self,a):
        self.a=a
    def algebra_func(self,a):
        sqrt=math.sqrt(self.a)
        floor_num=math.floor(self.a)
        ceil_num=math.ceil(self.a)

    def alge_display(self, sqrt, floor_num, ceil_num):
        print(f"square root:{sqrt},Floor number:{floor_num},Ceil number:{ceil_num}")


class Hcf_and_lcm(Algebra):
    def __init__(self,a):
        self.a=a

    def hcf_num(self,a):
     Lcm=math.lcm(self.a)
     factorial=math.factorial(self.a)

    def hcf_display(self, Lcm, factorial):
        print(f"Lcm of a number :{Lcm},factorial of a number:{factorial}")

m1=Hcf_and_lcm(10)
m1.hcf_display(10,20)
m1.alge_display(49,22.3,32.2)
m1.math_display(10,20,30)
m1.math_operations(10,20)