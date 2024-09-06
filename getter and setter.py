# class Person:
#     def __init__(self,name,age=0):
#         self.name=name
#         self.__age=age
#     def display(self):
#         print(self.name)
#         print(self.__age)
#
#     def getAge(self):
#         print(self.__age)
#
#     def setAge(self,age):
#         self.__age=age
#
# print("The age of the person is")
# person=Person('Dev',30)
# #accessing using class method
# person.display()
# #changing age using setter
# print("after revising the age of the person")
# person.setAge(35)
# person.getAge()
#for getter and setter we use to access outside the class
# class stud_abc:
#     def __init__(self,totalMarks=0,totalSub=0):
#         self.__totalMarks=totalMarks
#         self.__totalSub=totalSub
#
#     #getter method
#     def get_totalMarks(self):
#         return self._totalMarks
#
#     #setter method
#     def set_totalMarks(self,x):
#         self._totalMarks=x#here we can change this to public or protected in get and set method
#
#     #getter method
#     def get_totalSub(self):
#         return self._totalSub
#
#     #setter method
#     def set_totalSub(self,y):
#         self._totalSub=y
#
# student=stud_abc()
# #setting thr totalMarks using setter
# student.set_totalMarks(349)
# #setting the totalsubusing using setter
# student.set_totalSub(5)
#
# #retrieving totalmarks using getter
# print("Total Marks"+str(student.get_totalMarks()))
# #retrieving totalsub uding getter
# print("total sub"+str(student.get_totalSub()))
# #caluclate average
# print("Average"+str(student._totalMarks / student._totalSub))
# class student:
#     def __init__(self,name=0,marks=0):
#         self.__name=name
#         self.__marks=marks
#     def get_marks(self):
#         return self.marks
#     def set_marks(self,x):
#         self.marks=x
#     def get_name(self):
#         return self.name
#     def set_name(self,y):
#          self.name=y
#
# ram=student()
# ram.set_marks(10)#first set then call get
# ram.set_name("krishna")
# print("name:",ram.get_name())
# print("marks:",ram.get_marks())
#other form 
class student(object):
    def _init_(self, name:str):
        self.name:str=name
        self.__marks:int=0


    def get_marks(self):
        return self.name+" got"+str(self.__marks)

    def set_marks(self,marks:int):
        self.__marks= marks

    def _str_(self):
        return "student name is "+ self.name


stud = student("vinayak")
print(stud)
stud.set_marks(10)
marks_stud_got=stud.get_marks()
print(marks_stud_got)