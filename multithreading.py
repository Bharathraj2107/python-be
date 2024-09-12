from threading import *
def m1():
    for i in range(3):
        print("Good Morning")

def m2():
    for i in range(3):
        print("Good Evening")


def m3():
    for i in range(3):
        print("Good Night")
print("--------------------------------------")
print("\tMultithreading")
print("----------------------------------------")
##creating objects for multiple threads
t1=Thread(target=m1,name="Morning")#giving the name for the thread is name here target is m1 first method
t2=Thread(target=m2,name="Evening")
t3=Thread(target=m3,name="Night")
##start threads by calling the start method
t1.start()
t2.start()
t3.start()