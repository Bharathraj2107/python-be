import threading
import time
from threading import *
# def m1():
#     for i in range(3):
#         print("Good Morning")
# def m2():
#     for i in range(3):
#         print("Good Evening")
# def m3():
#     for i in range(3):
#         print("Good Night")
#
# print("--------------------------------------")
# print("\tMultithreading")
# print("----------------------------------------")
# ##creating objects for multiple threads
# t1=Thread(target=m1,name="Morning")#giving the name for the thread is name here target is m1 first method
# t2=Thread(target=m2,name="Evening")
# t3=Thread(target=m3,name="Night")
# ##start threads by calling the start method
# t1.start()
# t2.start()
# t3.start()
#here we are using join-util and unless t1 says join t2 cannot do running it will be in runable state
# def m1():
#     for i in range(3):
#         print("Good Morning")
# def m2():
#     for i in range(3):
#         print("Good Evening")
# def m3():
#     for i in range(3):
#         print("Good Night")
#
# print("--------------------------------------")
# print("\tMultithreading")
# print("----------------------------------------")
# ##creating objects for multiple threads
# t1=Thread(target=m1,name="Morning")#giving the name for the thread is name here target is m1 first method
# t2=Thread(target=m2,name="Evening")
# t3=Thread(target=m3,name="Night")
# ##start threads by calling the start method
# #start thread 1
#
# t1.start()
# #wait until thread 1 is finished (main and sub threads t2,t3 should wait)
# t1.join()
# #start thread 2 after thread 1
# t2.start()
# #wait until thread 1 is finished (main and sub threads t1,t3 should wait)
# t2.join()
# #start thread 3 after thread 2
# t3.start()
# #wait until thread 1 is finished (main and sub threads t2,t3 should wait)
# t3.join()
# #end of the main thread
# print("END of the main thread")
# #detect the current execution thread
# def m1():
#     tname=threading.current_thread().getName()#get name gives the currrent thread which is executing
#     print("current Thread\t:",tname)
#     print("good Morning")
# def m2():
#     tname=threading.current_thread().getName()
#     print("current Thread\t:",tname)
#     print("good Evening")
# def m3():
#     tname=threading.current_thread().getName()
#     print("current Thread\t:",tname)
#     print("good night")
# #main thread
# print("-----------------------------------------")
# print("\tFinding current thread-Multithreading")
# print("---------------------------------------")
# # #creating objects for multiple threads
# # t1=Thread(target=m1,name="Morning")
# # t2=Thread(target=m2,name="Evening")
# # t3=Thread(target=m3,name="Night")
# # t1.start()
# # t2.start()
# # t3.start()
# def cal_sqre(num):
#     print("calculate the square root of the given number")
#     for n in num:
#         time.sleep(0.3)#at each iteration it waits for 0.3 time
#         print('square is :',n*n)
# def cal_cube(num):
#     print("calculate the cube of the given number")
#     for n in num:
#         time.sleep(0.3)#at each iteration it waits for 0.3 time
#         print('cube is :',n*n*n)
# arg=[4,5,6,7,2]
# t=time.time()#get total time to execute the functions
# cal_sqre(arg)
# cal_cube(arg)
# th1=threading.Thread(target=cal_sqre,args=(arg,))
# th2=threading.Thread(target=cal_cube,args=(arg,))
# th1.start()
# th2.start()
# th1.join()
# th2.join()
# print("Total time taken by threads is :",time.time()-t)#print the total time
# print("Again executing the main thread")
# print("Thread 1 and thread 2 have finished their execution")
import _thread
import time
# def my_thread(thrd_msg,delay):
#     count=0
#     while count<3:
#         time.sleep(delay)
#         count+=1
#         #print--will display which thread in executed and time taken
#         print(thrd_msg,"------",time.time())#here time time is time taken to execute
# #now the thread fun need to be executed
# try:
#     _thread.start_new_thread(my_thread("thread 1",1))
#     _thread.start_new_thread(my_thread("thread 2",2))
# except:
#     print("some error occured")
# while 1:
#     pass
def calc_square(numbers,delay):
    for n in numbers:
        print(f"\n {n} ^ 2={n*n}")
        time.sleep(delay)
def calc_cube(numbers,delay):
    for n in numbers:
        print(f"\n {n} ^ 3={n*n*n}")
        time.sleep(delay)
numbers=[2,3,5,8]
square_thread=threading.Thread(target=calc_square,args=(numbers,1))
cube_thread=threading.Thread(target=calc_cube,args=(numbers,2))

square_thread.start()
cube_thread.start()

square_thread.join()
cube_thread.join()
print("Thread execution done")