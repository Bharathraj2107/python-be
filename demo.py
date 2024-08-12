# print("arithmetic operators")
# a=int(input("enter the value of a"))
# b=int(input("enter the value of b"))
# c=a+b
# print(c)
# c=a-b
# print(c)
#
# c=a*b
# print(c)
#
# c=a/b
# print(c)
# c=a%b
# print(c)
# print("assignment operator")
# a+=10
# a-=10
# a*=10
# a/=10
# a%=10
# print("logical operator")
# a=input("enter a ")
# b=input("enter b")
# print(a and b)
# print(a or b)
# a=10
# b=20
# print(a&b)
# print(a|b)
# print(a ^ b)
# print(~a)
# print(a>>2)
# print(a<<2)
# print("comparison")
# print(a!=b)
# print(a>b)
# print(a<b)
# print(a<=b)
# print(a>=b)
# print(a==b)
a=[1,2,3,4,5,6,7]
# b=[]
# print(dir(a))
# a.append(8)
# print(a)
# print(a.clear)
# b=a.copy()
# print(b)
# print(a[2])
# print(a.insert(1,12))
# print(a.pop())
# print(a.remove(3))
# a.reverse()
# print(a)
#
# a.sort(reverse=True)
# a=[1,2,3,4,5,6,7]
# print(a[0:3])
# print(a[-5:])
# print(a[:-5])
# print(a[:-1])
# print(a)
# a=10
# print(~a)
# # a.extend(b)
# # print(a)
# # print()
# b=(1,5,6,1,13,12)
# # print(b.count(1))
# print(type(b))
# d=sorted(b)
#
# print(d)
# print(type(d))
# print(b.index(13))
# print(b)
# print(b)
# print(dir(b))


#packing and unpacking
#fname=('rohan','rot','joy')
#lname=('Raj','joe','mou')
#age=(20,23,67)
#res=zip(fname,lname,age)
# print(res)
#customers=tuple(res)
#print(customers)
# fname,lname,age=customers[2]#here it stores the value in the  fname and lname and age
#a=customers[2]
#print(a)
# print(f"{fname} {lname} is {age} years old")
# a=[1,3,4,8,9,6,2,2]
# nested_list = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# nested_list[1][0]=20
# b=nested_list
# print(b)
# a.append('tom')
# a.extend([10,12])
# a.insert(1,2)
# a.clear()
# a[0]=0
# b=a.index(4)
# b=sorted(a)
# a.reverse()
# b=a.copy()
# b=sum(a)
# print(b)
# print(a[-1])
# print(a[:3])
# print(a[2:])
#difference between sort and sorted in list
# nested_tuple = (1, 2, (3, 4), (5, 6))
# b=nested_tuple[2][0]
# print(b)  # Output: (1, 2, (3, 4), (5, 6))
# tuple_data = (5, 2, 3, 1, 4)
# sorted_tuple = sorted(tuple_data)
# print(sorted_tuple)  # Output: [1, 2, 3, 4, 5]
# print(tuple_data)    # Output: (5, 2, 3, 1, 4) (original tuple is unchanged)
# my_dict={'a':10,'b':20,'c':30}
# print(my_dict.get('b'))
# print(list((my_dict.items()))[1][0])
# print(list(my_dict.keys()))
# print(list(my_dict.values()))




# the benefits are
# 1)it is both structure and object oriented
# 2)there is no compilation time
# 3)it consumes less time
# 4)it is more advanced in the current world
# 5)it executes line by line;

# 2)mutable-the values that can be changed when ever required is
#  called mutable-ex:list
# immutable-the values that cannot be changed once declared
# called immutable-ex:tuple

# 3)
# a=int(input("enter the value of a"))
# b=int(input("enter the value of b"))
# temp=a
# b=a
# temp=b

# 4)
# a=[]
# b=int(input("enter the values"))
# a.append(b)
# print(f"the list is ",a)
# c=tuple(a)
# print("the tuple is",c)

# 5)
# a=(11,22)
# d=sorted(a)//[11,22]
# for num in d:
#     e.append(d)
#     print(e)
# e=(99,88)
# f=sorted(e)//[99,88]
# for num in f:
#     a.append(f)
#     print(a)
# //swap(a,b)

# list
# list=[1,2,3,4]
# for i in list:
#     print(i)
# for j in range(4):
#   print(list[j])

# 2)
# list=[1,2]
# list.insert(1,12)

# 3)
# list=[1,2,3,4,5,6]
# list.sort()
# print(list)
# list.sort(reverse=True)
# print(list)

# 4)
# list=[1,2,9]
# min_val=list.min()
# max_val=list.max()

# 5)
# list1=[1,2,3,4,5]
# for i in list1:
#   i=i*i
#   print(i)

# list2=[1,2,3,4,5]
# for j in list2:
#     t=j=j*j
#     t=t*j
#     print(t)

#Tuple
# l=(1,2,3)
# g=len(l)
# print(g)
# 2)
# week_tuple=("Monday","Tuesday","wednesday","Thursday","Friday","Saturday","Sunday")
# b=week_tuple.index('wednesday')
# print(b)
# c=week_tuple.count("Monday")
# print(c)

# set
# set={1,2,3,4}
# set.remove(2)
# print(set)

# set={1,2,3,4}
# i=int(input("enter the number to find"))
# if i in set:
#    print("the number is present in the set "
#          )
# else:
#    print("not found")
# list=[1,2,3]
# set={}
# for i in list:
#  set.add(i)
#   i=i+1;
# print(set)
# print(set.__dict__)
# add memebers
# set={1,2,3,4,5}
# if i in set
# if i not in set

#dict
# car={"model":'swift',"color":'green',"tiers_count":4,"numberof_seats":4,"kmph":5,"price":500000}
# print(car)

nums=[2,7,11,15]
target=9

# def two_sum(nums,target):
#     for i in nums:
#         ans=target-i
#         list.append(ans)
#     if next in list:
#         return nums[i]
# print(
#     b=two_sum(nums, target)
#
# print(answer)
# def two_sum(nums, target):
#     for i in range(len(nums)):
#         for j in range(i+1,len(nums)):
#             if nums[i]+nums[j]==target:
#              return i,j
# print(two_sum(nums, target))
# #largest element
# array=[1,2,3,4,5]
# a=max(array)
# print(a)
# #second largest element
# array=[1,2,3,4,5]
# array.sort(reverse=True)
# print(array[1])
#remove duplicates
# array=[1,1,2,5,4,3,4,5,1,2,2,3,4,5]
# duplicate_removed=set(array)
# print(duplicate_removed)
#union of the array
arr1=[1,2,3,4,5,6]
arr2=[4,5,6,7,8,9]
# arr1.extend(arr2)
# # print(arr1)
# union=set(arr1)
# print(union)
#intersection of sorted  array
# list=[]
# for i in arr1:
#     for j in arr2:
#      if i==j:
#         list.append(i)
# print(list)
# arr=[1,2,3,4,5,6,7,8,9]
# print(arr.index(2))
# list=[]
# arr=[0,1,2,3,4,5,0,0,0,4,5,0,8]
# arr.sort(reverse=True)
# print(arr)
# arr=[9,5,4,3,8,7,2,1,6]
# arr1_s=arr.sort()
# if arr1==arr:
#     print("sorted")
# else:
#     print("unsorted")
#
# arr=[1,2,3,4,5]
# b=arr.pop(0)
# arr.append(b)
# print(arr)
#string
# a="mmadam"
# b=set(a)
# print(b)
# b=a[::-1]
# if a==b:
#     print("yes")
# else:
#     print("no")

