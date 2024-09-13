# #lock it will block all threads until it executes
# import threading
# import time
# class BankAccount():
#     def __init__(self,name,balance):
#         self.name=name
#         self.balance=balance
#
#     def __str__(self):
#         return  self.name
#
# #these accounts are our shared resources
# account1=BankAccount("account1",100)#new thread
# account2=BankAccount("account2",0)
#
# #creating lock for threads
# lock=threading.Lock()
#
# class BankTransferThread(threading.Thread):
#     def __init__(self,sender,receiver,amount):
#         threading.Thread. __init__(self)
#         self.sender=sender
#         self.receiver=receiver
#         self.amount=amount
#     def run(self):
#         lock.acquire()
#         sender_initial_balance=self.sender.balance
#         sender_initial_balance-=self.amount
#         #inserting delay to allow switch between threads
#         time.sleep(0.001)
#         self.sender.balance=sender_initial_balance
#
#         receiver_initial_balance=self.receiver.balance
#         receiver_initial_balance+=self.amount
#     #inserting delay to allow switch between threads
#         time.sleep(0.001)
#         self.receiver.balance=receiver_initial_balance
#
#
#         lock.release()
#
# if __name__=='__main__':
#
#     threads=[]
#
#     for i in range(100):
#         threads.append(BankTransferThread(account1,account2,1))#1 thread at a time
#
#     for thread in threads:
#         thread.start()
#     for thread in threads:
#       thread.join()
#
#     print(account1.name,account1.balance)
#     print(account2.name,account2.balance)
#
# lock=threading.Lock()
# x=100
# def thread_task(amt):
#     time.sleep(1)
#     lock.acquire()
#     global x
#     x=x-amt
#     print(x)
#     lock.release()
#
# for i in range(10):
#     t1=threading.Thread(target=thread_task,args=(10,))
#
#     t1.start()
#     t1.join()
#rlock it knows which thread is next
# from threading import *
# import time
# l=RLock()
# def factorial(n):
#     l.acquire()
#     if n==0:
#         result=1
#     else:
#         result=n*factorial(n-1)
#     l.release()
#     return result
# def results(n):
#     print("The factorial of",n,"is:",factorial(n))
#
# t1=Thread(target=results,args=(5,))
# t2=Thread(target=results,args=(9,))
#
# t1.start()
# t2.start()
# t1.join()
# t2.join()
#semaphore at a time how many threads release
from threading import *
import time
s=Semaphore(3)

def call_names(name,age):
    for i in range(3):
        s.acquire()
        print("Hi",name)
        time.sleep(2)
        s.release()
t1=Thread(target=call_names,args=("siresh",15))
t2=Thread(target=call_names,args=("Nitya",20))
t3=Thread(target=call_names,args=("Shiva",16))
t4=Thread(target=call_names,args=("Ajay",25))

t1.start()
t2.start()
t3.start()
t4.start()
