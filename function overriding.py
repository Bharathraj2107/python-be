#runtime overriding
#polymorphism method overriding with functions and objects
# class parrot:
#     def __init__(self,color):
#         self.color=color
#     def features(self):
#         print("The color of the parrot is ::",self.color)
#         print("The parrot can fly")
#
# class ostrich:
#     def __init__(self,color):
#         self.color=color
#     def features(self):
#         print("the color of the ostrich is",self.color)
#         print("the ostrich cannot fly")
# #define the function to call the method of class
# def create_object(object):
#     object.features()
# #create object of parrot class
# create_object(parrot("green"))
# create_object(ostrich("Black and white"))
#polymorphism in unrelated class methods
# class Manager:
#     def __init__(self,name,department):
#         self.name=name
#         self.post='Manager'
#         self.department=department
#
#     def post_details(self):
#             if self.department.upper()=='HR':
#                 self.basic=30000
#             else:
#                 self.basic=25000
#
#             self.houserent=100000
#             self.transport=5000
#             print("the post of %s is %s"%(self.name,self.post))
#
#     def salary(self):
#             salary=self.basic+self.houserent+self.transport
#             return salary
# class Clerk:
#     def __init__(self,name):
#         self.name=name
#         self.post="clerk"
#
#     def post_details(self):
#             self.basic = 100000
#             self.transport=2000
#             print("the post of %s is %s"%(self.name, self.post))
#
#     def salary(self):
#         salary = self.basic + self.basic+ self.transport
#         return salary
#
# manager= Manager("Kabir","hr")
# clerk=Clerk("Robin")
#
# for obj in (manager,clerk):
#     obj.post_details()
#     print(obj.salary())
class Bird:
    def intro(self):
        print("there are different typesof birds")
    def flight(self):
        print("most of the birds can fly but some cannot")
class parrot(Bird):

    def flight(self):
        print("parrots can fly")


class penguin(Bird):

    def flight(self):
        print("penguin can't fly")

objp=parrot()
objpe=penguin()
for obj in (objp,objpe):
    obj.flight()