#single inheritance
class person:
    def __init__(self,firstname,lastname):
        self.firstname=firstname
        self.lastname=lastname

    def fullname(self):
            print(self.firstname," ",self.lastname)

class student(person):
    def __init__(self,firstname,lastname,grade):
        self.grade=grade
        super().__init__(firstname,lastname)#calling base constructor

    def display_detail(self):
        super().fullname()#calling base class method
        print('grade',self.grade)

std=student('james','bond')

std.display_detail()

