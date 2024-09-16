import time
from queue import PriorityQueue
import threading
# import time
#
# #implementing priority queues using list
# student=[]#5>highest less than
# student.append([5,'Nick'])
# student.append([6,'Sachin'])
# student.append([1,'Rohan'])
# student.append([3,'Jack'])
# #student.sort(reverse=True)
# while student:
#     t=student.pop()
#     print(t)
#     time.sleep(3)
#     print(student)
# # #The list will be sorted based on the highest priority
# import heapq
# s_roll=[]
# heapq.heappush(s_roll,(4,"Tom"))
# heapq.heappush(s_roll,(1,"Aruhi"))
# heapq.heappush(s_roll,(3,"Dyson"))
# heapq.heappush(s_roll,(2,"Bob1"))
# heapq.heappush(s_roll,(7,"Bob2"))
# heapq.heappush(s_roll,(6,"Bob3"))
# heapq.heappush(s_roll,(5,"Bob"))
# while s_roll:
#     deque_r=heapq.heappop(s_roll)
#     print(deque_r)
#     time.sleep(3)
#     print(s_roll)
# #Inside the while loop,the "heapq.heapop() function remove"
# #the list element in ascending order
# #implementing priority queues using queue.priorityqueue
# import queue
# students=queue.PriorityQueue()
# students.put((3,"Henry"))
# students.put((4,"Lily"))
# students.put((1,"Joseph"))
# students.put((2,"Anna"))
# students.put((6,"Anna1"))
# while not students.empty():
#     print(students.get())
#Daemon threads (main Thread)backend running threads called as daemon
import threading
from threading import Thread
import time
#before setting daemon thread as true
# def show_time():
#     count=0
#     while True:
#         count+=1
#         time.sleep(1)
#         print(f"Has been waiting for{count} seconds(s)")
#     t=Thread(target=show_time)
#     t.start()
#     answer=input("Do you want to exit?\n")

#once we set the daemon thread
def show_timer():
    count=0
    while True:
        count+=1
        time.sleep(1)
        print(f"Has been waiting for{count} seconds(s)..")
t=Thread(target=show_timer,daemon=True)
t.start()
answer=input("Do you want to exit?\n")