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


# class Hcf_and_lcm(Algebra):
#     def __init__(self,a):
#         self.a=a
#
#     def hcf_num(self,a):
#      Lcm=math.lcm(self.a)
#      factorial=math.factorial(self.a)
#
#     def hcf_display(self, Lcm, factorial):
#         print(f"Lcm of a number :{Lcm},factorial of a number:{factorial}")
#
# # m1=Hcf_and_lcm(10)
# # m1.hcf_display(10,20)
# m1=Algebra(2)
# m1.algebra_func(2)
# m1.alge_display()
# m1.math_display(10,20,30)
# m1.math_operations(10,20)

# class vehicle:
#
#   def types(self):
#         print("two wheeler")
#         print("four wheeler")
#
# class cars(vehicle):
#     def car_features(self):
#         car=input("enter the car name")
#         seating_capacity=input("enter the seating capacity")
#         speed=input("enter the speed of car required")
#         print(f"It is a {car} it has {seating_capacity} seating capacity and its speed is {speed}")
#
# class BMW(cars):
#
#      def bMW_features(self):
#          model=input("enter the model for BMW:")
#          price=input("enter the price range for BMW:")
#          color=input("enter the color for BMW:")
#          print(f"The car model is {model} it's price is {price} and color is {color}")
# b1=BMW()
# b1.types()
# b1.car_features()
# b1.bMW_features()
# class vehicles:
#     def vehicle(self):
#         print("parent class")
#
# class Two_wheeler(vehicles):
#     def two(self):
#         print("It is a Two_wheeler")
#
# class four_wheeler(vehicles):
#     def four(self):
#         print("It is a four_wheeler")
#
# class six_wheeler(vehicles):
#     def six(self):
#         print("It is a six_wheeler")
#
# h1=six_wheeler()
# h1.two()
# h1.four()
# h1.six
# #hierarchial class
# class Bank_loans:
#  pass
#
# class Health_loan(Bank_loans):
#     def Heth_loan(self):
#         H_money = int(input("enter the money"))
#         if H_money > 4500000 and  H_money<2000000:
#              return H_money * 0.50
#         elif H_money >2000000 and H_money<1000000:
#                 return H_money * 0.25
# class Education_loan(Bank_loans):
#     def Edu_loan(self):
#         E_money =int(input("enter the amount"))
#         if E_money >4500000 and  E_money<2000000:
#               return E_money * 0.50
#         elif E_money >2000000 and E_money<1000000:
#                 return E_money * 0.25
# class vehicle_loan(Bank_loans):
#
#     def veh_loan(self):
#         v_money =int(input("enter the amount"))
#         if v_money >4500000 and v_money<2000000:
#               return v_money * 0.50
#         elif v_money > 2000000 and v_money<1000000:
#                  return  v_money * 0.25
# # v1=vehicle_loan()
# # # v1.veh_loan()
# # E1=Education_loan()
# # E1.Edu_loan()
# H1=Health_loan()
# print(H1.Heth_loan())
class Bank_loans:
    pass

class Health_loan(Bank_loans):
    def Heth_loan(self):
        H_money = int(input("Enter the money: "))
        if 2000000 < H_money <= 4500000:
            return H_money * 0.50
        elif 1000000 < H_money <= 2000000:
            return H_money * 0.25
        else:
            return "Invalid amount for Health Loan"

class Education_loan(Bank_loans):
    def Edu_loan(self):
        E_money = int(input("Enter the amount: "))
        if 2000000 < E_money <= 4500000:
            return E_money * 0.50
        elif 1000000 < E_money <= 2000000:
            return E_money * 0.25
        else:
            return "Invalid amount for Education Loan"

class Vehicle_loan(Bank_loans):
    def veh_loan(self):
        v_money = int(input("Enter the amount: "))
        if 2000000 < v_money <= 4500000:
            return v_money * 0.50
        elif 1000000 < v_money <= 2000000:
            return v_money * 0.25
        else:
            return "Invalid amount for Vehicle Loan"
# v1=Vehicle_loan()
# print( v1.veh_loan())
# E1=Education_loan()
# print(E1.Edu_loan())

# Usage example
H1 = Health_loan()
print(H1.Heth_loan())