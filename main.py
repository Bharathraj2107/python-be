class user:
    def __init_(self,name,age):
       self.name=name
       self.age=age
       self.msg= self.name + "is" + str(self.age) + "years old"

o = user("ram",25)
print(o.name)
