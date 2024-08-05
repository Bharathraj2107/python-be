#args
# def add(*num):
#     sum=0
#     for n in num:
#         sum=sum+n
#     print("sum",sum)
# add(2,6)
# add(3,4,5,6,7)
# add(1,2,3,5,6,7,8)

# def person(**kwargs):
#     for key,value in kwargs.items():
#         print("{}-{}".format(key,value))
# person(Name="sean",gen='male',age=38,city="london",mobile=9375821987)
#
# def func(a,b,*args,**kwargs):
#     print(a,b)
#     print(args)
#     print(kwargs)
# func(1,3,10,20,Name="tom",salary=60000)

def intro(**data):
    print("\n Data type of argument:",type(data))
    for key,value in data.items():
        print("{} is {}".format(key,value))
intro(Firstname="sita",Lastname="sharma",age=22,phone=123567890)
intro(Firstname="john",Latname="wood",Email="johnwood@nomail.com",country="wakanda",age=25,phone=9876543210)