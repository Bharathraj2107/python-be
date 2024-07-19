#Numbers in Python can be reversed as strings but not directly as integers.
# For example, if you have the number 12321, reversing it as an integer is not straightforward,
# but reversing a string representation of it ("12321") is simple.
#argument with return function
# def add(a,b):
#     return a+b
# def sub(a,b):
#     return a-b
# def div(a,b):
#     return a/b
# v1=int(input("enter the number"))
# v2=int(input("enter the number"))
# print("-------------------------")
# print("Select (1) for addition")
# print("Select (2) for Subtraction")
# print("Select (3) for division")
# print("-----------------------")
# ch=int(input("enter the choice"))
# if ch==1:
#     print(f"{v1}+{v2} addition is ",add(v1,v2))
# if ch==2:
#     print(f"{v1}+{v2} Subtraction is ",sub(v1,v2))
# if ch==3:
#     print(f"{v1}+{v2} division is ",div(v1,v2))
#argument and no return value
# def multiply(x,y):
#     print("value of x=",x)
#     print("value of y=", y)
#     c=x*y
#     print(c)
# multiply(y=2,x=4)
#function with no argument,no return value
# def factorial_number():
#     factorial=1
#     num=int(input("enter a number to get its factorial"))
#     for i in range(1,num+1):
#         factorial=factorial*i
#     print("The factorial is",factorial)
# factorial_number()
#no argument with  return value
# my_list=[23,44,66,74,23]
# def add_list():
#     sum=0
#     for list_item in my_list:
#         sum=sum+list_item
#     return sum
# result=add_list()
# print("The result is ",result)
#argument with return function
# def pallin(num):
#     real=str(num)
#     rev=real[::-1]
#     if real==rev:
#         return True
#     else:
#         return False
#
# num=int(input("enter the number"))
# print(pallin(num))

#argument and no return value
# def pallin(num):
#     real=str(num)
#     rev=real[::-1]
#     if real==rev:
#         print("pallindrome")
#     else:
#         print("not a pallindrome")
# num=int(input("enter the number"))
# pallin(num)
#no argument no return value
# def pallin():
#     num = int(input("enter the number"))
#     real=str(num)
#     rev=real[::-1]
#     if real==rev:
#          print("pallindrome")
#     else:
#          print("not a pallindrome")
# pallin()
#no argument with return function
# def pallin():
#     num=int(input("enter the number"))
#     real = str(num)
#     rev=real[::-1]
#     if real==rev:
#         return True
#     else:
#         return False
#
# print(pallin())
