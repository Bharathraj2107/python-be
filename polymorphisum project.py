#bank main class
#2 diff child class
#2 methods same for 2 class
class Bank:
    def __init__(self):
         self.total_money=0
class SBI(Bank):
    def loan(self):
        money=int(input("enter the money u need for loan"))
        if money>10000:
            total_money = money * 0.5
            print(f"{money} is greater than thousand so interest rate is 0.5 .The Total amount is ",total_money)
        else:
            total_money = money * 0.25
            print(f"{money} is less than thousand so interest rate is 0.25 .The total amount is",total_money)

class HDFC(Bank):
    def loan(self):
        money=int(input("enter the money u need for loan"))
        if money>10000:
            total_money = money * 0.5
            print(f" {money} is greater than thousand so interest rate is 0.5 .The total amount is",total_money)
        else:
            total_money = money * 0.25
            print(f" {money} is less than thousand so interest rate is 0.25.The total amount is ",total_money)

def create_object(object):
    object.loan()
create_object(SBI())
create_object(HDFC())
# s1=SBI()
# s1.
# s2=HDFC()

#base class institute
#when function called enter login for all the 3 class to downolad brocher if initially login not required
# class institute:
#     def login(self):
#         Email=input("Enter the email:")
#         Password=input("Enter the password:")
#         if '1234' == Password and 'Bharath123@gmail.com'==Email:
#             print("Access Granted")
#         else:
#             print("Access Denied")
#
# class python_brochure(institute):
#     pass
# class Mern_stack(institute):
#     pass
# I1=institute()
# py=python_brochure()
# M1=Mern_stack()
# for obj in (I1,py,M1):
#     obj.login()