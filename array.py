import array as arr
#numbers=arr.array('i',[10,20,30,40,50])
#print(numbers)
#print("------------------------------------")
# for x in numbers:
#   print(x)
# a=arr.array('d', [1.1,2.1,3.1] )
# print(a[1])
# a=arr.array('d', [1.1,2.1,3.1] )
# print(len(a))
# a=arr.array('d', [1.1,2.1,3.1] )
# a.append(3.4)
# print(a)
# a.extend([4.5,6.3,6.8])
# print(a)
# a=arr.array('d',[1.1,2.1,3,1,2.6,7.8])
# b=arr.array('d',[3.7,8.6])
# a.insert(1,3.8)
# print(a)
#in one dimensional array + will concatinate
# a=arr.array('d',[1.1,2.1,3,1,2.6,7.8])
# b=arr.array('d',[3.7,8.6])
# c=arr.array('d')
# c=a+b
# print("array c=",c)
#find the sum of all array elements
# sum=0
# a=arr.array('i',[1,2,3,4,5])
# for x in a:
#     sum+=x
# print(sum)
# for i in a:
#      c+=i
# print(c)
#reverse an aray
# a=arr.array('i',[1,2,3,4,5])
# print(a[::-1])
#even number and sum
# sum=0
# a=arr.array('i',[1,2,3,4,5,6])
# for x in a:
#     if x%2==0:
#         sum+=x
# print(sum)
#slicing to an array
# a=arr.array('i',[1,2,3,4,5,6])
# print(a[1:3])
# a=arr.array('i',[9,2,3,4,5,6])
# a.remove(9)
# print(a)
# a=arr.array('i',[2,3,4,5,6])
# for s in a:
#     st=s*s
#     print("square",st)
#     cu = s * s * s
# print("cubes",cu)
# a=arr.array('i',[2,3,4,5,6])
# max=a[0]
# min=a[0]
# for x in a:
#     if x>max:
#         max = x
#     if x< min:
#         min=x
# print("the largest is ",max)
# print("the smallest is ",min)
# min=min(a)
# print(min)
# max=max(a)
# print(max)

#multi dimensional array
import numpy as np
# T=[[11,12,5,2],[15,6,10,5],[10,8,12,5],[12,15,8,6]]
# print(T)
# T.insert(2,[0,5,11])
# for r in T:
#     for c in r:
#         print(c,end=' ')
#     print()

# arr1=[[0]*3]*2
# print(arr1)
# print(type(arr1))

#matrix using join function
#the join() method is a string method and returns a string in which the element of the sequence have been joined by the str separartor
# m=[[1,2,3],[7,1,5],[0,9,3]]
# for i in m:
#     print("".join(str(i)))
from numpy import reshape,arange,ones,zeros,eye
# a=ones((3,4),float)
# print(a)
# b=zeros((3,4),int)
# print(b)
# c=eye(3)
# print(c)
#
# a=[1,2,3,4,5,6]
# # b=reshape(a,(2,3))
# # print(b)
# b=reshape(a,(3,2))
# print(b)
# a=arange(12)
# print(a)
# b=reshape(a,(2,3,2))#here 1st value is number of matrix and 2 nd is rows and 3 rd is column
# print(b)
# a=arange(9)
# b=reshape(a,(3,3))
# print(b)
# print("--------------------")
# c=reshape(a,(3,3))
# print(c)
# print("----------")
# sum=b+c
# print(sum)

# import numpy as np
# a=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
# print(a[1:3,1:3])#here 1:3 of first for consider 2 list and 1:3for element selection range
#print(a[:,1:2])
# print(a[1,:])
# print(a[1:])
# print(a[:,1])
# a=np.array([20,30,40,50])
# b=np.arange(4)
# # print(a+b)
# print(np.add(a,b))
# # print(a-b)
# print(np.subtract(a,b))
# A=np.array([[1,1],[6,1]])
# B=np.array([[2,8],[3,4]])
# print(np.multiply(A,B))
# print(np.divide(A,B))
# print(B**2)
# cars=["toyota","wagner","mustang"]
# # for i in cars:
# #     print(i)
# # cars.append("lamborgini")
# print(cars.remove("toyota"))
# print(cars)
# print(len(cars))
# print(cars[0])
# cars[0]="audi"
# print(cars[0])
# fruits = ['apple', 'banana', 'cherry', 'orange']
# print(fruits)
# x = fruits.count('cherry')
# print(x)
# fruits = ['apple', 'banana', 'cherry']
#
# cars = ['Ford', 'BMW', 'Volvo']
#
# fruits.extend(cars)
# print(fruits)
# fruits = ['apple', 'banana', 'cherry']
# fruits.insert(1,"mango")
# print(fruits)
# # fruits.pop()
# # fruits.reverse()
# x=fruits[::-1]
# print(x)
#
# cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']
#
# cars.sort(len(cars))
# def myFunc(e):
#   return len(e)
#
# cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']
#
# cars.sort(key=myFunc)
# print(cars)
# cars = ['Ford', 'BMW', 'Volvo']
#
# cars.sort(reverse=True)
# print(cars)
#strings
# a = """Lorem ipsum dolor sit amet,
# consectetur adipiscing elit,
# sed do eiusmod tempor incididunt
# ut labore et dolore magna aliqua."""
# print(a)
# a = "Hello, World!"
# print(a[1])
# for x in "banana":
#   print(x ,end="")
# a = "Hello  World!"
# print(len(a))
# txt = "The best things in life are free!"
# print("free" in txt)
# b = "Hello, World!"
# print(b[-5:-2])
# txt = "hello, and welcome to my world."
#
# x = txt.capitalize()
#
# print (x)
# txt = "Hello, And Welcome To My World!"
#
# x = txt.casefold()
#
# print(x)
import array as arr
numbers=arr.array('i',[10,20,30])
numbers1=arr.array('i',[40,50,60])
# numbers2=arr.array('i')
# print(numbers[1])
# print(len(numbers))
# numbers.append(40)
# numbers.insert(1,50)
# numbers.extend(numbers1)
numbers2=numbers+numbers1
# print(numbers2)
#print(numbers2.pop())
# print(numbers2.pop(1))
#print(numbers2.remove(40))
# print(numbers2[0:3])
# for x in numbers2[1:3]:
#     print(x)
# T=[[11,12,5,2],[15,6,10,5],[10,8,12,5],[12,15,8,6]]
# T.insert(2,[0,5,11,13,6])
# for r in T:
#     for c in r:
#         print(c,end=" ")
#     print()
# o=ones((3,4),int)
# print(o)
# b=eye(3)
# print(b)
# a=[1,2,3,4,5,6]
# b=reshape(a,(2,3))
# print(b)