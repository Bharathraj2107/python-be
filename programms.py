from abc import ABC
class company:
    print("This is a  software company")
    salary_fulltime=30000
    salary_hourly=0
    # def fullemp_salary(self):
    #     pass
    # def hourly_salary(self):
    #     pass
# class full_time_employees(company):
#     def fullemp_salary(self):
#         holiday=int(input("enter the number of holidays taken by fulltime employee"))
#         if holiday<3:#company has minimum holidays per month
#             print("There is no salary detection")
#             return self.salary_fulltime
#         else:
#             salary=self.salary_fulltime-holiday*500
#             return salary
#
# class hourly_employee(company):
#     def hourly_salary(self):
#         hour=int(input("enter the number of hours worked by the partime employee"))
#         self.hourly_salary=hour*500
#         holiday=int(input("enter the number o holidays taken by parttime employee"))
#         if holiday<3:#company has minimum holidays per month
#             print("There is no salary detection")
#             return self.hourly_salary
#         else:
#            salary=self.hourly_salary-holiday*200
#            return salary
#
# ef=full_time_employees()
# eh=hourly_employee()
# print("The salary of a fulltime employeee",ef.fullemp_salary())
# print("The monthly salary of a hourly worker is ",eh.hourly_salary())
#2
# from abc import ABC, abstractmethod

# class PaymentGateway(ABC):
#     def __init__(self, amount):
#         self.amount = amount#for that instances this
#         #amount is assigned ex:py.amount,sq.amount,st.amount
#
#     def process_payment(self):
#         pass
#
# class PayPal(PaymentGateway):
#     def process_payment(self):
#         print(f"The {self.amount} paid successfully with PayPal")
#         if 100 < self.amount <= 500:
#             refund_amount = 50
#             return f"Refund amount: {refund_amount}"
#         elif self.amount > 500:
#             refund_amount = 150
#             return f"Refund amount: {refund_amount}"
#         else:
#             return "Better luck next time!"
#
# class Stripe(PaymentGateway):
#     def process_payment(self):
#         print(f"The {self.amount} paid successfully with Stripe")
#         if 100 < self.amount <= 500:
#             refund_amount = 50
#             return f"Refund amount: {refund_amount}"
#         elif self.amount > 500:
#             refund_amount = 150
#             return f"Refund amount: {refund_amount}"
#         else:
#             return "Better luck next time!"
#
# class Square(PaymentGateway):
#     def process_payment(self):
#         print(f"The {self.amount} paid successfully with Square")
#         if 100 < self.amount <= 500:
#             refund_amount = 50
#             return f"Refund amount: {refund_amount}"
#         elif self.amount > 500:
#             refund_amount = 150
#             return f"Refund amount: {refund_amount}"
#         else:
#             return "Better luck next time!"
#
#
# amount = int(input("Enter the amount you want to pay: "))
#
# py = PayPal(amount)
# st = Stripe(amount)
# sq = Square(amount)
#
# choice = input("Enter the choice from which you want to pay (1)PayPal (2)Stripe (3)Square: ")
#
# if choice == "1":
#     print(py.process_payment())
# elif choice == "2":
#     print(st.process_payment())
# elif choice == "3":
#     print(sq.process_payment())
# else:
#     print("Invalid choice!")
#3
# class Movie:
#     def __init__(self,title,director,actors,reviews):
#         self.title=title
#         self.director=director
#         self.actors= actors
#         self.reviews = reviews
#         self.list_movies={
#             "Ramachari":["It is a good romantic movie"],
#             "conjuring":["It is a horror movie "],
#             "JameBond":["It is a action thriller movie"],
#             "TomandJerry":["It is a comedy cartoon"]
#         }
#
#     def add_review(self):
#         print("The movies available are")
#         for i in self.list_movies:
#             print(i)
#         self.title=input("enter the movie title to which you want to write review")
#         if self.title in self.list_movies:
#             self.reviews=input("enter the review about the movie")
#             self.list_movies[self.title]=self.reviews
#
#         elif self.title not in self.list_movies:
#             self.reviews = input("enter the review about the movie")
#             self.list_movies[self.title]=self.reviews
#
#
#     def retriew_review(self):
#         self.title=input("enter the movie title for which you want reviews")
#         if self.title in self.list_movies:
#             print(f"The reviews of the movie {self.title} are {self.list_movies[self.title]}")
# m=Movie('Anjan','A.R murgadose',['surya','samantha'],"Romantic Thriller")
# m.add_review()
# m.retriew_review()
#4
# class Bank:
#     def __init__(self):
#         self.__username="BharathRaj"
#         self.__password="1234"
#     def account_access(self):
#         username=input("enter the username")
#         password=input("enter the password")
#         if username==self.__username and password==self.__password:
#             print("Access Granted")
#         else:
#             print("Invalid username or password")
#
# b=Bank()
# b.account_access()