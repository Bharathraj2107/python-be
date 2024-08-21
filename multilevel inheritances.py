# class person:
#     def __init__(self,name1):
#         print(name1,"is a person")
#
#
# class Doctor(person):
#     def __init__(self, name2):
#         print(name2, "is doctor")
#         super().__init__(name2)# to print name argument we use super
# class Engineer(Doctor):
#     def __init__(self, name3):
#         print(name3, "is a Engineer")
#         super().__init__(name3)# to print name argument we use super it is constructor so  it will not return
#
# E1=Engineer('vishwajith')#it will pass the value to all the argumnets at a time init functions at  a time it executes

#multiple inheritances

class al:
    def __init__(self,al):
        print(al,"is an animal")

class ml(al):
    def __init__(self,m_name):
        print(m_name,"can't fly")
        super().__init__(m_name)
class Nonwingedml(ml):
    def __init__(self,Nonwingedml):
        print(Nonwingedml,"can't swim")
        super().__init__(Nonwingedml)


class NonMarineml(ml):
    def __init__(self,NonMarineml):
        print(NonMarineml,'is a warm-blooded animal')
        super().__init__(NonMarineml)

class Dog(NonMarineml,Nonwingedml):
    def __init__(self,name):
        print(name ,'has 4 legs')
        super().__init__(name)
d=Dog('blacky')
print('')
bat=NonMarineml('Bat')