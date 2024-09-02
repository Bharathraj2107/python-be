#for protected variable
# class Employee:
#     def __init__(self,name,project):
#         self._name=name#protected bcoz  of single underscore
#         self._project=project
#
# emp=Employee("Team Be-practical",1)
# print("Name",emp._name)
# print("project",emp._project)

#global variable
# num=99889897645
# s_id=["bepractical"]
# pas=815689
# id_c=input("enter your id")
# pa=int(input("enter the password"))
# class student:
#     def check_give(self):
#         self._num=num
#         self.s_id=s_id
#         self.pas=pas
#         self.pa=pa
#         self.id_c=id_c
#         if id_c in s_id and pa==pas:
#             print(num)
#         else:
#             print("wrong id or password")
# s=student()
# s.check_give()

#for private variable
# class Employee:
#     def __init__(self,name,project):
#         self.name=name
#         self.__project=project#private variable
# emp=Employee("Be-Practical Team",1)
# #accessing public variable
# print("Name",emp.name)
# #accessing private variable
# print("Project",emp._Employee__project)
#here for private variable only the parent class can access  emp is object and ,_employeee is the class and__project
class Teacher:
   def __init__(self,val1,val2,val3):
       self.val1=val1
       self._val2=val2
       self.__val3=val3
   def dispublicMembers(self):
       print("This is public number",self.val1)
   def _disprotectedMember(self):
       print("this is protected member",self._val2)

   def __disprivateMembers(self):
        print("This is private member",self.__val3)
   def accessprivateMember(self):#here we using public method to accesss private method from child class
       self.__disprivateMembers()

class child(Teacher):
     def __init__(self,val1,val2,val3):
         Teacher.__init__(self,val1,val2,val3)

     def accessprotectmember(self):
            self._disprotectedMember()

obj1=child("Hello","simon",100000)
obj1.dispublicMembers()
obj1._disprotectedMember()
obj1.accessprivateMember()
#obj1.disprivateMembers()#child class can't access the private method of the parent calss
#school bag is one of the most real example of encapsulation.school bag
#can keep our books ,pens etc
#we should make public items some,private some variables add that element and remove that element