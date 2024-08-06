class cars:
    # def __init__(self,name,color,price):
    #     self.name=name
    #     self.color=color
    #     self.price=price
    def cars_info(self):
       self. name=input("enter name")#we haveto use self compulsory
       self. color=input("enter the color")
       self. price = input("enter the price")
    def display(self):
        print(self.name,self.color,self.price)
c1=cars()
c1.cars_info()
c1.display()